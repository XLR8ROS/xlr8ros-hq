# XOS-HQ-HOWTO-MEMORY-SYSTEM-OPERATION.md
**Version:** 2026-09-16
**Authority:** HQ

## 1. Purpose

Define how to operate the XOS memory system in practice: live Google Doc Daily Notes, verbatim recovery, daily finalization, canonical Markdown export, exhaustive episodic promotion, chunking, embedding, semantic indexing, retrieval, attachment/file recovery, and recovery from missing memory.

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
3. gather recoverable photos, audio, video, files, and other attachments
4. order source material chronologically by timestamp
5. weave the verbatim chronology with operational Daily Note material inside the live document
6. clearly distinguish verbatim source from agent-authored operational narration
7. preserve tool/system context not visible in the transcript
8. preserve media references and repository asset paths where available
9. record unresolved gaps
10. verify the final woven document contains all substantive material from any prior Daily Note representation plus the newly recovered detail
11. export/reproduce the complete woven result as the canonical Markdown Daily Note in the agent repository
12. package that Markdown in a date-specific folder with the recovered attachment/file assets for the date
13. commit the canonical package only at the designated finalization stage

Repository package example:

`memory/Daily_Notes/2026-09/2026-09-13/2026-09-13.md`
`memory/Daily_Notes/2026-09/2026-09-13/IMG_0135.png`

Do not omit an episode merely because it appears repetitive, humorous, off-topic, mistaken, or low-value.

The finalized date folder is the canonical closed Daily Note package. The Google Doc remains the live/readable authoring history surface.

## 8. Attachment and Media Recovery

Attachments include **all file types**, not merely images: screenshots/photos, audio, video, PDFs, documents, spreadsheets, text/Markdown, code, archives, and other files.

### 8.1 Primary retrieval

At the attachment's chronological position in the source episode:

1. record the filename/file identity when exposed
2. record the conversation/source URL and date/time when available
3. attempt to retrieve the original bytes from the primary authorized conversation/operator surface
4. preserve any exposed caption, OCR, MIME/type, stable URL, or file ID as provenance

### 8.2 Fallback ladder when the operator surface will not provide usable bytes

Do **not** stop merely because Opera, another browser/operator surface, or the conversation accessibility tree exposes only a reference.

Search authorized evidence surfaces in this order as applicable:

1. current conversation attachments/files
2. ChatGPT Library, including prior-conversation files, using the exact filename first
3. Library semantic search using filename plus conversation context, date, caption/OCR, subject, and file type
4. Google Drive or other connected file source when provenance indicates the file originated there
5. repository/existing durable assets
6. other authorized connector/source explicitly associated with the episode

For ChatGPT Library recovery:

- search the Library surface, not only the current conversation
- prefer an exact filename/title match when available
- verify the candidate using MIME type, caption/OCR/content, conversation context, date, and surrounding episode
- use the returned canonical file ID; never invent an ID from the filename
- materialize/copy the original file bytes when repository storage is required
- preserve the original filename unless collision/provenance requirements require a deterministic rename

### 8.3 Package placement

Store recovered files beside the day's Markdown inside the date folder. Link or embed the relative path at the correct chronological point in the Markdown. Preserve provenance sufficient to explain where the file came from and how it was matched.

### 8.4 Failure rule

Only mark an attachment unresolved after the applicable fallback surfaces have been checked. Preserve the original reference, filename, description/caption/OCR when exposed, and the failed recovery surfaces. Never fabricate or regenerate a substitute and call it the original.

## 9. Exhaustive Episodic Promotion

After the Daily Note is woven, verified, exported to its canonical date-folder package, and committed:

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

1. identify the **currently approved indexing implementation** from the maintained `memory-vector-procedure` / current runtime documentation before executing or claiming indexing
2. do not assume a historical backend or implementation from memory
3. chunk the preserved corpus at useful semantic boundaries without dropping substantive content
4. retain source IDs, timestamps, media references, and provenance on chunks where supported
5. generate embeddings using the currently approved workflow
6. upsert/index through the currently approved implementation
7. verify the indexing run completed successfully
8. verify retrieval against the newly indexed source/package, not merely job completion
9. preserve source files even when embedding/indexing fails
10. retry downstream processing without requiring source recapture

A Git commit is not an indexing receipt. A historical QMD, Qdrant, or other retired/experimental backend is not to be assumed current merely because it appears in older notes. The implementation named by the current maintained procedure/runtime is controlling.

## 11. Retrieval

Retrieval may be selective. Use the currently approved semantic retrieval implementation, metadata filters, exact text search, source provenance, recency, and other supported ranking mechanisms.

For the still-open current day, the live Google Doc is a valid Agent Recall source. For finalized prior days, prefer the canonical repository Markdown/date package and Durable Memory corpus.

Do not confuse selective retrieval with selective preservation.

## 12. Recovery When Memory Is Missing

When expected Daily Notes, transcripts, attachments/files, Durable Memory, or contract material is absent:

1. report the gap immediately
2. search the live Google Drive Daily Notes folder, agent repo, HQ/Canon, conversation history, ChatGPT Library, available files, connectors, Paperclip, commits, external evidence, and other authorized sources
3. recover verbatim source where possible
4. run the attachment fallback ladder for referenced files that are not directly retrievable
5. preserve timestamps/provenance
6. reconstruct chronology without invention
7. weave recovery into the applicable live/final Daily Note
8. export/verify the canonical date-folder package
9. promote the recovered episode into Durable Memory
10. chunk/embed/index it using the currently approved implementation
11. verify downstream retrieval
12. record anything still missing

## 13. Bootstrap Memory Load

At startup, follow the agent's bootstrap documents. Load the required recent Agent Recall window. Include the current live Google Doc when the day is still open. If required files are missing, bootstrap is incomplete; state the blocker and use the maximum verified continuity available while the defect is repaired.

## 14. Evidence, Expansion, and Supersession

Evidence beats belief.

If newly recovered material only adds depth, verbatim, media, timestamps, tool context, or provenance while leaving the earlier understanding intact, merge it as additive expansion. Once all substantive content has been verified inside the richer canonical artifact, redundant old containers may be removed without deleting unique evidence.

Newer verified understanding may supersede older understanding when the meaning actually changes. Preserve corrections as corrections, not silent rewrites of history.

## 15. Failure Handling

If capture fails on a minor action, use the best available fallback as soon as possible. If capture fails on a critical/system-changing action, preserve evidence and stop when necessary to prevent loss.

If Google Docs is unavailable, use a non-destructive working fallback and document the deviation. Do not convert the live lifecycle into per-entry Git commits merely because another storage surface is inconvenient.

If a primary operator surface cannot return attachment bytes, continue through the attachment fallback ladder before declaring the asset unavailable.

If promotion, chunking, embedding, or indexing fails, the source remains authoritative and preserved. Retry downstream processing later.

## 16. Completion Check

Memory work is complete only when the required source is preserved and the requested downstream operation is either verified complete or explicitly reported blocked.

For finalization/promotion work, verify:

- live Daily Note source preserved
- source chronology fully woven
- every referenced attachment/file was recovered or its fallback search/gap was recorded
- canonical Markdown Daily Note and date-folder assets committed
- no substantive prior content lost
- Durable Memory copy exists
- chunks generated without substantive loss
- currently approved index refresh succeeded where supported
- retrieval test returns the newly indexed source/package
- provenance retained
- unresolved gaps recorded

## 17. Principle

**Capture live in the open document. Recover the source and its files. Weave completely. Finalize once. Package by date. Commit the canonical record. Preserve completely. Retrieve selectively. Distill separately.**

## Current contract lifecycle and consultation requirements

The [HQ Global Memory Contract](../Global%20Memory%20Contract.md) governs this procedure.

- Default live Daily Note surface: agent/day Google Doc in the designated Google Drive Daily Notes folder when available.
- WDN writes update the live document only; they do not themselves authorize Git commits, finalization, promotion, or indexing.
- At end-of-day/finalization, recover all conversations and exposed execution context, weave the live document, preserve recoverable files through the attachment fallback ladder, verify completeness, export canonical Markdown/date package, then commit and promote.
- Preserve every recoverable episode and its attachments/files. Promote all content to Durable Memory independently of embedding eligibility or indexing success.
- Use the accepted America/New_York day boundary, retaining original timestamps/offsets and UTC. A two-finalized-note Recent window is a storage rule, distinct from rolling 48-hour bootstrap recall.
- When a third finalized note arrives, move the oldest into its calendar-month Daily Notes folder and update provenance pointers. Never delete source because indexing failed.
- Keep the current month and two preceding months uncompressed. Older complete monthly packages become eligible for lossless compression only after complete Durable Memory promotion and provenance verification. Verify archive inventory/integrity before removing redundant working copies.
- No exact yearly recompression trigger is approved. Retain monthly archives unchanged until Reg approves that trigger; approximately three months into the next year is context, not a schedule.
- Consult the maintained Compound Engineering source index in the XOS Paperclip How-To Hub, task XOS-20, document key `compound-engineering` before applying documented Compound Engineering procedures.
- The finalized Memory How-To Hub is in XOS Paperclip task XOS-21, document key `memory-how-to-hub`; its linked `memory-vector-procedure` records the selected implementation and verification limits.
- Opera capture remains validation-gated in XOS-15. Live promotion/indexing/retrieval acceptance remains in XOS-13. Documentation and a successful file comparison do not establish runtime success or contract lock enforcement.
