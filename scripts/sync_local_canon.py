#!/usr/bin/env python3
"""Mirror authoritative HQ YAML into local checkout copies; no network or token."""
from pathlib import Path
import sys
import os
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from render_canon import parse_manifest, render_literal

CHECKOUTS = Path("/Users/reginaldberry/XOS-GitHub")
MANIFEST = ROOT / "canon/synchronization.yaml"

def local_repo(repository):
    if repository == "XLR8ROS/xlr8ros-hq":
        return ROOT
    owner, name = repository.split("/", 1)
    return CHECKOUTS / owner / name

def update(path, data):
    if path.exists() and path.read_bytes() == data:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=".canon-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.chmod(temp_name, 0o644)
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
    return True

def main():
    changed = 0
    for item in parse_manifest(MANIFEST.read_text(encoding="utf-8")):
        data = render_literal(ROOT / item["source"]).encode("utf-8")
        destinations = [("XLR8ROS/xlr8ros-hq", item["hq_markdown"])]
        destinations += [(t["repo"], t["path"]) for t in item["downstream"]]
        for repo, relative in destinations:
            checkout = local_repo(repo)
            if not checkout.is_dir():
                print("MISSING_CHECKOUT", repo, file=sys.stderr)
                continue
            target = checkout / relative
            if update(target, data):
                print("UPDATED", repo, relative)
                changed += 1
    print("LOCAL_CANON_SYNC_COMPLETE changes=" + str(changed))

if __name__ == "__main__":
    main()
