# XOS Repo Hygiene HOWTO

**XOS Timestamp:** 2026-05-05
**Scope:** CodiCore repo-local copy; mirrorable into XOS canon after review.
**Status:** Operational how-to, not root canon by itself.

## 1. Purpose

This how-to tells Codi how to keep CodiCore clean without inventing lanes, deleting evidence, mixing memory classes, or touching protected files.

This file holds detailed repo-lane procedure so root governance files such as `AGENT.md` and `MEMORY.md` can stay small and point here instead of carrying the whole lane map.

## 2. Authority boundary

- Higher XOS canon, Constitution/Articles, approved SOPs, and explicit Reg direction outrank this file.
- `MEMORY.md`, `AGENT.md`, `AGENTS.md`, `USER.md`, `IDENTITY.md`, `SOUL.md`, `TOOLS.md`, and other root governance/control files are protected.
- Do not edit protected root files unless Reg explicitly authorizes the exact file change.
- If repo layout, lane ownership, or authority is unclear, stop and report the structure gap before moving files.

## 3. Navigation and how-to pointer

- Path-finding map: `navigation/navigation.md`.
- Repo hygiene detail: this file.
- Memory promotion detail: `navigation/XOS_Memory_Flow_HOWTO.md`.
- Root files should point here for detail. Do not duplicate the full map inside root governance files.
- Repo-local how-tos are operational references. They do not override higher XOS canon.

## 4. Canonical lanes

### 4.1 Root/protected files

- `AGENT.md` = Codi operating law.
- `AGENTS.md` = workspace behavior and startup rules.
- `MEMORY.md` = protected memory contract.
- `USER.md` = Reg reference profile.
- `IDENTITY.md` = Codi identity.
- `SOUL.md` = Codi behavioral spirit.
- `TOOLS.md` = local tool/environment notes.
- `HEARTBEAT.md` = heartbeat behavior prompt.

### 4.2 Active daily-note lane

- `memory/YYYY-MM-DD.md` = active OpenClaw daily-note injection lane.
- Exactly one active daily-note file per date.
- Append to the same date file during the day.
- Times, source labels, and entry names go inside the file as headings, not in the filename.
- Correct: `memory/2026-05-05.md`.
- Incorrect: `memory/2026-05-05-1032.md`, `memory/2026-05-05-summary.md`, `memory/2026-05-05-audio-default.md`.

Allowed direct children of `memory/`:
- `YYYY-MM-DD.md` daily-note files.
- `migration-backups/` during cleanup/recovery.
- `.dreams/` only if OpenClaw Dreaming requires machine state.

Do not place outputs, reports, proposals, scripts, logs, artifacts, distilled lessons, or standalone summaries directly in `memory/`.

### 4.3 Durable memory lane

- `Durable_Memory/` = promoted durable operational memory.
- Distilled lessons, stable procedures, resolved blockers, tool facts, and durable preferences go here after review.
- Raw daily notes do not go here unchanged.

### 4.4 Evidence and output lanes

- `sessions/` = Codi-owned session evidence, transcripts, summaries, handoffs, focused work records.
- `Outputs/` = proposals, reports, proofs, inventories, healthchecks, heartbeat reports, cleanup reports, promotion logs, snapshots, generated artifacts.
- `event-log/` = SQLite event-log database, schema docs, README, migrations, audit summaries.
- `tools/event-log/` = SQLite/event-log scripts, readers, writers, exporters, summarizers.
- `navigation/` = path navigator and operational how-tos.
- `archives/` = retired evidence, old daily notes, old sessions, old outputs, legacy imported memory/history.
- `DREAMS.md` or `dreams.md` = human-readable Dreaming review diary if present.

### 4.5 Retired or legacy lanes

- `daily-notes/` = retired/legacy daily-note lane unless Reg explicitly restores it. Use only as migration source if old notes still exist there.
- Retired output lanes: `outputs/`, `output/`, `Outputs 2/`, top-level `reports/`.
- Do not create or revive retired lanes without Reg approval.

## 5. Before moving anything

Before any cleanup, merge, rename, archive, or lane change:

1. Produce exact inventory, not a summary.
2. Identify protected files.
3. Identify tracked/untracked state with `git status --short` when git is relevant.
4. Propose exact old path → new path.
5. State which files will be preserved, merged, moved, skipped, or archived.
6. Create a recoverable backup when content could be lost or overwritten.
7. Verify source/destination before moving.
8. Wait for Reg when scope, authority, destination, or file class is unclear.

No file in scope should be left without a plan or a skip reason.

## 6. Move and merge rules

- Use existing canonical lanes.
- Do not create new lanes without Reg.
- Do not edit protected root files as part of cleanup unless explicitly authorized.
- Do not delete unless Reg explicitly authorizes deletion.
- Recoverable move beats destructive removal.
- If output is large, save inventory under `Outputs/inventories/`.
- When merging multiple files into one canonical file, preserve source content. Do not summarize unless explicitly instructed.
- Use source headings inside the merged file when needed.
- For daily notes, merged output goes to `memory/YYYY-MM-DD.md`. Backup folders hold originals only.

## 7. Daily-note naming hygiene

Active daily notes must obey:

- Location: `memory/`
- Filename: `YYYY-MM-DD.md`
- One active file per date.
- No suffixes.
- No time in filename.
- No duplicate same-date active files.

If a date-bearing source file is noncanonical, extract the first `YYYY-MM-DD` from the filename and merge into `memory/YYYY-MM-DD.md` only if it is truly daily-note content.

Backup copies inside `memory/migration-backups/` are not active files.

## 8. Placement examples

- Daily note → `memory/YYYY-MM-DD.md`.
- Session transcript or handoff → `sessions/YYYY/MM/` or current session lane if defined.
- Proposal → `Outputs/proposals/`.
- Report → `Outputs/reports/`.
- Heartbeat report → `Outputs/heartbeat/`.
- Healthcheck → `Outputs/healthchecks/`.
- Cleanup report → `Outputs/cleanup/`.
- Promotion log → `Outputs/promotion-logs/`.
- Proof file → `Outputs/proofs/`.
- Inventory/path map → `Outputs/inventories/`.
- Snapshot evidence → `Outputs/snapshots/`.
- SQLite DB/schema/docs → `event-log/`.
- SQLite scripts/tools → `tools/event-log/`.
- Distilled lesson → `Durable_Memory/`.
- Old legacy memory → `archives/legacy-memory/`.
- Retired daily-note source after migration → `archives/daily-notes/` or approved migration backup.

## 9. Duplicate lane cleanup

If duplicate lanes exist by spelling, casing, or drift:

1. Stop and inventory exact paths.
2. Classify each lane.
3. Propose canonical destination.
4. Preserve source evidence before moves.
5. Do not silently merge unrelated classes.

The canonical output lane is `Outputs/`. Do not use `outputs/`, `output/`, `Outputs 2/`, or top-level `reports/`.

## 10. Verification report

After any approved cleanup or move, report:

- old path → new path
- file class
- content preserved yes/no
- verification method
- exact files moved
- exact files skipped and why
- final direct listing of affected folders
- exact `git status --short` if git is relevant
- unresolved risks

Never report “several,” “multiple,” “appears,” or “likely” when exact evidence is requested. Chunk large output or save the exact output under `Outputs/`.
