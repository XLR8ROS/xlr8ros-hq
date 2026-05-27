# MNFST / Manifest HOW-TO Hub

Purpose: central operating hub for local MNFST / Manifest setup, dashboard access, Docker/runtime management, update procedure, troubleshooting, and XOS integration notes.

## Hub Sections

- `docs/` — pulled public documentation and reference pages
- `repo/` — upstream repo snapshot/reference notes
- `schemas/` — config/schema/reference material if found
- `notes/` — local XOS notes and findings
- `scripts/` — helper scripts generated for this hub

## Local XOS Known Context

- Manifest/MNFST runs locally.
- Docker stack includes Manifest and Postgres.
- Dashboard/runtime ports must be verified from the local container config before updates.
- OpenClaw is local Node-based gateway and should not be confused with Docker Manifest.
- Update work should identify image, ports, env, mounts, and labels before recreating containers.
