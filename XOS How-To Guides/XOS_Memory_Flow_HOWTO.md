# XOS Memory Flow HOWTO

**XOS Timestamp:** 2026-05-15
**Scope:** CodiCore repo-local operational procedure; mirrorable into XOS canon.
**Status:** Operational how-to, not root canon by itself.

## Purpose

This how-to explains how Codi captures events, preserves evidence, and converts evidence into durable operational memory without editing protected root files.

## Event-First Capture

Every meaningful turn, action, tool call, output, correction, decision, blocker, failure, recovery, and changed understanding is captured first as an event.

Write live capture to:

`memory/YYYY-MM-DD.md`

Use one active daily note per date. Append chronologically. Use timestamps to seconds when possible and milliseconds when runtime supports it.

Do not decide at capture time that something is not important enough to record. Later review can lower weight, supersede, classify, distill, or promote.

## Three Whys

Each meaningful event should record three whys when knowable:

1. proximate why — why now; what triggered the current turn/action/decision
2. method why — why this response/action/method; what current thought, belief, uncertainty, or understanding shaped it
3. historical why — why this pattern/rule exists; what prior memory, correction, failure, canon, lesson, or precedent shaped it

If Reg's why is not explicit, Codi may record an inferred why clearly marked as inferred.

## Event Dimensions

Each event may carry multiple dimensions:

- dialogue: user direction, correction, clarification, approval, rejection, open question, answer
- thought: belief, assumption, uncertainty, anchor, intent, confidence, pressure signal, changed understanding
- knowledge: new information, belief, understanding, fact, truth record, canon, canonized truth
- action/output: command, file change, cron change, Moltbook post/comment/reply, report, artifact, commit
- problem/recovery: blocker, failure, contradiction, rollback, restore, resolved blocker
- rule/standard: standing rule, procedure, canon candidate, policy conflict

Open question means real missing evidence or conflict. It does not mean asking Reg permission for something Reg already instructed.

## Evidence Feeds

Review these feeds for promotion and durable extraction:

1. `memory/YYYY-MM-DD.md` — active daily chronological event capture
2. `sessions/` — session records, handoffs, transcripts, focused work blocks
3. `Outputs/` — proposals, reports, proofs, healthchecks, heartbeat reports, cleanup reports, promotion logs, generated artifacts
4. `event-log/` — structured SQLite event ledger and audits
5. `DREAMS.md` / `dreams.md` — OpenClaw Dreaming review diary if present
6. relevant legacy evidence when needed

`memory/.dreams/` is machine state, not human memory. Do not promote raw `.dreams` state.

## Promotion Flow

Event capture → evidence review → classify dimensions/status → extract facts/truth/procedures/tool states/lessons → `Durable_Memory/` → promotion log in `Outputs/promotion-logs/` → refresh semantic hooks/indexes where supported.

No `memory/candidates/` folder. Promotion is one pass.

Do not copy raw daily notes into durable memory as promotion. Durable memory is derived from source-backed events and keeps evidence references.

## What Qualifies

Promote when remembering it would reduce future friction, prevent repeated mistakes, improve routing, preserve a resolved blocker, document stable tool state, preserve user direction, improve safety/speed, or explain a recurring why.

Qualifying durable memory includes distilled lessons, failure lessons, user corrections, standing rules, stable procedures, resolved blockers, tool/environment facts, truth records, durable preferences, decisions/conventions, relationship context, and "do not repeat this" lessons.

## Provenance and Supersession

Use simple precedence:

- evidence beats belief
- truth checks canon when canon conflicts with reality
- canon guides behavior when aligned with truth or accepted as rule
- Reg's direction beats Codi inference, but does not automatically make factual claims true
- newer verified understanding can supersede older understanding without deleting old evidence
- stronger why/provenance beats surface keyword similarity

When superseding, record old memory reference, new memory, evidence path, reason, timestamp, and approval status.

## Approval Boundary

Codi does not need Reg approval for routine durable operational memory promotion into `Durable_Memory/`.

Codi does need exact Reg approval before editing protected docs, canon, authority rules, role definitions, policy, SOP/governance docs, or operating doctrine.

A memory may mention canon-sensitive material without changing canon.

## Promotion Log Minimum

Each promotion log must include sources reviewed, source/evidence paths, event dimensions/classes applied, three-why gaps or weak inferred whys when relevant, promoted memory summary, destination path, qualification reason, rejected/lowered items if relevant, approval-sensitive items, and timestamp.

## Dreaming Boundary

OpenClaw Dreaming may produce `DREAMS.md` and machine state under `memory/.dreams/`. Use `DREAMS.md` as evidence if present.

Do not allow Dreaming deep promotion to write into CodiCore `MEMORY.md` unless Reg explicitly authorizes it, because CodiCore uses `MEMORY.md` as protected contract.
