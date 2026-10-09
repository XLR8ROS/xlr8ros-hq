#!/usr/bin/env python3
"""Render XOS HQ Canon and synchronize declared downstream Markdown mirrors.

Uses Python standard library only. No downstream YAML is created.
Set XOS_CANON_SYNC_TOKEN for downstream GitHub writes.
"""
import base64
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "canon" / "synchronization.yaml"


def parse_manifest(text):
    entries = []
    current = None
    downstream = False
    for line in text.splitlines():
        if re.match(r"^  [a-z0-9-]+:$", line):
            current = {"name": line.strip()[:-1], "downstream": []}
            entries.append(current)
            downstream = False
        elif current and line.startswith("    source: "):
            current["source"] = line.split(": ", 1)[1]
        elif current and line.startswith("    hq_markdown: "):
            current["hq_markdown"] = line.split(": ", 1)[1]
        elif current and line == "    downstream:":
            downstream = True
        elif current and downstream and line.startswith("      - repository: "):
            current["downstream"].append({"repo": line.split(": ", 1)[1]})
        elif current and downstream and line.startswith("        path: "):
            current["downstream"][-1]["path"] = line.split(": ", 1)[1]
    return entries


def render_literal(source):
    text = source.read_text(encoding="utf-8")
    if not re.search(r"^source_of_truth: true$", text, re.M):
        raise ValueError(f"Not an authoritative Canon: {source}")
    if not re.search(r"^  mode: literal$", text, re.M):
        raise ValueError(f"Unsupported YAML rendering mode: {source}")
    marker = "content: |\n"
    if text.count(marker) != 1:
        raise ValueError(f"Expected one literal content block: {source}")
    lines = text.split(marker, 1)[1].splitlines(keepends=True)
    if any(line.strip() and not line.startswith("  ") for line in lines):
        raise ValueError(f"Invalid YAML content indentation: {source}")
    return "".join(line[2:] if line.startswith("  ") else line for line in lines)


def api(repo, path, token, method="GET", payload=None):
    encoded = urllib.parse.quote(path, safe="/")
    url = f"https://api.github.com/repos/{repo}/contents/{encoded}"
    data = json.dumps(payload).encode() if payload is not None else None
    request = urllib.request.Request(url, data=data, method=method, headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "xos-canon-sync",
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404 and method == "GET":
            return None
        raise RuntimeError(f"GitHub {method} {repo}/{path}: HTTP {error.code}") from error


def sync_target(repo, path, content, token):
    old = api(repo, path, token)
    if old is not None and old.get("type") != "file":
        raise ValueError(f"Target is not a file: {repo}/{path}")
    if old is not None:
        existing = base64.b64decode(old["content"]).decode("utf-8")
        if existing == content:
            print(f"UNCHANGED {repo}/{path}")
            return
    payload = {
        "message": f"canon: synchronize {path} from XOS HQ YAML",
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
    }
    if old is not None:
        payload["sha"] = old["sha"]
    api(repo, path, token, method="PUT", payload=payload)
    print(f"SYNCED {repo}/{path}")


def main():
    entries = parse_manifest(MANIFEST.read_text(encoding="utf-8"))
    token = os.environ.get("XOS_CANON_SYNC_TOKEN")
    errors = []
    for item in entries:
        source = ROOT / item["source"]
        if not source.is_file():
            raise FileNotFoundError(source)
        content = render_literal(source)
        target = ROOT / item["hq_markdown"]
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_text(encoding="utf-8") != content:
            target.write_text(content, encoding="utf-8")
            print(f"RENDERED {target.relative_to(ROOT)}")
        for dest in item["downstream"]:
            if not token:
                print(f"PENDING TOKEN {dest['repo']}/{dest['path']}")
                continue
            try:
                sync_target(dest["repo"], dest["path"], content, token)
            except Exception as exc:
                errors.append(f"{dest['repo']}/{dest['path']}: {exc}")
    if errors:
        raise SystemExit("\n".join(errors))
    if not token:
        print("HQ rendered; downstream synchronization requires XOS_CANON_SYNC_TOKEN")


if __name__ == "__main__":
    main()
