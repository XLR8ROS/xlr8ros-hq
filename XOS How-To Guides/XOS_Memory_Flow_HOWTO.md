# XOS Memory Flow HOWTO

**XOS Timestamp:** 2026-05-04 21:01:01 EDT
**Scope:** CodiCore repo-local copy; mirrorable into XOS canon.
**Status:** Operational how-to, not root canon by itself.

## Purpose

This how-to explains how Codi converts evidence into durable operational memory without editing protected root files.

## Evidence feeds

Review these feeds for promotion:

1. `daily-notes/` — daily/timestamped raw evidence.
2. `sessions/` — session-specific records, handoffs, transcripts, focused work blocks.
3. `Outputs/` — proposals, reports, proofs, healthchecks, heartbeat reports, cleanup reports, promotion logs, generated artifacts.
4. `event-log/` — structured SQLite event ledger.
5. `DREAMS.md` — OpenClaw Dreaming review diary if present.

`memory/.dreams/` is machine state, not human memory. Do not promote raw `.dreams` state.

## Promotion flow

Evidence feeds → review → distilled lessons/facts/procedures → `Durable_Memory/` → promotion logged in `Outputs/promotion-logs/`.

No `memory/candidates/` folder. Promotion is one pass.

## What qualifies

Promote when remembering it would reduce future friction, prevent repeated mistakes, improve routing, preserve a resolved blocker, document stable tool state, or improve safety/speed.

Qualifying memory types:

- distilled lessons
- failure lessons
- user corrections
- stable procedures
- resolved blockers
- tool/environment facts
- durable preferences
- decisions/conventions
- “do not repeat this” lessons

## Distillation examples

Bad raw memory:
“Reg got mad because Codi messed up inventory.”

Good distilled lesson:
“When Reg requests exact filesystem inventory, provide exact paths or chunk/save full output. Do not silently summarize.”

Bad raw memory:
“Codi edited MEMORY.md.”

Good distilled lesson:
“Memory promotion never authorizes editing protected root files such as MEMORY.md.”

## Approval boundary

Codi does not need Reg approval for routine durable operational memory promotion into `Durable_Memory/`.

Codi does need exact Reg approval before editing protected docs, canon, authority rules, role definitions, policy, SOP/governance docs, or operating doctrine.

A memory may mention canon-sensitive material without changing canon.

## Recency and supersession

Newer verified operational memory may supersede older operational memory when facts changed, a blocker resolved, a tool state changed, or Reg corrected old understanding.

Newer evidence does not override protected canon or explicit Reg direction unless Reg explicitly changes it.

When superseding, record old memory reference, new memory, evidence path, reason, timestamp, and approval status.

## Dreaming boundary

OpenClaw Dreaming may produce `DREAMS.md` and machine state under `memory/.dreams/`. Use `DREAMS.md` as evidence if present.

Do not allow Dreaming deep promotion to write into CodiCore `MEMORY.md` unless Reg explicitly authorizes it, because CodiCore uses `MEMORY.md` as protected contract.

## Promotion log minimum

Each promotion log must include:

- sources reviewed
- source/evidence paths
- promoted memory summary
- destination path in `Durable_Memory/`
- qualification reason
- rejected items if relevant
- approval-sensitive items
- timestamp
