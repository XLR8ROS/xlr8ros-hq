# MNFST / Manifest Troubleshooting

## Dashboard Cannot Be Reached

Check:

- Is `manifest-1` running?
- Is Postgres running?
- Which port is mapped?
- Is the mapped host port occupied?
- What do Manifest logs say?

## Container Will Not Start

Check:

- port conflict
- missing env
- Postgres unavailable
- stale image
- Docker update changed networking/startup behavior
- volume/mount path issue

## Browser Shows Old Dashboard / 404

Check:

- old bookmark
- wrong localhost port
- old remote dashboard URL
- stale browser tab
- container not running
