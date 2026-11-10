#!/usr/bin/env python3
"""Deterministic XOS QC register projection over Paperclip native evidence.

This tool is deliberately read-only. It does not mutate Paperclip, invent missing
review facts, or duplicate Completed by / Reviewed by columns in the core issues
schema. It projects those fields from native run, interaction, work-product, and
issue evidence, with optional reviewed supplements for facts Paperclip does not
natively capture (for example Reg's verbatim request or the applicable canon
revision).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Iterable

QC_VERDICTS = {"PASS", "FAIL_RETURN", "NEEDS_EVIDENCE", "HUMAN_BLOCKER"}


def _iso(value: Any) -> str:
    return str(value or "")


def _lower(value: Any) -> str:
    return str(value or "").strip().lower()


def _run_id(run: dict[str, Any]) -> str:
    return str(run.get("runId") or run.get("id") or "")


def _outcome(interaction: dict[str, Any]) -> str:
    result = interaction.get("result") or {}
    return _lower(result.get("outcome") or result.get("verdict") or result.get("qcVerdict"))


def _interaction_text(interaction: dict[str, Any]) -> str:
    payload = interaction.get("payload") or {}
    parts = [
        interaction.get("title"),
        interaction.get("summary"),
        payload.get("prompt"),
        payload.get("detailsMarkdown"),
        payload.get("summary"),
    ]
    return " ".join(str(x) for x in parts if x).lower()


def _target(interaction: dict[str, Any]) -> dict[str, Any]:
    payload = interaction.get("payload") or {}
    target = payload.get("target")
    return target if isinstance(target, dict) else {}


def is_plan_interaction(interaction: dict[str, Any]) -> bool:
    target = _target(interaction)
    if _lower(target.get("key")) == "plan":
        return True
    text = _interaction_text(interaction)
    phrases = (
        "approve the plan",
        "approve plan",
        "approve this plan",
        "plan for xos-",
        "qc standard plan",
    )
    return any(p in text for p in phrases)


def is_review_interaction(interaction: dict[str, Any]) -> bool:
    if _lower(interaction.get("status")) not in {"accepted", "rejected", "declined", "resolved"}:
        return False
    if is_plan_interaction(interaction):
        return False
    text = _interaction_text(interaction)
    review_words = ("review", "qc", "accept", "approve", "signoff", "sign-off", "decision")
    has_review_word = any(word in text for word in review_words)
    has_resolver = any(
        interaction.get(k)
        for k in ("resolvedByAgentId", "resolvedByUserId", "resolvedByRunId")
    )
    return has_review_word or has_resolver


def explicit_qc_verdict(interaction: dict[str, Any]) -> str | None:
    containers: list[dict[str, Any]] = []
    for value in (interaction.get("result"), interaction.get("payload")):
        if isinstance(value, dict):
            containers.append(value)
    for container in containers:
        for key in ("qcVerdict", "qc_verdict", "verdict"):
            value = str(container.get(key) or "").upper()
            if value in QC_VERDICTS:
                return value
    return None


class PaperclipCLI:
    def __init__(self, company_id: str, command: list[str] | None = None) -> None:
        self.company_id = company_id
        self.command = command or ["npx", "--no-install", "paperclipai"]

    def json(self, *args: str) -> Any:
        proc = subprocess.run(
            [*self.command, *args],
            text=True,
            capture_output=True,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(
                f"Paperclip command failed ({proc.returncode}): "
                f"{' '.join(args)}\n{proc.stderr[-2000:]}"
            )
        try:
            return json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                f"Paperclip command returned non-JSON for {' '.join(args)}"
            ) from exc

    def agent_names(self) -> dict[str, str]:
        rows = self.json(
            "agent", "list", "--company-id", self.company_id, "--json"
        )
        result: dict[str, str] = {}
        for row in rows if isinstance(rows, list) else []:
            agent_id = str(row.get("id") or "")
            if agent_id:
                result[agent_id] = str(row.get("name") or agent_id)
        return result

    def bundle(self, identifier: str) -> dict[str, Any]:
        return {
            "issue": self.json("issue", "get", identifier, "--json"),
            "comments": self.json("issue", "comments", identifier, "--json"),
            "interactions": self.json("issue", "interactions", identifier, "--json"),
            "runs": self.json("issue", "runs", identifier, "--json"),
        }


def load_supplement(path: str | None) -> dict[str, dict[str, Any]]:
    if not path:
        return {}
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("Supplement must be a JSON object keyed by issue identifier")
    output: dict[str, dict[str, Any]] = {}
    for key, value in raw.items():
        if not isinstance(value, dict):
            raise ValueError(f"Supplement entry {key!r} must be an object")
        output[str(key)] = value
    return output


def select_plan_approval(interactions: Iterable[dict[str, Any]]) -> dict[str, Any] | None:
    candidates = [
        i for i in interactions
        if _lower(i.get("status")) == "accepted" and is_plan_interaction(i)
    ]
    return max(candidates, key=lambda i: _iso(i.get("resolvedAt") or i.get("createdAt")), default=None)


def select_completion_run(
    issue: dict[str, Any],
    runs: Iterable[dict[str, Any]],
) -> dict[str, Any] | None:
    succeeded = [r for r in runs if _lower(r.get("status")) == "succeeded"]
    execution_run_id = str(issue.get("executionRunId") or "")
    if execution_run_id:
        for run in succeeded:
            if _run_id(run) == execution_run_id:
                return run
    return max(
        succeeded,
        key=lambda r: _iso(r.get("finishedAt") or r.get("startedAt") or r.get("createdAt")),
        default=None,
    )


def select_review(interactions: Iterable[dict[str, Any]]) -> dict[str, Any] | None:
    candidates = [i for i in interactions if is_review_interaction(i)]
    return max(
        candidates,
        key=lambda i: _iso(i.get("resolvedAt") or i.get("updatedAt") or i.get("createdAt")),
        default=None,
    )


def pending_human_blocker(interactions: Iterable[dict[str, Any]]) -> dict[str, Any] | None:
    candidates = []
    for interaction in interactions:
        if _lower(interaction.get("status")) != "pending":
            continue
        policy = _lower(
            interaction.get("effectiveResolverPolicy")
            or interaction.get("resolverPolicy")
            or interaction.get("requestedResolverPolicy")
        )
        if policy == "human_only":
            candidates.append(interaction)
    return max(candidates, key=lambda i: _iso(i.get("createdAt")), default=None)


def request_evidence(
    issue: dict[str, Any],
    comments: Iterable[dict[str, Any]],
    supplement: dict[str, Any],
) -> dict[str, Any]:
    if supplement.get("reg_request"):
        return {
            "text": str(supplement["reg_request"]),
            "timestamp": str(supplement.get("reg_request_timestamp") or ""),
            "source": str(supplement.get("reg_request_source") or "reviewed_supplement"),
            "verbatim_verified": bool(supplement.get("reg_request_verbatim_verified", True)),
        }

    user_comments = [
        c for c in comments
        if c.get("authorUserId") and str(c.get("authorUserId")) != "local-board"
    ]
    if user_comments:
        row = min(user_comments, key=lambda c: _iso(c.get("createdAt")))
        return {
            "text": str(row.get("body") or ""),
            "timestamp": str(row.get("createdAt") or ""),
            "source": f"issue_comment:{row.get('id')}",
            "verbatim_verified": False,
        }

    return {
        "text": str(issue.get("description") or ""),
        "timestamp": str(issue.get("createdAt") or ""),
        "source": "issue_description",
        "verbatim_verified": False,
    }


def reviewer_identity(
    interaction: dict[str, Any] | None,
    agent_names: dict[str, str],
) -> tuple[str, str, str]:
    if not interaction:
        return "", "", ""
    agent_id = str(interaction.get("resolvedByAgentId") or "")
    user_id = str(interaction.get("resolvedByUserId") or "")
    run_id = str(interaction.get("resolvedByRunId") or "")
    if agent_id:
        return agent_names.get(agent_id, agent_id), agent_id, run_id
    if user_id:
        return user_id, f"user:{user_id}", run_id
    return "", "", run_id


def completion_identity(
    run: dict[str, Any] | None,
    agent_names: dict[str, str],
) -> tuple[str, str, str]:
    if not run:
        return "", "", ""
    agent_id = str(run.get("agentId") or "")
    return agent_names.get(agent_id, agent_id), agent_id, _run_id(run)


def _work_product_review_states(issue: dict[str, Any]) -> list[str]:
    values = []
    for product in issue.get("workProducts") or []:
        state = str(product.get("reviewState") or "none")
        title = str(product.get("title") or product.get("type") or product.get("id") or "work-product")
        values.append(f"{title}:{state}")
    return values


def build_row(
    bundle: dict[str, Any],
    agent_names: dict[str, str],
    supplement: dict[str, Any] | None = None,
) -> dict[str, Any]:
    supplement = supplement or {}
    issue = bundle["issue"]
    comments = bundle.get("comments") or []
    interactions = bundle.get("interactions") or []
    runs = bundle.get("runs") or []

    identifier = str(issue.get("identifier") or issue.get("id") or "")
    request = request_evidence(issue, comments, supplement)
    plan = select_plan_approval(interactions)
    completion = select_completion_run(issue, runs)
    review = select_review(interactions)
    human_blocker = pending_human_blocker(interactions)

    completed_name, completed_agent_id, completed_run_id = completion_identity(
        completion, agent_names
    )
    reviewed_name, reviewed_identity_id, reviewed_run_id = reviewer_identity(
        review, agent_names
    )

    self_review = bool(
        completed_agent_id
        and reviewed_identity_id
        and completed_agent_id == reviewed_identity_id
    )

    plan_target = _target(plan or {})
    plan_revision = str(
        plan_target.get("revisionId")
        or (supplement.get("plan_revision") or "")
    )
    plan_approval_at = str(
        (plan or {}).get("resolvedAt")
        or supplement.get("plan_approval_timestamp")
        or ""
    )

    delivery_at = str(
        issue.get("completedAt")
        or (completion or {}).get("finishedAt")
        or (completion or {}).get("startedAt")
        or ""
    )

    explicit = str(supplement.get("qc_verdict") or "").upper()
    if explicit and explicit not in QC_VERDICTS:
        raise ValueError(f"{identifier}: invalid qc_verdict {explicit!r}")
    if not explicit and review:
        explicit = explicit_qc_verdict(review) or ""

    reasons: list[str] = []
    if self_review:
        verdict = "FAIL_RETURN"
        reasons.append("completed_by and reviewed_by resolve to the same agent")
    elif explicit:
        verdict = explicit
        reasons.append("explicit QC verdict evidence supplied")
    elif human_blocker:
        verdict = "HUMAN_BLOCKER"
        reasons.append(f"pending human-only interaction {human_blocker.get('id')}")
    else:
        verdict = "NEEDS_EVIDENCE"
        if not request["verbatim_verified"]:
            reasons.append("Reg verbatim request is not independently verified")
        if not plan:
            reasons.append("approved plan interaction not found")
        if not completion:
            reasons.append("successful completion run not found")
        if not review:
            reasons.append("independent completion review not found")
        if not supplement.get("canon_revision"):
            reasons.append("applicable XOS canon/SOP revision not supplied")
        if not reasons:
            reasons.append("no explicit QC verdict was recorded")

    review_outcome = _outcome(review or {})
    evidence = {
        "request_source": request["source"],
        "plan_interaction_id": str((plan or {}).get("id") or ""),
        "completion_run_id": completed_run_id,
        "review_interaction_id": str((review or {}).get("id") or ""),
        "review_run_id": reviewed_run_id,
        "work_product_reviews": _work_product_review_states(issue),
        "status": str(issue.get("status") or ""),
    }

    return {
        "issue": identifier,
        "title": str(issue.get("title") or ""),
        "issue_status": str(issue.get("status") or ""),
        "reg_request": request["text"],
        "reg_request_timestamp": request["timestamp"],
        "reg_request_source": request["source"],
        "reg_request_verbatim_verified": request["verbatim_verified"],
        "plan_revision": plan_revision,
        "plan_approval_timestamp": plan_approval_at,
        "planned_due": str(supplement.get("planned_due") or ""),
        "actual_delivery_timestamp": delivery_at,
        "completed_by": completed_name,
        "completed_by_agent_id": completed_agent_id,
        "completed_by_run_id": completed_run_id,
        "reviewed_by": reviewed_name,
        "reviewed_by_identity": reviewed_identity_id,
        "reviewed_by_run_id": reviewed_run_id,
        "review_outcome": review_outcome,
        "independent_review": bool(reviewed_identity_id and not self_review),
        "canon_revision": str(supplement.get("canon_revision") or ""),
        "canon_compliance": str(supplement.get("canon_compliance") or "NEEDS_EVIDENCE"),
        "qc_verdict": verdict,
        "qc_reason": "; ".join(reasons),
        "evidence": evidence,
    }


def _md(value: Any) -> str:
    text = str(value or "")
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")


def render_markdown(rows: list[dict[str, Any]]) -> str:
    header = (
        "| Issue | Reg original ask / received | Approved plan | Planned due | "
        "Actual delivery | Completed by | Reviewed by | XOS canon / SOP | QC verdict |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
    )
    body = []
    for row in rows:
        request_label = row["reg_request"] or "MISSING"
        if not row["reg_request_verbatim_verified"]:
            request_label = "NEEDS_EVIDENCE: " + request_label
        plan = row["plan_revision"] or "NEEDS_EVIDENCE"
        if row["plan_approval_timestamp"]:
            plan += f" @ {row['plan_approval_timestamp']}"
        completed = row["completed_by"] or "NEEDS_EVIDENCE"
        if row["completed_by_run_id"]:
            completed += f" / run {row['completed_by_run_id']}"
        reviewed = row["reviewed_by"] or "NEEDS_EVIDENCE"
        if row["review_outcome"]:
            reviewed += f" / {row['review_outcome']}"
        canon = row["canon_revision"] or "NEEDS_EVIDENCE"
        if row["canon_compliance"]:
            canon += f" / {row['canon_compliance']}"
        verdict = f"{row['qc_verdict']}: {row['qc_reason']}"
        body.append(
            "| "
            + " | ".join(
                _md(x)
                for x in (
                    row["issue"],
                    request_label,
                    plan,
                    row["planned_due"] or "Not stated",
                    row["actual_delivery_timestamp"] or "NEEDS_EVIDENCE",
                    completed,
                    reviewed,
                    canon,
                    verdict,
                )
            )
            + " |"
        )
    return (
        "# XOS QC Register — Native Paperclip Evidence Projection\n\n"
        "This register is generated from Paperclip native evidence. Missing facts are "
        "reported as missing; the generator never converts status, model output, or a "
        "successful process exit into completion or independent review by itself.\n\n"
        + header
        + "\n".join(body)
        + "\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--company-id", required=True)
    parser.add_argument("--issue", action="append", required=True, dest="issues")
    parser.add_argument("--supplement")
    parser.add_argument("--json-output")
    parser.add_argument("--markdown-output")
    args = parser.parse_args()

    cli = PaperclipCLI(args.company_id)
    supplements = load_supplement(args.supplement)
    names = cli.agent_names()
    rows = [
        build_row(cli.bundle(identifier), names, supplements.get(identifier, {}))
        for identifier in args.issues
    ]

    json_text = json.dumps(rows, indent=2, sort_keys=True) + "\n"
    markdown_text = render_markdown(rows)

    if args.json_output:
        Path(args.json_output).write_text(json_text, encoding="utf-8")
    else:
        sys.stdout.write(json_text)

    if args.markdown_output:
        Path(args.markdown_output).write_text(markdown_text, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
