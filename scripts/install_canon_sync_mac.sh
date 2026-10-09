#!/bin/zsh
set -euo pipefail
ROOT="/Users/reginaldberry/XOS-GitHub/xlr8ros-hq"
SOURCE="$ROOT/launchd/com.xos.canon-sync.plist"
DEST="$HOME/Library/LaunchAgents/com.xos.canon-sync.plist"
[[ -f "$SOURCE" ]] || { echo "BLOCKED: missing $SOURCE" >&2; exit 2; }
[[ -f "$ROOT/scripts/run_canon_sync_mac.sh" ]] || { echo "BLOCKED: missing runner" >&2; exit 2; }
command -v gh >/dev/null || { echo "BLOCKED: GitHub CLI is required" >&2; exit 3; }
gh auth status || { echo "BLOCKED: GitHub CLI authentication required" >&2; exit 4; }
python3 -c 'import yaml' || { echo "BLOCKED: PyYAML missing; python3 -m pip install PyYAML" >&2; exit 5; }
security find-generic-password -s xos-canon-sync-token -w >/dev/null 2>&1 || { echo "BLOCKED: missing xos-canon-sync-token in login Keychain" >&2; exit 6; }
mkdir -p "$HOME/Library/LaunchAgents" "$HOME/Library/Logs"
cp "$SOURCE" "$DEST"
/usr/bin/plutil -lint "$DEST"
launchctl bootout "gui/$(id -u)/com.xos.canon-sync" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$DEST"
launchctl kickstart -k "gui/$(id -u)/com.xos.canon-sync"
launchctl print "gui/$(id -u)/com.xos.canon-sync"
echo "Installed and started com.xos.canon-sync"
