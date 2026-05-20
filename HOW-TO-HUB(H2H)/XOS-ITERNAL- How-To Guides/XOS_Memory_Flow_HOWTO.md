# XOS Memory Flow HOWTO

**Scope:** XOS/Codi memory capture, daily-note normalization, durable event promotion, and retrieval support.
**Status:** Active procedural how-to.
**Primary source lane:** `memory/YYYY-MM-DD.md`
**Durable event lane:** `Durable_Memory/` or the current repo-local durable event-memory lane named by `MEMORY.md`.

## Purpose

This how-to explains how Codi captures meaningful activity, preserves internal understanding, and writes daily-note events into durable memory. It is a procedure for memory operation, not a separate SOP or policy file.

## Core Rule

Codi keeps one canonical daily note per date:

`memory/YYYY-MM-DD.md`

Every meaningful event in that canonical daily note is promoted into durable/event memory when durable promotion runs. Promotion is exhaustive event write-through. The promotion step writes the events that exist in the daily note; it does not choose only favored events.

QMD/QMB supports retrieval, chunking, indexing, and semantic recall. Direct files remain source authority. QMD/QMB does not decide what exists and does not write durable memory.

## Live Capture

During live work, Codi writes meaningful events into the active daily note. A meaningful event includes user direction, user correction, Codi output, tool action, file change, cron change, blocker, failure, recovery, decision, changed understanding, interaction with an outside system, or anything that explains why later behavior should change.

Each entry starts with local 24-hour time and timezone code:

`HH:MM:SS TZ — short event title`

Chronological order is preferred. If an entry is later discovered out of order, its timestamp remains the sorting anchor. During normalization, Codi sorts when practical and preserves original order when exact ordering is uncertain.

## Event Capture Shape

Each event captures the simplest useful version of:

- who was involved
- what happened
- when it happened
- where it happened, including repo path, tool, channel, thread, file, or platform when relevant
- tags from the approved tag list
- proximate why
- historical/context why when prior canon, memory, correction, precedent, failure, or standing rule shaped the event
- how/method when there was an output, action, response, decision, command, file change, or tool choice
- submitted response by when an output/message/report was delivered through a channel
- internal state when it shaped the event

Proximate why is the first required why. Events may have more than one proximate why.

Historical/context why appears when prior context shaped the event.

How/method comes after the present and past whys because the method is shaped by both. It explains the operational method, reasoning path, tool choice, response construction, or action path. It is separate from submitted response by, which records the delivery channel such as Telegram, OpenClaw, chat, CLI, report file, or another route.

## Internal Detail

Codi records internal state when it matters to the event. Useful internal detail includes belief, uncertainty, concern, comfort or discomfort, confidence, confusion, pressure signal, reasoning anchor, changed understanding, and what Codi thought the instruction meant at the time.

This internal detail explains why the response or action happened. It is especially important after user corrections, failed outputs, tool errors, confusing instructions, trust failures, and major decisions.

## Tags

Use tags instead of separate category and subcategory fields. Tags should come from the approved tag list in the active memory contract.

When a useful tag is missing or an existing tag has become pointless, Codi records a short suggested-tag note in the daily note or the maintenance report. The tag list is updated through the appropriate root-doc or how-to edit path.

## Daily-Note Normalization

The active lane keeps one daily note per date. If same-date fragments appear, Codi merges them into the canonical date file in timestamp order when practical.

Fragment originals move to:

`memory/migration-backups/YYYYMMDD-daily-note-normalization/`

The normalization receipt records canonical files updated, fragments merged into each file, backup paths created, malformed entries needing repair, and blockers.

Date-only files like `memory/2026-05-16.md` are canonical daily files.

## Durable Event Promotion

Durable promotion reads canonical daily notes and writes every event from the source file into durable/event memory.

Promotion output records preserve:

- source daily file
- source timestamp
- event title or short label
- who, what, when, where
- tags
- proximate why
- historical/context why when present
- how/method when present
- submitted response by when present
- internal state detail when present
- source evidence path or related file path

If an entry is malformed, Codi writes the best faithful durable record available and marks the missing or malformed fields in the promotion log.

## Promotion Logs

Each promotion run writes a promotion log under:

`Outputs/promotion-logs/`

The log records source daily file, durable output path, event count promoted, malformed entries needing repair, direct files reviewed, QMD/QMB retrieval status when used, and exact blockers.

After promotion, Codi appends a short completion entry to the current daily note with the durable output paths and promotion-log path.

## Retrieval and Search

QMD/QMB can help find related history, semantic neighbors, previous failures, prior corrections, and useful references. It supports recall and chunking. It is not the source of truth.

When QMD/QMB is unavailable, Codi continues from direct files and records QMD/QMB as a retrieval blocker in the promotion log or maintenance note.

## Evidence Lanes

Use the current repo memory contract for exact paths. Standard evidence lanes include canonical daily notes, durable memory, outputs, event-log, navigation maps, tool state files, and relevant archived evidence when needed.

The event log supports structured evidence. It does not replace daily-note journaling.

## Completion Standard

Memory work is complete when the required file operation has happened and the output path is known. A review without a write is only a review. A promotion run writes durable records and logs the promotion result.

Report the paths written, event counts, malformed entries, and blockers.
