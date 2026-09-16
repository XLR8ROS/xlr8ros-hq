# XOS-HQ-HOWTO-MEMORY-SYSTEM-OPERATION.md
**Version:** 2026-09-16
**Authority:** HQ

## 1. Purpose

Define how to operate the XOS memory system in practice: live Google Doc Daily Notes, verbatim recovery, daily finalization, canonical Markdown export, exhaustive episodic promotion, chunking, embedding, semantic indexing, retrieval, and recovery from missing memory.

## 2. Governing Model

**Preservation is exhaustive. Retrieval is selective.**

Do not decide during capture or episodic promotion what will matter later. Preserve the recoverable substantive episode first. Relevance ranking belongs to retrieval and distilled-memory layers.

## 3. Live Daily Note Surface

During an active day, use an editable Google Doc in the agent's designated Google Drive Daily Notes folder as the default live Daily Note surface when available.

Recommended structure:

- one Daily Notes folder per agent
- one clearly named live Google Doc per agent/day, e.g. `2026-09-16 — Nex Working Daily Note`
- chronological timestamped WDN entries throughout the day
- source links, recovered verbatim, working weave material, and media references may be added while the day remains open

The Google Doc is the live working and inspection surface. It is not the finalized canonical repository artifact.

Do not use the repository Markdown file as a live scratchpad when the designated Google Doc surface is available.

## 4. Daily Execution

For every recoverable turn, action, decision, correction, blocker, failure, recovery, tool action, external interaction, or changed understanding:

1. perform or answer the current work
2. append operational context to the active Google Doc Daily Note when needed
3. preserve source evidence in the correct lane
4. place outputs correctly
5. do not discard material because it appears unimportant

Append chronologically with precise timestamps.

`WDN` means write the current operational state to the active live Daily Note immediately. A chat acknowledgment without a persistent write is not completion.

A WDN append does **not** mean:

- commit to GitHub
- finalize the Daily Note
- promote to Durable Memory
- update the vector index
- close the day's note

If Google Docs is unavailable, use the best available non-destructive persistent fallback and record the deviation. Do not silently fall back to one Git commit per WDN append.

## 5. What Daily Notes Add

Daily Notes preserve information a verbatim transcript may not contain: tool calls and material results, system/file/config changes, success/failure/partial state, corrections, decisions, blockers, dependencies, handoffs, unresolved state, and concise judgment summaries.

Do not treat Daily Notes as a substitute for the complete verbatim episode.

## 6. Verbatim Recovery

When conversation history or another episodic source is available:

1. capture the complete recoverable episode
2. preserve original timestamps and speaker attribution when available
3. retain corrections, mistakes, tangents, topic changes, and incidental material
4. do not select only material presently judged useful
5. record provenance such as conversation/thread/source URL or file when available
6. expand user-visible execution disclosures such as `Thinking`, `Worked for ...`, tool-result summaries, or similar exposed context when technically available
7. preserve attachment/photo/audio/video/file position and source references
8. mark gaps rather than inventing missing text

Hidden reasoning that is not actually exposed must not be invented.

## 7. Daily Finalization / Weave

At finalization for a date:

1. open that date's live Google Doc Daily Note
2. gather all recoverable conversations and episodic sources for that date
3. gather recoverable photos, audio, video, files, and other media
4. order source material chronologically by timestamp
5. weave the verbatim chronology with operational Daily Note material inside the live document
6. clearly distinguish verbatim source from agent-authored operational narration
7. preserve tool/system context not visible in the transcript
8. preserve media references and repository asset paths where available
9. record unresolved gaps
10. verify the final woven document contains all substantive material from any prior Daily Note representation plus the newly recovered detail
11. export/reproduce the complete woven result as the canonical Markdown Daily Note in the agent repository
12. commit the canonical Markdown only at the designated finalization stage

Do not omit an episode merely because it appears repetitive, humorous, off-topic, mistaken, or low-value.

The final repository Markdown is the canonical closed Daily Note. The Google Doc remains the live/readable authoring history surface.

## 8. Media Handling

When recoverable media exists:

1. preserve the original asset when technically available
2. store a repository-side memory asset or other approved durable copy when supported
3. assign a stable path or source reference
4. link or embed that reference at the correct chronological location in the Daily Note
5. carry provenance into Durable Memory and indexing metadata
6. do not replace an inaccessible asset with an invented description

## 9. Exhaustive Episodic Promotion

After the Daily Note is woven, verified, exported to canonical Markdown, and committed:

1. promote the complete substantive episodic record into the repo's `Durable_Memory/` lane
2. retain provenance and chronology
3. normalize metadata as needed
4. suppress only exact technical duplicates when no substantive information is lost
5. preserve earlier incorrect states alongside later corrections when they are part of the episode
6. treat later recovery that merely adds detail as additive expansion, not supersession
7. do not apply a usefulness qualification gate to episodic preservation

Distilled Lessons are separate and may be selective. They never replace Durable Memory.

## 10. Chunking and Semantic Indexing

After durable preservation:

1. chunk the preserved corpus at useful semantic boundaries without dropping substantive content
2. retain source IDs, timestamps, media references, and provenance on chunks where supported
3. generate vector embeddings using the approved embedding workflow
4. upsert chunks into the applicable semantic/vector index
5. verify the indexing run completed successfully
6. preserve source files even when embedding/indexing fails
7. retry downstream processing without requiring source recapture

The vector store exists so future searches can surface details whose importance was unknowable when captured.

## 11. Retrieval

Retrieval may be selective. Use semantic search, metadata filters, recency, source provenance, exact text search, and other ranking mechanisms to return the material relevant to the current question.

For the still-open current day, the live Google Doc is a valid Agent Recall source. For finalized prior days, prefer the canonical repository Markdown and Durable Memory corpus.

Do not confuse selective retrieval with selective preservation.

## 12. Recovery When Memory Is Missing

When expected Daily Notes, transcripts, Durable Memory, or contract material is absent:

1. report the gap immediately
2. search the live Google Drive Daily Notes folder, agent repo, HQ/Canon, conversation history, available files, connectors, Paperclip, commits, external evidence, and other authorized sources
3. recover verbatim source where possible
4. preserve timestamps/provenance
5. reconstruct chronology without invention
6. weave recovery into the applicable live/final Daily Note
7. export/verify the canonical Markdown Daily Note
8. promote the recovered episode into Durable Memory
9. chunk/embed/index it
10. verify the downstream job
11. record anything still missing

## 13. Bootstrap Memory Load

At startup, follow the agent's bootstrap documents. Load the required recent Agent Recall window. Include the current live Google Doc when the day is still open. If required files are missing, bootstrap is incomplete; state the blocker and use the maximum verified continuity available while the defect is repaired.

## 14. Evidence, Expansion, and Supersession

Evidence beats belief.

If newly recovered material only adds depth, verbatim, media, timestamps, tool context, or provenance while leaving the earlier understanding intact, merge it as additive expansion. Once all substantive content has been verified inside the richer canonical artifact, redundant old containers may be removed without deleting unique evidence.

Newer verified understanding may supersede older understanding when the meaning actually changes. Preserve corrections as corrections, not silent rewrites of history.

## 15. Failure Handling

If capture fails on a minor action, use the best available fallback as soon as possible. If capture fails on a critical/system-changing action, preserve evidence and stop when necessary to prevent loss.

If Google Docs is unavailable, use a non-destructive working fallback and document the deviation. Do not convert the live lifecycle into per-entry Git commits merely because another storage surface is inconvenient.

If promotion, chunking, embedding, or indexing fails, the source remains authoritative and preserved. Retry downstream processing later.

## 16. Completion Check

Memory work is complete only when the required source is preserved and the requested downstream operation is either verified complete or explicitly reported blocked.

For finalization/promotion work, verify:

- live Daily Note source preserved
- source chronology fully woven
- media references/assets preserved where recoverable
- canonical Markdown Daily Note exported and committed
- no substantive prior content lost
- Durable Memory copy exists
- chunks generated without substantive loss
- embeddings/index refresh succeeded where supported
- provenance retained
- unresolved gaps recorded

## 17. Principle

**Capture live in the open document. Weave completely. Finalize once. Commit the canonical record. Preserve completely. Retrieve selectively. Distill separately.**

## Current contract lifecycle and consultation requirements

The [HQ Global Memory Contract](../Global%20Memory%20Contract.md) governs this procedure.

- Default live Daily Note surface: agent/day Google Doc in the designated Google Drive Daily Notes folder when available.
- WDN writes update the live document only; they do not themselves authorize Git commits, finalization, promotion, or indexing.
- At end-of-day/finalization, recover all conversations and exposed execution context, weave the live document, preserve recoverable media, verify completeness, export canonical Markdown, then commit and promote.
- Preserve every recoverable episode and its attachments/photos/audio/video/media references. Promote all content to Durable Memory independently of embedding eligibility or indexing success.
- Use the accepted America/New_York day boundary, retaining original timestamps/offsets and UTC. A two-finalized-note Recent window is a storage rule, distinct from rolling 48-hour bootstrap recall.
- When a third finalized note arrives, move the oldest into its calendar-month Daily Notes folder and update provenance pointers. Never delete source because indexing failed.
- Keep the current month and two preceding months uncompressed. Older complete monthly packages become eligible for lossless compression only after complete Durable Memory promotion and provenance verification. Verify archive inventory/integrity before removing redundant working copies.
- No exact yearly recompression trigger is approved. Retain monthly archives unchanged until Reg approves that trigger; approximately three months into the next year is context, not a schedule.
- Consult the maintained Compound Engineering source index in the XOS Paperclip How-To Hub, task XOS-20, document key `compound-engineering` before applying documented Compound Engineering procedures.
- The finalized Memory How-To Hub is in XOS Paperclip task XOS-21, document key `memory-how-to-hub`; its linked `memory-vector-procedure` records the selected implementation and verification limits.
- Opera capture remains validation-gated in XOS-15. Live promotion/indexing/retrieval acceptance remains in XOS-13. Documentation and a successful file comparison do not establish runtime success or contract lock enforcement.
