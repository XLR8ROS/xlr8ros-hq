# Local MNFST / Manifest Stack Checklist

## Identify Current Container

Run:

docker inspect manifest-1 --format 'IMAGE={{.Config.Image}}
PORTS={{json .HostConfig.PortBindings}}
MOUNTS={{json .Mounts}}
ENV={{json .Config.Env}}
LABELS={{json .Config.Labels}}'

## Check Port Usage

Run:

lsof -nP -iTCP -sTCP:LISTEN | grep -Ei "2099|manifest|openclaw|node|docker"

## Check Manifest Logs

Run:

docker logs manifest-1 --tail 120

## Check Postgres

Run:

docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -Ei "manifest|postgres"

## Update Rule

Do not update by guessing.

First capture:

- current image
- current ports
- current mounts
- current env
- current labels
- current container logs
- whether Postgres volume/data is healthy
