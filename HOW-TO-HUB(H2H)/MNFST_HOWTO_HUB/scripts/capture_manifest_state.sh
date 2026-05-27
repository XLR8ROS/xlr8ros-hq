#!/usr/bin/env zsh
set -euo pipefail

OUT="manifest-state-$(date +%Y%m%d-%H%M%S).txt"

{
  echo "# Manifest State Capture"
  echo "Generated: $(date)"
  echo

  echo "## Docker Containers"
  docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}\t{{.Image}}" | grep -Ei "manifest|mnfst|postgres" || true
  echo

  echo "## manifest-1 Inspect"
  docker inspect manifest-1 --format 'IMAGE={{.Config.Image}}
PORTS={{json .HostConfig.PortBindings}}
MOUNTS={{json .Mounts}}
ENV={{json .Config.Env}}
LABELS={{json .Config.Labels}}' 2>/dev/null || true
  echo

  echo "## Listening Ports"
  lsof -nP -iTCP -sTCP:LISTEN | grep -Ei "2099|manifest|mnfst|openclaw|node|docker|postgres" || true
  echo

  echo "## manifest-1 Logs"
  docker logs manifest-1 --tail 120 2>/dev/null || true
} | tee "$OUT"

echo
echo "Wrote: $OUT"
