#!/usr/bin/env python3
"""Synchronize registered readable canon mirrors from their authoritative YAML.

Run in HQ GitHub Actions. The synchronization registry is the only target list.
No local agent-specific edits are allowed; failures exit nonzero.
"""
import base64
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "canon/synchronization.yaml"
REPO = "XLR8ROS/xlr8ros-hq"
TOKEN = os.getenv("XOS_CANON_SYNC_TOKEN") or os.getenv("GITHUB_TOKEN")
DRY_RUN = "--check" in sys.argv
HEADER_TEMPLATE = "<!-- Generated readable copy. Canonical YAML: {repo}/{source}. Do not edit independently. -->\n\n"

def api(repo, path, method="GET", body=None):
    if not TOKEN:
        raise RuntimeError("No GitHub token supplied")
    url = "https://api.github.com/repos/" + repo + "/contents/" + "/".join(
        urllib.parse.quote(p, safe="") for p in path.split("/")
    )
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": "Bearer " + TOKEN,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "xos-canon-synchronizer",
    })
    try:
        with urllib.request.urlopen(request, timeout=25) as result:
            return json.load(result)
    except urllib.error.HTTPError as exc:
        if exc.code == 404 and method == "GET":
            return None
        raise RuntimeError(f"GitHub {method} {repo}/{path}: HTTP {exc.code} {exc.read().decode()[:300]}") from exc

def ensure(repo, path, content):
    existing = api(repo, path)
    desired = content.encode("utf-8")
    if existing is not None:
        if existing.get("type") != "file":
            raise RuntimeError(f"Target not a file: {repo}/{path}")
        old = base64.b64decode(existing["content"])
        if old == desired:
            print("MATCH", repo, path)
            return
    if DRY_RUN:
        raise RuntimeError(f"DRIFT {repo}/{path}")
    payload = {
        "message": "canon: synchronize registered mirror from authoritative YAML",
        "content": base64.b64encode(desired).decode("ascii"),
        "branch": "main",
    }
    if existing:
        payload["sha"] = existing["sha"]
    api(repo, path, "PUT", payload)
    check = api(repo, path)
    if base64.b64decode(check["content"]) != desired:
        raise RuntimeError(f"Post-write mismatch: {repo}/{path}")
    print("VERIFIED", repo, path)

def main():
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    if registry.get("canonical_repository") != REPO:
        raise RuntimeError("Unexpected canonical repository")
    for item in registry["artifacts"].values():
        source = item["source"]
        source_path = ROOT / source
        if not source_path.is_file() or not source_path.resolve().is_relative_to((ROOT / "canon").resolve()):
            raise RuntimeError(f"Unrecognized source: {source}")
        document = yaml.safe_load(source_path.read_text(encoding="utf-8"))
        if document.get("source_of_truth") is not True or document.get("render", {}).get("mode") != "literal":
            raise RuntimeError(f"Invalid authoritative source: {source}")
        body = document.get("content")
        if not isinstance(body, str):
            raise RuntimeError(f"Missing literal content: {source}")
        hq_path = item["hq_markdown"]
        if document["render"]["markdown_path"] != hq_path:
            raise RuntimeError(f"Render destination conflicts with registry: {source}")
        header = HEADER_TEMPLATE.format(repo=REPO, source=source)
        rendered = header + body
        ensure(REPO, hq_path, rendered)
        for target in item.get("downstream", []):
            ensure(target["repository"], target["path"], rendered)
    print("ALL REGISTERED CANON MIRRORS VERIFIED")

if __name__ == "__main__":
    main()
