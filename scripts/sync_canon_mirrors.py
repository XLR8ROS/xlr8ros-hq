#!/usr/bin/env python3
"""XOS canonical YAML -> readable Markdown -> registered GitHub mirrors.

This is the single automatic sync engine for HQ and registered division canon.
It runs centrally from HQ, never from an agent Core. Changes are idempotent,
verified by read-back, and errors are aggregated so one missing repo cannot
silently prevent healthy destinations from updating.

Examples:
  python3 scripts/sync_canon_mirrors.py --validate
  XOS_CANON_SYNC_TOKEN=... python3 scripts/sync_canon_mirrors.py --check
  XOS_CANON_SYNC_TOKEN=... python3 scripts/sync_canon_mirrors.py
"""
import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "canon" / "synchronization.yaml"
HQ = "XLR8ROS/xlr8ros-hq"
API = "https://api.github.com"
TOKEN = os.environ.get("XOS_CANON_SYNC_TOKEN", "")
VALID_REPO = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")
SEAD_COMMENT = (
    "<!-- Generated readable copy. Authoritative YAML: "
    "{repo}/{source}. Do not edit independently. -->\n\n"
)


def validate_repo(repo):
    if not isinstance(repo, str) or not VALID_REPO.fullmatch(repo):
        raise ValueError("Invalid registered GitHub repository name")
    return repo


def validate_path(path):
    if not isinstance(path, str) or not path or "\\" in path:
        raise ValueError("Invalid registered file path")
    posix = PurePosixPath(path)
    if posix.is_absolute() or ".." in posix.parts or "." in posix.parts:
        raise ValueError("Unsafe registered file path")
    if posix.as_posix() != path:
        raise ValueError("Noncanonical registered file path")
    return path


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def github_api(repo, path, method="GET", payload=None):
    """GitHub Contents API, authenticated only through preapproved sync token."""
    validate_repo(repo)
    validate_path(path)
    url = API + "/repos/" + repo + "/contents/" + "/".join(
        urllib.parse.quote(part, safe="") for part in path.split("/")
    )
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "xos-canon-sync",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        if method == "GET" and exc.code == 404:
            return None
        # Deliberately avoid dumping request/response body or credentials.
        raise RuntimeError(f"{method} {repo}/{path}: HTTP {exc.code}") from exc


def remote_bytes(repo, path):
    obj = github_api(repo, path)
    if obj is None:
        return None, None
    if obj.get("type") != "file" or obj.get("encoding") != "base64":
        raise RuntimeError(f"Non-file or unsupported encoding: {repo}/{path}")
    try:
        data = base64.b64decode(obj["content"], validate=False)
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"Cannot decode file: {repo}/{path}") from exc
    if obj.get("size") != len(data):
        raise RuntimeError(f"Wrong remote file length: {repo}/{path}")
    return data, obj["sha"]


def rendered_content(source_repo, source, text, render_path, header_style):
    doc = yaml.safe_load(text)
    if not isinstance(doc, dict):
        raise ValueError(f"Invalid source document: {source_repo}/{source}")
    if doc.get("status") != "authoritative" or doc.get("source_of_truth") is not True:
        raise ValueError(f"Not approved authoritative canon: {source_repo}/{source}")
    if doc.get("render", {}).get("mode") != "literal":
        raise ValueError(f"Not a literal-render canon: {source_repo}/{source}")
    if doc["render"].get("markdown_path") != render_path:
        raise ValueError(f"Source/render destination disagreement: {source}")
    content = doc.get("content")
    if not isinstance(content, str):
        raise ValueError(f"No literal text content: {source}")
    if header_style == "none":
        prefix = ""
    elif header_style == "sead-generated" and source_repo == "XLR8ROS/XLR8ROS_SEAD":
        prefix = SEAD_COMMENT.format(repo=source_repo, source=source)
    else:
        raise ValueError(f"Unsupported render header style: {header_style}")
    return (prefix + content).encode("utf-8")


def load_registry(path=REGISTRY):
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise ValueError("Registry is not a mapping")
    if doc.get("schema") != "xos.canon-synchronization/v1":
        raise ValueError("Unknown synchronization registry schema")
    if doc.get("canonical_repository") != HQ:
        raise ValueError("Unrecognized authoritative HQ")
    artifacts = doc.get("artifacts")
    if not isinstance(artifacts, dict) or not artifacts:
        raise ValueError("No registered canonical artifacts")
    destination_sources = {}
    output = []
    for name, item in artifacts.items():
        if not isinstance(item, dict):
            raise ValueError(f"Invalid artifact record {name}")
        source_repo = validate_repo(item.get("source_repository", HQ))
        source = validate_path(item["source"])
        if not source.startswith("canon/") or not source.endswith(".yaml"):
            raise ValueError(f"Source must be authoritative canon YAML: {name}")
        render_path = validate_path(item.get("source_markdown", item.get("hq_markdown", "")))
        header_style = item.get("header_style", "none")
        if header_style not in ("none", "sead-generated"):
            raise ValueError(f"Invalid header style: {name}")
        downstream = item.get("downstream", [])
        if not isinstance(downstream, list):
            raise ValueError(f"Invalid downstream list: {name}")
        destinations = [(source_repo, render_path)]
        destinations += [
            (validate_repo(t["repository"]), validate_path(t["path"]))
            for t in downstream
        ]
        if len(set(destinations)) != len(destinations):
            raise ValueError(f"Duplicate mirror in {name}")
        source_identity = (source_repo, source, render_path, header_style)
        for dest in destinations:
            if dest in destination_sources and destination_sources[dest] != source_identity:
                raise ValueError(f"Conflicting canon mirror owners: {dest}")
            destination_sources[dest] = source_identity
        output.append((name, source_identity, destinations))
    return output


def ensure(repo, path, desired, check_only):
    old, sha = remote_bytes(repo, path)
    if old == desired:
        print(f"MATCH {repo}/{path} SHA256={sha256(desired)}", flush=True)
        return "match"
    if check_only:
        print(f"DRIFT {repo}/{path}", flush=True)
        return "drift"
    payload = {
        "message": "canon: auto-sync from authoritative XOS YAML",
        "content": base64.b64encode(desired).decode("ascii"),
        "branch": "main",
    }
    if sha is not None:
        payload["sha"] = sha
    github_api(repo, path, method="PUT", payload=payload)
    again, _ = remote_bytes(repo, path)
    if again != desired:
        raise RuntimeError(f"Post-write read-back mismatch: {repo}/{path}")
    print(f"VERIFIED {repo}/{path} SHA256={sha256(desired)}", flush=True)
    return "verified"


def synchronize(mode="sync"):
    entries = load_registry()
    if mode != "validate" and not TOKEN:
        raise RuntimeError("XOS_CANON_SYNC_TOKEN not configured; no unauthenticated fallback")
    statuses = {"match": 0, "verified": 0, "drift": 0}
    errors = []
    source_count = 0
    for name, (source_repo, source, render_path, header_style), targets in entries:
        try:
            if source_repo == HQ:
                file = (ROOT / source).resolve()
                if not file.is_relative_to((ROOT / "canon").resolve()):
                    raise ValueError("HQ source escaped canon directory")
                text = file.read_text(encoding="utf-8")
            elif mode == "validate":
                print(f"EXTERNAL_SOURCE_REGISTERED {source_repo}/{source}", flush=True)
                continue
            else:
                blob, _ = remote_bytes(source_repo, source)
                if blob is None:
                    raise RuntimeError(f"Missing or inaccessible authoritative YAML: {source_repo}/{source}")
                text = blob.decode("utf-8")
            # Proposed canonical sources must not write to any downstream destination
            # before an authorized approval and source-of-truth promotion.
            metadata = yaml.safe_load(text)
            if isinstance(metadata, dict) and metadata.get("status") == "proposed_reg_review" and metadata.get("source_of_truth") is False:
                print(f"PENDING_REG_APPROVAL {name} {source_repo}/{source}", flush=True)
                continue
            rendered = rendered_content(source_repo, source, text, render_path, header_style)
            source_count += 1
            if mode == "validate":
                if source_repo != HQ:
                    continue
                local = (ROOT / render_path).read_bytes()
                if local != rendered:
                    raise RuntimeError(f"Local HQ rendering differs from source: {render_path}")
                print(f"VALID {name} {source_repo}/{render_path}", flush=True)
                continue
            for repo, path in targets:
                try:
                    status = ensure(repo, path, rendered, check_only=mode == "check")
                    statuses[status] += 1
                except Exception as exc:
                    msg = f"{name} -> {repo}/{path}: {type(exc).__name__}: {exc}"
                    errors.append(msg)
                    print("ERROR " + msg, file=sys.stderr, flush=True)
        except Exception as exc:
            msg = f"{name}: {type(exc).__name__}: {exc}"
            errors.append(msg)
            print("ERROR " + msg, file=sys.stderr, flush=True)
    print(
        f"SYNC_SUMMARY sources={source_count}/{len(entries)} "
        + " ".join(f"{k}={v}" for k, v in statuses.items())
        + f" errors={len(errors)}",
        flush=True,
    )
    if errors or statuses["drift"]:
        return 1
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="Read-only mirror drift audit")
    group.add_argument("--validate", action="store_true", help="Validate registry and local HQ render without network")
    args = parser.parse_args()
    mode = "validate" if args.validate else ("check" if args.check else "sync")
    try:
        sys.exit(synchronize(mode))
    except (ValueError, RuntimeError, OSError, yaml.YAMLError) as exc:
        print(f"SYNC_FAILED {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
