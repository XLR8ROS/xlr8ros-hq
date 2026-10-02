# XOS Memory Flow HOWTO

**XOS Timestamp:** 2026-09-16
**Scope:** XOS memory-flow procedure
**Status:** Operational How-To; governed by the Global Memory Contract and XOS HQ SOP

## Purpose

Define the end-to-end XOS memory flow from live Google Doc capture through complete episodic preservation, daily weave, canonical Markdown finalization, durable promotion, chunking, vector embedding, semantic indexing, selective retrieval, and separate lesson distillation.

## Core Flow

**Live Google Doc capture → preserve source chronology → weave/finalize in the live document → verify completeness → export canonical Markdown → commit → promote complete episode → chunk → embed → index → retrieve selectively → distill separately.**

Preservation is exhaustive. Retrieval is selective.

## Live Daily Note

During an active day, the default Daily Note is one editable Google Doc per agent/day in that agent's designated Google Drive Daily Notes folder when available.

The live Google Doc is the operational authoring surface. It remains open and additive throughout the day. It may contain WDN entries, source links, recovered verbatim, working weave material, tool-state notes, and media references.

The repository Markdown Daily Note is not the normal live scratchpad. It becomes the canonical finalized representation after the day has been woven and verified.

## Event-First Capture

Capture every recoverable turn, action, tool call, output, correction, decision, blocker, failure, recovery, external interaction, and changed understanding before it disappears from operational context.

Do not decide at capture time that something is not important enough to record.

Daily Notes preserve the operational layer. Verbatim episodic source preserves what was actually said or happened. Both matter.

## WDN

`WDN` is an explicit instruction to append the current timestamped operational state to the active live Daily Note.

When Google Docs is available, WDN writes to that day's working Google Doc. It does not create a Git commit, finalize the note, promote Durable Memory, or update the semantic index.

Acknowledging WDN without writing the note is incomplete execution.

If the Google Doc path is unavailable, use a non-destructive persistent fallback and record the deviation. A path that necessarily creates a repository commit for every WDN is not the normal WDN path.

## Verbatim Episodic Capture

When transcript or conversation material is recoverable, preserve the complete substantive episode. Keep timestamps, speaker attribution, corrections, mistakes, tangents, topic shifts, and incidental details. Mark missing material as missing rather than reconstructing it as fact.

Where the user-facing interface exposes execution disclosures such as tool results, `Worked for ...`, or other expandable execution context, preserve that exposed material when technically recoverable. Do not invent hidden reasoning that is not exposed.

Preserve recoverable photos, screenshots, audio, video, attachments, and files with source references and chronological placement. Store durable media assets where technically supported.

Do not filter source episodes according to present usefulness.

## Daily Finalization

For each date being finalized:

1. open the live Google Doc Daily Note
2. collect all recoverable timestamped conversation episodes for that date
3. collect recoverable tool/system evidence and media
4. order material chronologically
5. weave it with the operational WDN entries inside the live document
6. distinguish verbatim source from agent-authored narration
7. retain tool/system context invisible in the transcript
8. retain media/source references at their chronological positions
9. record gaps explicitly
10. verify that all substantive content from any prior Daily Note representation survives in the richer weave
11. export/reproduce the complete final weave as the canonical repository Markdown Daily Note
12. commit that canonical Markdown at the designated finalization stage

Do not commit merely because an individual WDN entry was appended.

## Durable Promotion

After canonical Daily Note finalization, promote the complete substantive episodic record to the applicable `Durable_Memory/` lane.

Promotion may normalize timestamps, add metadata/provenance, suppress exact technical duplicates without information loss, chunk content, and cross-link evidence. Promotion must not remove substantive material because it seems low-value.

Later recovery that only adds detail, depth, verbatim, timestamps, media, or provenance is additive expansion. Weave it into the richer canonical artifact; do not falsely label it a changed understanding.

There is no usefulness qualification gate for preserving episodic history.

## Chunking and Embeddings

After durable preservation:

1. split the corpus at useful semantic boundaries without substantive loss
2. attach source/provenance and media metadata where supported
3. generate approved vector embeddings
4. upsert into the applicable semantic/vector store
5. verify the indexing job
6. retain the source even if downstream processing fails

The purpose is future semantic recovery: obscure details can become relevant months later.

## Retrieval

Retrieval is where selectivity belongs. Use semantic similarity, exact search, metadata, provenance, recency, authority, and other ranking/filtering methods to surface the most relevant chunks for the current task.

For the open current day, the live Google Doc is a valid recall source. For finalized prior days, the canonical repository Markdown and Durable Memory are the primary preserved representations.

Selective retrieval never authorizes selective source preservation.

## Distilled Lessons

Distilled Lessons are a separate derived layer. Extract recurring patterns, stable procedures, corrections, lessons, preferences, tool states, and other reusable knowledge when useful.

Distillation may be selective because the full episodic source remains preserved underneath it.

## Provenance, Expansion, and Supersession

Preserve source identity, timestamps, conversation/session references, live Google Doc identity, repository file paths, commits, tasks, media paths, and tool evidence when available.

Additive reconstruction means older substantive information plus newly recovered detail becomes one richer canonical artifact. After completeness is verified, redundant finished-memory containers may be removed without deleting unique evidence or provenance.

New verified understanding may supersede old understanding only when the substantive meaning actually changes. Preserve the correction sequence when it explains how understanding changed.

## Recovery Flow

When memory is missing:

1. report the gap
2. search authorized evidence surfaces, including the Google Drive Daily Notes folder, conversation history, agent repo, HQ/Canon, files, connectors, Paperclip, commits, and external evidence
3. recover verbatim source where possible
4. preserve timestamps and provenance
5. reconstruct chronology without invention
6. weave the affected live/final Daily Note
7. verify/export canonical Markdown
8. promote the complete recovered episode
9. chunk/embed/index it
10. verify downstream processing
11. record unresolved gaps

## Approval Boundary

Routine memory capture, episodic promotion, and indexing follow the governing contract and do not require repeated approval when already authorized. Changes to protected Canon, contracts, SOPs, authority rules, or operating doctrine require Reg authorization. Reg explicitly authorized this 2026-09-16 live-Google-Doc Daily Note lifecycle.

## Completion Rule

Promotion is complete only when source preservation is verified and all requested downstream stages are either verified successful or explicitly reported blocked.

**Learn once, forget nothing, remember everything, because everything has value.**

## Current contract lifecycle and consultation requirements

The [HQ Global Memory Contract](../Global%20Memory%20Contract.md) governs this procedure.

- Default active-day surface is the agent/day Google Doc in the designated Daily Notes Drive folder when available.
- WDN updates the live document only; no automatic Git commit/finalization/promotion/indexing.
- End-of-day finalization gathers that day's conversations, exposed execution context, operational state, and recoverable multimedia; weaves and verifies the live document; then exports canonical Markdown for the repository.
- Preserve every recoverable episode and its attachments/photos/audio/video/media references. Promote all content to Durable Memory independently of embedding eligibility or indexing success.
- Use the accepted America/New_York day boundary, retaining original timestamps/offsets and UTC. A two-finalized-note Recent window is a storage rule, distinct from rolling 48-hour bootstrap recall.
- When a third finalized note arrives, move the oldest into its calendar-month Daily Notes folder and update provenance pointers. Never delete source because indexing failed.
- Keep the current month and two preceding months uncompressed. Older complete monthly packages become eligible for lossless compression only after complete Durable Memory promotion and provenance verification. Verify archive inventory/integrity before removing redundant working copies.
- No exact yearly recompression trigger is approved. Retain monthly archives unchanged until Reg approves that trigger.
- Consult the maintained Compound Engineering source index in the XOS Paperclip How-To Hub, task XOS-20, document key `compound-engineering`, before applying documented Compound Engineering procedures.
- The finalized Memory How-To Hub is in XOS Paperclip task XOS-21, document key `memory-how-to-hub`; its linked `memory-vector-procedure` records selected implementation and verification limits.
- Opera capture remains validation-gated in XOS-15. Live promotion/indexing/retrieval acceptance remains in XOS-13. Documentation alone does not establish runtime success or contract lock enforcement.
