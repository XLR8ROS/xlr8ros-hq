# MNFST / Manifest Update Procedure Draft

## Principle

Manifest updates must preserve local data and runtime config.

## Before Update

Capture:

- image
- ports
- mounts
- env
- labels
- logs
- Postgres status

## Update Shape

If using Docker image:

1. Pull newer image.
2. Stop old Manifest container.
3. Recreate Manifest container with same env/mounts and corrected host port.
4. Keep Postgres/data volume intact.
5. Start Manifest.
6. Verify dashboard.
7. Verify model/provider config.
8. Verify OpenClaw integration if applicable.

## Never Do Blindly

- delete Postgres volume
- delete Manifest data volume
- recreate container without saving env/mounts
- kill unknown port processes without identifying them
