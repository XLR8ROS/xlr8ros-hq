# XOS Navigation

This file is the routing index for XOS-wide artifacts that must remain synchronized across agent repositories.

## Global Memory Contract

**Canonical source:** `XLR8ROS/xlr8ros-hq/Global Memory Contract.md`

**Synchronization direction:** HQ -> agent-local copies.

On 2026-09-30, the then-best locked local copy in `reginaldberry02-sys/NexCore` was promoted verbatim to HQ as the canonical baseline. After that one-time reconciliation, edits must be made to the HQ canonical file only. Agent-local copies are downstream synchronized mirrors and must not become competing authorities.

### Registered local copies

- `reginaldberry02-sys/NexCore/Global Memory Contract.md`
- `reginaldberry02-sys/AddisonCore/Global Memory Contract.md`
- `reginaldberry02-sys/EddieCore/Global Memory Contract.md`
- `XLR8ROS/CodiCore/Global Memory Contract.md`
- `XLR8ROS/PaigeCore/Global Memory Contract.md`

Each registered agent repository must contain `.github/workflows/sync-global-memory-contract.yml`. The workflow pulls the canonical HQ file, verifies textual equality, updates the local mirror only when needed, writes synchronization metadata outside the governing contract text, and commits the repair automatically.

## Adding an agent

When a new agent repository is created:

1. Add its local contract path to this registry.
2. Install the canonical `Global Memory Contract.md` copy.
3. Install `Global Memory Contract.metadata.md`.
4. Install `.github/workflows/sync-global-memory-contract.yml`.
5. Verify the local contract blob SHA equals the HQ canonical blob SHA.

The governing contract text itself must remain free of agent-local metadata and synchronization receipts.
