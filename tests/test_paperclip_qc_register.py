"""Offline tests for the native-evidence XOS QC register projection."""
import importlib.util
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "scripts" / "paperclip_qc_register.py"
spec = importlib.util.spec_from_file_location("paperclip_qc_register", SOURCE)
qc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qc)


class QCRegisterTests(unittest.TestCase):
    def issue(self, **overrides):
        value = {
            "identifier": "XOS-1",
            "title": "Example",
            "status": "done",
            "description": "Do the work.",
            "createdAt": "2026-10-01T00:00:00Z",
            "completedAt": "2026-10-01T01:00:00Z",
            "executionRunId": None,
            "workProducts": [],
        }
        value.update(overrides)
        return value

    def bundle(self, *, issue=None, comments=None, interactions=None, runs=None):
        return {
            "issue": issue or self.issue(),
            "comments": comments or [],
            "interactions": interactions or [],
            "runs": runs or [],
        }

    def test_plan_approval_is_not_completion_review(self):
        interaction = {
            "id": "plan-review",
            "status": "accepted",
            "resolvedAt": "2026-10-01T00:30:00Z",
            "resolvedByUserId": "reg",
            "payload": {
                "prompt": "Do you approve the plan?",
                "target": {"type": "issue_document", "key": "plan", "revisionId": "rev-1"},
            },
            "result": {"outcome": "accepted"},
        }
        row = qc.build_row(self.bundle(interactions=[interaction]), {}, {})
        self.assertEqual(row["plan_revision"], "rev-1")
        self.assertEqual(row["reviewed_by"], "")
        self.assertEqual(row["qc_verdict"], "NEEDS_EVIDENCE")

    def test_latest_successful_run_is_completed_by(self):
        runs = [
            {"runId": "r1", "agentId": "a1", "status": "succeeded",
             "finishedAt": "2026-10-01T00:30:00Z"},
            {"runId": "r2", "agentId": "a2", "status": "succeeded",
             "finishedAt": "2026-10-01T00:40:00Z"},
            {"runId": "r3", "agentId": "a3", "status": "failed",
             "finishedAt": "2026-10-01T00:50:00Z"},
        ]
        row = qc.build_row(self.bundle(runs=runs), {"a1": "One", "a2": "Two"}, {})
        self.assertEqual(row["completed_by"], "Two")
        self.assertEqual(row["completed_by_run_id"], "r2")

    def test_self_review_is_fail_return(self):
        runs = [{"runId": "r1", "agentId": "a1", "status": "succeeded",
                 "finishedAt": "2026-10-01T00:30:00Z"}]
        review = {
            "id": "review-1",
            "status": "accepted",
            "resolvedAt": "2026-10-01T00:45:00Z",
            "resolvedByAgentId": "a1",
            "resolvedByRunId": "rr1",
            "payload": {"prompt": "Approve final QC review?"},
            "result": {"outcome": "accepted"},
        }
        row = qc.build_row(self.bundle(runs=runs, interactions=[review]), {"a1": "Same"}, {})
        self.assertEqual(row["qc_verdict"], "FAIL_RETURN")
        self.assertFalse(row["independent_review"])

    def test_pending_human_only_interaction_is_human_blocker(self):
        pending = {
            "id": "h1",
            "status": "pending",
            "effectiveResolverPolicy": "human_only",
            "createdAt": "2026-10-01T00:40:00Z",
            "payload": {"prompt": "Reg must decide."},
        }
        row = qc.build_row(self.bundle(interactions=[pending]), {}, {})
        self.assertEqual(row["qc_verdict"], "HUMAN_BLOCKER")
        self.assertIn("h1", row["qc_reason"])

    def test_explicit_supplement_supplies_missing_non_native_evidence(self):
        supplement = {
            "reg_request": "Exact request",
            "reg_request_timestamp": "2026-10-01T00:00:00Z",
            "reg_request_verbatim_verified": True,
            "canon_revision": "hq@abc123",
            "canon_compliance": "PASS",
            "qc_verdict": "PASS",
            "completed_by": "IGNORED",
            "reviewed_by": "IGNORED",
        }
        row = qc.build_row(self.bundle(), {}, supplement)
        self.assertEqual(row["reg_request"], "Exact request")
        self.assertTrue(row["reg_request_verbatim_verified"])
        self.assertEqual(row["canon_revision"], "hq@abc123")
        self.assertEqual(row["qc_verdict"], "PASS")
        self.assertEqual(row["completed_by"], "")
        self.assertEqual(row["reviewed_by"], "")

    def test_markdown_escapes_pipe_and_newline(self):
        row = qc.build_row(
            self.bundle(),
            {},
            {"reg_request": "a|b\nc", "reg_request_verbatim_verified": True},
        )
        rendered = qc.render_markdown([row])
        self.assertIn("a\\|b<br>c", rendered)

    def test_operator_or_description_is_not_claimed_as_reg_verbatim(self):
        comments = [{
            "id": "c1",
            "authorUserId": "local-board",
            "createdAt": "2026-10-01T00:01:00Z",
            "body": "Operator text",
        }]
        row = qc.build_row(self.bundle(comments=comments), {}, {})
        self.assertFalse(row["reg_request_verbatim_verified"])
        self.assertEqual(row["reg_request_source"], "issue_description")

    def test_explicit_qc_verdict_can_come_from_review_result(self):
        runs = [{"runId": "r1", "agentId": "a1", "status": "succeeded",
                 "finishedAt": "2026-10-01T00:30:00Z"}]
        review = {
            "id": "review-2",
            "status": "accepted",
            "resolvedAt": "2026-10-01T00:45:00Z",
            "resolvedByAgentId": "a2",
            "payload": {"prompt": "Independent QC review"},
            "result": {"outcome": "accepted", "qcVerdict": "PASS"},
        }
        row = qc.build_row(
            self.bundle(runs=runs, interactions=[review]),
            {"a1": "Builder", "a2": "Reviewer"},
            {},
        )
        self.assertEqual(row["qc_verdict"], "PASS")
        self.assertTrue(row["independent_review"])


if __name__ == "__main__":
    unittest.main()
