# XOS-HQ-HOWTO-MEMORY-SYSTEM-OPERATION.md
**Version:** 2026-09-14
**Authority:** HQ

## 1. Purpose

Define how to operate the XOS memory system in practice: live Daily Notes, verbatim recovery, daily finalization, exhaustive episodic promotion, chunking, embedding, semantic indexing, retrieval, and recovery from missing memory.

## 2. Governing Model

**Preservation is exhaustive. Retrieval is selective.**

Do not decide during capture or episodic promotion what will matter later. Preserve the recoverable substantive episode first. Relevance ranking belongs to retrieval and distilled-memory layers.

## 3. Daily Execution

For every meaningful turn, action, decision, correction, blocker, failure, recovery, tool action, external interaction, or changed understanding:

1. perform or answer the current work
2. append operational context to the active Daily Note when needed
3. preserve source evidence in the correct lane
4. place outputs correctly
5. do not discard material because it appears unimportant

Use the repo-local Daily Note path defined by that agent's memory contract. Append chronologically with precise timestamps.

`WDN` means write the current operational state to the active Daily Note immediately through the available persistent write path. A chat acknowledgment without a persistent write is not completion.

## 4. What Daily Notes Add

Daily Notes preserve information a verbatim transcript may not contain: tool calls and material results, system/file/config changes, success/failure/partial state, corrections, decisions, blockers, dependencies, handoffs, unresolved state, and concise judgment summaries.

Do not treat Daily Notes as a substitute for the complete verbatim episode.

## 5. Verbatim Recovery

When conversation history or another episodic source is available:

1. capture the complete recoverable episode
2. preserve original timestamps and speaker attribution when available
3. retain corrections, mistakes, tangents, topic changes, and incidental material
4. do not select only material presently judged useful
5. record provenance such as conversation/thread/source URL or file when available
6. mark gaps rather than inventing missing text

## 6. Daily Finalization / Weave

At finalization for a date:

1. open the existing Daily Note
2. gather all recoverable verbatim episodes for that date
3. order source material chronologically by timestamp
4. weave the verbatim chronology with operational Daily Note material
5. clearly distinguish verbatim source from agent-authored operational narration
6. preserve tool/system context not visible in the transcript
7. record unresolved gaps
8. save the final Markdown Daily Note

Do not omit an episode merely because it appears repetitive, humorous, off-topic, mistaken, or low-value.

## 7. Exhaustive Episodic Promotion

After source chronology is preserved:

1. promote the complete substantive episodic record into the repo's `Durable_Memory/` lane
2. retain provenance and chronology
3. normalize metadata as needed
4. suppress only exact technical duplicates when no substantive information is lost
5. preserve earlier incorrect states alongside later corrections when they are part of the episode
6. do not apply a usefulness qualification gate to episodic preservation

Distilled Lessons are separate and may be selective. They never replace Durable Memory.

## 8. Chunking and Semantic Indexing

After durable preservation:

1. chunk the preserved corpus at useful semantic boundaries without dropping substantive content
2. retain source IDs, timestamps, and provenance on chunks where supported
3. generate vector embeddings using the approved embedding workflow
4. upsert chunks into the applicable semantic/vector index
5. verify the indexing run completed successfully
6. preserve source files even when embedding/indexing fails
7. retry downstream processing without requiring source recapture

The vector store exists so future searches can surface details whose importance was unknowable when captured.

## 9. Retrieval

Retrieval may be selective. Use semantic search, metadata filters, recency, source provenance, exact text search, and other ranking mechanisms to return the material relevant to the current question.

Do not confuse selective retrieval with selective preservation.

## 10. Recovery When Memory Is Missing

When expected Daily Notes, transcripts, Durable Memory, or contract material is absent:

1. report the gap immediately
2. search agent repo, HQ/Canon, conversation history, available files, connectors, Paperclip, commits, external evidence, and other authorized sources
3. recover verbatim source where possible
4. preserve timestamps/provenance
5. reconstruct chronology without invention
6. finalize the affected Daily Note
7. promote the recovered episode into Durable Memory
8. chunk/embed/index it
9. verify the downstream job
10. record anything still missing

## 11. Bootstrap Memory Load

At startup, follow the agent's bootstrap documents. Load the required recent Agent Recall window. If required files are missing, bootstrap is incomplete; state the blocker and use the maximum verified continuity available while the defect is repaired.

## 12. Evidence and Supersession

Evidence beats belief. Newer verified understanding may supersede older understanding without deleting old evidence. Preserve corrections as corrections, not silent rewrites of history.

## 13. Failure Handling

If capture fails on a minor action, use the best available fallback as soon as possible. If capture fails on a critical/system-changing action, preserve evidence and stop when necessary to prevent loss.

If promotion, chunking, embedding, or indexing fails, the source remains authoritative and preserved. Retry downstream processing later.

## 14. Completion Check

Memory work is complete only when the required source is preserved and the requested downstream operation is either verified complete or explicitly reported blocked.

For promotion work, verify:

- source chronology preserved
- Daily Note finalized when applicable
- Durable Memory copy exists
- chunks generated without substantive loss
- embeddings/index refresh succeeded where supported
- provenance retained
- unresolved gaps recorded

## 15. Principle

**Capture first. Preserve completely. Retrieve selectively. Distill separately. Never throw away the source because today's agent cannot predict tomorrow's question.**
