#!/bin/zsh
set -euo pipefail
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
ROOT="/Users/reginaldberry/XOS-GitHub/xlr8ros-hq"
if [[ ! -f "$ROOT/scripts/sync_canon_mirrors.py" ]]; then
  echo "BLOCKED: missing HQ checkout at $ROOT" >&2
  exit 2
fi
cd "$ROOT"
if [[ -n "$(git status --porcelain -- canon)" ]]; then
  echo "BLOCKED: local canon has uncommitted modifications; will not overwrite" >&2
  exit 3
fi
git pull --ff-only origin main
# Use existing git credential access on the Mac; never embed secrets in launchd plist.
TOKEN="$(security find-generic-password -s xos-canon-sync-token -w 2>/dev/null || true)"
if [[ -z "$TOKEN" ]]; then
  echo "BLOCKED: xos-canon-sync-token not found in login Keychain" >&2
  exit 4
fi
export XOS_CANON_SYNC_TOKEN="$TOKEN"
unset TOKEN
python3 -c 'import yaml' || { echo "BLOCKED: PyYAML required for python3" >&2; exit 5; }
python3 scripts/sync_canon_mirrors.py
