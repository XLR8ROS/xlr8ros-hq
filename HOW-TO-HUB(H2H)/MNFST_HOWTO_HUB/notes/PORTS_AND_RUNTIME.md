# Ports and Runtime Notes

## Known Issue

If Manifest fails to start after reboot or Docker update, check whether the expected host port is already occupied.

## Current Diagnostic Pattern

- `manifest-1` may expose a dashboard/runtime port.
- `postgres-1` can run while `manifest-1` is stopped.
- A local Node process can occupy ports and block Docker from binding the same host port.
- Confirm actual process ownership before killing anything.

## Safe Order

1. Identify process using port.
2. Identify container port bindings.
3. Read Manifest logs.
4. Decide whether to stop local process, change host port, or recreate container.
