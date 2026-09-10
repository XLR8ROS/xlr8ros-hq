#!/usr/bin/env python3
"""Synchronize selected repository Markdown files into an OpenAI Vector Store."""
from __future__ import annotations

import fnmatch
import hashlib
import json
import mimetypes
import os
import pathlib
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid

API_KEY = os.environ.get("OPENAI_API_KEY", "").strip()
STORE_NAME = os.environ.get("XOS_VECTOR_STORE_NAME", "").strip()
SCOPE = os.environ.get("XOS_VECTOR_SCOPE", "").strip()
VISIBILITY = os.environ.get("XOS_VECTOR_VISIBILITY", "").strip()
REPOSITORY = os.environ.get("XOS_REPOSITORY", os.environ.get("GITHUB_REPOSITORY", "")).strip()
BASE_URL = os.environ.get("XOS_OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
INCLUDES = [x for x in os.environ.get("XOS_INCLUDE_GLOBS", "**/*.md;*.md").split(";") if x]
EXCLUDES = [x for x in os.environ.get("XOS_EXCLUDE_GLOBS", "").split(";") if x]


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(1)


for key, value in {
    "OPENAI_API_KEY": API_KEY,
    "XOS_VECTOR_STORE_NAME": STORE_NAME,
    "XOS_VECTOR_SCOPE": SCOPE,
    "XOS_VECTOR_VISIBILITY": VISIBILITY,
    "XOS_REPOSITORY": REPOSITORY,
}.items():
    if not value:
        fail(f"Missing required environment variable: {key}")


def request(method: str, path: str, body: bytes | None = None, content_type: str = "application/json"):
    req = urllib.request.Request(BASE_URL + path, data=body, method=method)
    req.add_header("Authorization", f"Bearer {API_KEY}")
    if body is not None:
        req.add_header("Content-Type", content_type)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read()
            return json.loads(raw.decode("utf-8")) if raw else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        fail(f"OpenAI API {method} {path} returned {exc.code}: {detail}")


def json_request(method: str, path: str, payload: dict | None = None):
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    return request(method, path, body)


def list_all(path: str):
    items = []
    after = None
    while True:
        sep = "&" if "?" in path else "?"
        url = f"{path}{sep}limit=100"
        if after:
            url += "&after=" + urllib.parse.quote(after)
        page = json_request("GET", url)
        data = page.get("data", [])
        items.extend(data)
        if not page.get("has_more") or not data:
            return items
        after = page.get("last_id") or data[-1].get("id")


def get_or_create_store() -> dict:
    exact = [s for s in list_all("/vector_stores") if s.get("name") == STORE_NAME]
    if len(exact) > 1:
        fail(f"More than one vector store is named {STORE_NAME!r}; refusing to guess")
    if exact:
        store = exact[0]
        print(f"Using vector store {store['id']} ({STORE_NAME})")
        return store
    store = json_request("POST", "/vector_stores", {"name": STORE_NAME})
    print(f"Created vector store {store['id']} ({STORE_NAME})")
    return store


def matches(path: str) -> bool:
    return any(fnmatch.fnmatch(path, pat) for pat in INCLUDES) and not any(fnmatch.fnmatch(path, pat) for pat in EXCLUDES)


def git_blob_sha(path: pathlib.Path) -> str:
    try:
        return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()
    except Exception:
        data = path.read_bytes()
        return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def discover_files() -> dict[str, tuple[pathlib.Path, str]]:
    found = {}
    for p in pathlib.Path(".").rglob("*"):
        if not p.is_file():
            continue
        rel = p.as_posix().removeprefix("./")
        if rel.startswith(".git/") or not matches(rel):
            continue
        found[rel] = (p, git_blob_sha(p))
    return dict(sorted(found.items()))


def multipart_upload(path: pathlib.Path) -> dict:
    boundary = "----xos" + uuid.uuid4().hex
    filename = path.name
    mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    parts = [f"--{boundary}\r\nContent-Disposition: form-data; name=\"purpose\"\r\n\r\nassistants\r\n".encode()]
    parts.append(f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{filename}\"\r\nContent-Type: {mime}\r\n\r\n".encode() + path.read_bytes() + b"\r\n")
    parts.append(f"--{boundary}--\r\n".encode())
    return request("POST", "/files", b"".join(parts), f"multipart/form-data; boundary={boundary}")


def wait_ready(store_id: str, file_id: str, timeout_seconds: int = 600) -> dict:
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        obj = json_request("GET", f"/vector_stores/{store_id}/files/{file_id}")
        status = obj.get("status")
        if status == "completed":
            return obj
        if status in {"failed", "cancelled"}:
            fail(f"Indexing {file_id} ended with status={status}: {obj.get('last_error')}")
        time.sleep(2)
    fail(f"Timed out waiting for vector-store file {file_id}")


def attach(store_id: str, uploaded_file_id: str, rel: str, sha: str) -> dict:
    attributes = {
        "repo": REPOSITORY,
        "path": rel[:512],
        "blob_sha": sha,
        "scope": SCOPE[:512],
        "visibility": VISIBILITY[:512],
        "source_ref": os.environ.get("GITHUB_SHA", "")[:512],
    }
    obj = json_request("POST", f"/vector_stores/{store_id}/files", {
        "file_id": uploaded_file_id,
        "attributes": attributes,
        "chunking_strategy": {"type": "auto"},
    })
    return wait_ready(store_id, obj["id"])


def detach_and_delete(store_id: str, file_id: str) -> None:
    json_request("DELETE", f"/vector_stores/{store_id}/files/{file_id}")
    json_request("DELETE", f"/files/{file_id}")


def main() -> None:
    store = get_or_create_store()
    store_id = store["id"]
    local = discover_files()
    print(f"Discovered {len(local)} source files for {REPOSITORY}")

    remote_all = list_all(f"/vector_stores/{store_id}/files")
    remote = {}
    for obj in remote_all:
        attrs = obj.get("attributes") or {}
        if attrs.get("repo") == REPOSITORY and attrs.get("path"):
            remote.setdefault(attrs["path"], []).append(obj)

    added = updated = removed = unchanged = 0
    for rel, (path, sha) in local.items():
        candidates = remote.get(rel, [])
        current = next((x for x in candidates if (x.get("attributes") or {}).get("blob_sha") == sha and x.get("status") == "completed"), None)
        if current:
            unchanged += 1
            for old in candidates:
                if old.get("id") != current.get("id"):
                    detach_and_delete(store_id, old["id"])
                    removed += 1
            continue

        upload = multipart_upload(path)
        attach(store_id, upload["id"], rel, sha)
        if candidates:
            updated += 1
            for old in candidates:
                detach_and_delete(store_id, old["id"])
                removed += 1
        else:
            added += 1
        print(f"Indexed {rel}")

    for rel, candidates in remote.items():
        if rel in local:
            continue
        for old in candidates:
            detach_and_delete(store_id, old["id"])
            removed += 1
        print(f"Removed stale source {rel}")

    final = [x for x in list_all(f"/vector_stores/{store_id}/files") if (x.get("attributes") or {}).get("repo") == REPOSITORY]
    failed = [x for x in final if x.get("status") != "completed"]
    summary = {
        "vector_store_id": store_id,
        "vector_store_name": STORE_NAME,
        "repository": REPOSITORY,
        "source_files": len(local),
        "indexed_for_repo": len(final),
        "added": added,
        "updated": updated,
        "removed": removed,
        "unchanged": unchanged,
        "non_completed": len(failed),
    }
    print(json.dumps(summary, indent=2))
    if failed or len(final) != len(local):
        fail("Post-sync verification failed")


if __name__ == "__main__":
    main()
