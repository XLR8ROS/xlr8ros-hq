# XOS Memory Flow HOWTO

**XOS Timestamp:** 2026-09-14
**Scope:** XOS memory-flow procedure
**Status:** Operational How-To; governed by the Global Memory Contract and XOS HQ SOP

## Purpose

Define the end-to-end XOS memory flow from live event capture through complete episodic preservation, durable promotion, chunking, vector embedding, semantic indexing, selective retrieval, and separate lesson distillation.

## Core Flow

**Capture → preserve source chronology → finalize/weave → promote complete episode → chunk → embed → index → retrieve selectively → distill separately.**

Preservation is exhaustive. Retrieval is selective.

## Event-First Capture

Capture every recoverable turn, action, tool call, output, correction, decision, blocker, failure, recovery, external interaction, and changed understanding before it disappears from operational context.

Do not decide at capture time that something is not important enough to record.

Daily Notes preserve the operational layer. Verbatim episodic source preserves what was actually said or happened. Both matter.

## WDN

`WDN` is an explicit instruction to append the current timestamped operational state to the active Daily Note using the available persistent write path. Acknowledging WDN without writing the note is incomplete execution.

## Verbatim Episodic Capture

When transcript or conversation material is recoverable, preserve the complete substantive episode. Keep timestamps, speaker attribution, corrections, mistakes, tangents, topic shifts, and incidental details. Mark missing material as missing rather than reconstructing it as fact.

Do not filter source episodes according to present usefulness.

## Daily Finalization

For each date being finalized:

1. load the existing Daily Note
2. collect all recoverable timestamped verbatim episodes
3. order them chronologically
4. weave them with operational Daily Note entries
5. distinguish verbatim source from agent-authored narration
6. retain tool/system context invisible in the transcript
7. record gaps explicitly
8. save the final Markdown file

## Durable Promotion

Promote the complete substantive episodic record to the applicable `Durable_Memory/` lane.

Promotion may normalize timestamps, add metadata/provenance, suppress exact technical duplicates without information loss, chunk content, and cross-link evidence. Promotion must not remove substantive material because it seems low-value.

There is no usefulness qualification gate for preserving episodic history.

## Chunking and Embeddings

After durable preservation:

1. split the corpus at useful semantic boundaries without substantive loss
2. attach source/provenance metadata where supported
3. generate approved vector embeddings
4. upsert into the applicable semantic/vector store
5. verify the indexing job
6. retain the source even if downstream processing fails

The purpose is future semantic recovery: obscure details can become relevant months later.

## Retrieval

Retrieval is where selectivity belongs. Use semantic similarity, exact search, metadata, provenance, recency, authority, and other ranking/filtering methods to surface the most relevant chunks for the current task.

Selective retrieval never authorizes selective source preservation.

## Distilled Lessons

Distilled Lessons are a separate derived layer. Extract recurring patterns, stable procedures, corrections, lessons, preferences, tool states, and other reusable knowledge when useful.

Distillation may be selective because the full episodic source remains preserved underneath it.

## Provenance and Supersession

Preserve source identity, timestamps, conversation/session references, file paths, commits, tasks, and tool evidence when available.

New verified understanding may supersede old understanding without deleting historical evidence. Preserve the correction sequence when it explains how understanding changed.

## Recovery Flow

When memory is missing:

1. report the gap
2. search authorized evidence surfaces, including conversation history, agent repo, HQ/Canon, files, connectors, Paperclip, commits, and external evidence
3. recover verbatim source where possible
4. preserve timestamps and provenance
5. reconstruct chronology without invention
6. finalize the Daily Note
7. promote the complete recovered episode
8. chunk/embed/index it
9. verify downstream processing
10. record unresolved gaps

## Approval Boundary

Routine memory capture, episodic promotion, and indexing follow the governing contract and do not require repeated approval when already authorized. Changes to protected Canon, contracts, SOPs, authority rules, or operating doctrine require Reg authorization. Reg explicitly authorized the 2026-09-14 correction aligning this How-To with exhaustive episodic preservation.

## Completion Rule

Promotion is complete only when source preservation is verified and all requested downstream stages are either verified successful or explicitly reported blocked.

**Learn once. Forget nothing. Remember everything. Because everything has value.**

## Current contract lifecycle and consultation requirements

The [HQ Global Memory Contract](../Global%20Memory%20Contract.md) governs this procedure. Its September 14 reconciliation supersedes earlier selective-promotion wording.

- Preserve every recoverable episode and its attachments/photos/media references. Promote all content to Durable Memory independently of embedding eligibility or indexing success.
- Use the accepted America/New_York day boundary, retaining original timestamps/offsets and UTC. A two-finalized-note Recent window is a storage rule, distinct from rolling 48-hour bootstrap recall.
- When a third finalized note arrives, move the oldest into its calendar-month Daily Notes folder and update provenance pointers. Never delete source because indexing failed.
- Keep the current month and two preceding months uncompressed. Older complete monthly packages become eligible for lossless compression only after complete Durable Memory promotion and provenance verification. Verify archive inventory/integrity before removing redundant working copies.
- No exact yearly recompression trigger is approved. Retain monthly archives unchanged until Reg approves that trigger; approximately three months into the next year is context, not a schedule.
- Consult the maintained Compound Engineering source index in the XOS Paperclip How-To Hub, task XOS-20, document key `compound-engineering`. Read its version-pinned upstream documentation and runtime SKILL.md references before applying a procedure. Re-consult before planning/debugging/review in a documented area, after qualifying verified work, and when months-old Durable Memory becomes relevant. Distillation remains selective and separate from preservation.
- The finalized Memory How-To Hub is in XOS Paperclip task XOS-21, document key `memory-how-to-hub`; its linked `memory-vector-procedure` records the selected implementation and verification limits. These are Paperclip document identifiers, not repository file paths. If unavailable, report the missing reference rather than inventing procedure details.
- Opera capture remains validation-gated in XOS-15. Live promotion/indexing/retrieval acceptance remains in XOS-13. Documentation and a successful file comparison do not establish runtime success or contract lock enforcement.
