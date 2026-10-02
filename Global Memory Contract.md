Learn once, forget nothing, remember everything, because everything has value.

# Global Memory Contract

**Authority:** XOS HQ
**Status:** Authoritative memory contract
**Effective:** 2026-09-14
**Revised:** 2026-09-16

## 1. Purpose

This contract defines the memory obligations for XOS agents and memory-capable systems. Its purpose is to preserve operational continuity across conversations, models, runtimes, devices, infrastructure, assignments, and time.

## 2. Core Principle

Preservation is exhaustive. Retrieval is selective.

XOS agents must not decide at capture or episodic-promotion time that a detail is unimportant merely because its future value is not presently obvious. Future relevance is unknown by definition.

The complete recoverable episodic record is preserved first. Search, ranking, filtering, summarization, distillation, and weighting happen later.

## 3. Required Memory Layers

### 3.1 Daily Notes / Agent Recall

Daily Notes preserve the live operational layer that may not be visible from a future verbatim transcript alone, including:

- tool calls and material results
- file, connector, workflow, configuration, and system changes
- successes, failures, partial success, and unverified state
- corrections from Reg
- decisions, blockers, state transitions, dependencies, and handoffs
- concise reasoning and judgment summaries that are safe to preserve
- material context carried forward by the agent

Daily Notes are chronological and timestamped precisely whenever reliable time is available.

During an active day, the default live Daily Note surface is an editable Google Doc in the agent's designated Daily Notes Google Drive folder when that surface is available. The live Google Doc is a working operational artifact, not the finalized repository record.

Each agent/day should use one clearly identified live Daily Note document for that date unless a documented recovery or tooling constraint requires another structure. The live document may contain operational WDN entries, recovered verbatim, working weave material, source links, and media references while the day remains open.

### 3.2 Verbatim Episodic Record

Recovered or directly captured conversation episodes, transcripts, messages, external interactions, and other source chronology are preserved in full when available.

Do not curate, summarize away, or drop material because it appears trivial, repetitive, humorous, off-topic, mistaken, or presently useless.

Corrections, wrong turns, topic shifts, failed assumptions, and seemingly incidental details remain part of the episode.

### 3.3 Durable Memory

Durable Memory is the persistent episodic corpus used for long-term continuity.

For complete episodic promotion, the underlying source record is preserved exhaustively. Durable storage may normalize structure, attach provenance, deduplicate exact technical duplicates, split material into chunks, or add metadata, but it must not delete substantive source content merely because an agent predicts low future value.

### 3.4 Distilled Lessons

Distilled Lessons are a separate selective layer derived from preserved evidence. They may summarize recurring patterns, procedures, failures, preferences, decisions, and lessons.

Distillation is an optional, selective Compound Engineering-derived layer. It never determines whether source memory survives and never replaces the underlying episodic record.

Consult the authoritative Compound Engineering documentation and runtime SKILL.md procedures through the XOS How-To Hub when episodic evidence can inform reusable lessons, patterns, solutions, or concepts, including evidence retrieved months later. Maintain provenance from distilled knowledge to Durable Memory. The Memory How-To Hub must point to these maintained procedures; stale copied paraphrases are not current authority.

## 4. Capture Rule

Capture comes before classification, weighting, distillation, or promotion.

Every recoverable turn, action, tool call, correction, decision, blocker, failure, recovery, output, external interaction, and changed understanding must be captured before it disappears from operational context.

A completed action without traceable memory is operationally incomplete.

## 5. WDN Rule

`WDN` is an explicit instruction to write a timestamped Daily Note entry immediately into the active live Daily Note.

When the designated Google Drive Daily Notes surface is available, WDN writes go to that day's working Google Doc. A WDN write must not create or update the finalized repository Markdown Daily Note, create a Git commit, finalize the day, promote Durable Memory, or trigger downstream indexing merely because the note was written.

If the designated Google Doc surface is unavailable, use the best available non-destructive persistent fallback and record the deviation. A storage mechanism that necessarily commits or finalizes the repository record on every WDN append is not the normal live WDN path.

A valid WDN entry records the current operational state, what changed, what was learned, tool activity and outcomes, corrections, decisions, unresolved state, and context that may not be recoverable from the raw transcript alone.

Saying that WDN was triggered without persisting the entry does not satisfy the instruction.

## 6. Daily Finalization and Verbatim Weave

For each agent/day, the live Daily Note remains open throughout the active day. At the designated finalization stage, the agent must gather all recoverable material for that date and weave it into the live document before producing the canonical repository record.

The final Daily Note must weave all available verbatim communications and operational records into one timestamped chronological record, including:

1. the existing operational Daily Note entries
2. recovered timestamped verbatim conversation episodes
3. tool and system state not visible in the transcript
4. corrections, blockers, decisions, and unresolved work
5. interactions with Reg, other agents/entities, computers, tools, and any other recoverable record
6. attachments, photos, audio, video, files, and other media with their source references preserved with the Daily Note package
7. exposed execution disclosures such as tool-result summaries, `Worked for ...`, or other visible execution context when recoverable from the user-facing interface

Preserve chronology. Clearly distinguish verbatim/recovered source material from agent-authored operational narration.

Do not selectively omit episodes from the final source chronology based on present usefulness judgments.

After the live document has been woven and verified, export or reproduce its complete finalized content as the canonical Markdown Daily Note in the agent repository. That repository Markdown artifact is the committed finalized Daily Note. The working Google Doc is the live authoring and inspection surface; the repository Markdown file is the canonical finalized storage representation.

Finalization must verify that no substantive information present in the working document or prior canonical Daily Note is lost. Exact technical duplicates may be suppressed when no substantive information is lost.

## 7. Promotion Rule

EVERYTHING recoverable is promoted into Durable Memory. There is no usefulness or relevance gate for promotion; Durable Memory is the complete preserved episodic record.

Promotion occurs after the Daily Note has been woven, verified, and finalized into the canonical repository record unless an approved recovery procedure explicitly requires otherwise.

Promotion is not a relevance contest. The promotion process must preserve the complete substantive episode while adding structure needed for retrieval.

Permitted promotion operations include:

- timestamp normalization
- source and provenance metadata
- speaker/agent attribution
- exact-duplicate suppression when no substantive information is lost
- chunking
- vector embedding
- indexing
- cross-linking to Daily Notes, files, tasks, commits, external evidence, and media assets
- supersession metadata when understanding actually changes, without deleting historical evidence

Promotion must not remove substantive content because an agent thinks it is currently unimportant.

## 8. Chunking, Embeddings, and Retrieval

After weaving/finalization, the canonical Daily Note is chunked at useful semantic boundaries. All embeddable material, including supported text, file, image, audio, video, and other media representations, is embedded and indexed. The complete source is preserved and promoted into Durable Memory regardless of embedding eligibility or indexing success.

Source preservation and retrieval indexing are separate concerns. Chunks, embeddings, and indexes never replace the complete preserved source.

Search and retrieval may be selective, ranked, filtered, weighted, or context-limited. This selectivity belongs at retrieval time, not preservation time.

The purpose of semantic indexing is to allow future queries to surface details whose relevance could not have been predicted when the episode occurred.

## 9. Provenance, Expansion, and Supersession

Memory must preserve source provenance whenever available, including date/time, conversation or session identity, live Google Doc identity, repository file path, commit, task, external source, media asset path, and tool evidence.

When later recovery only adds detail, depth, verbatim, media, timestamps, provenance, or execution context without changing the earlier substantive understanding, treat it as additive expansion, not supersession. Weave the older substantive content into the richer canonical artifact, verify completeness, and then remove redundant containers when appropriate without deleting unique information.

Newer verified understanding may supersede older understanding when the meaning or conclusion actually changes. Supersession does not erase older evidence.

Corrections should preserve both the earlier state and the corrected state when doing so helps reconstruct what happened and why.

## 10. Bootstrap Recall

At startup, each XOS agent must follow its agent bootstrap sequence and load the most recent 48 hours of Agent Recall according to the available Daily Notes and durable memory sources.

For an open current-day Daily Note, the live Google Doc is a valid Agent Recall source. For finalized prior days, the canonical repository Markdown and Durable Memory are the authoritative preserved representations.

If expected memory material is missing, the agent must state the gap explicitly and continue with the maximum verified continuity available rather than silently pretending the bootstrap is complete.

## 11. Recovery of Missing Memory

When missing Daily Notes, transcripts, or episodic records are discovered:

1. search available conversation history, repositories, Google Drive Daily Note documents, files, connectors, shared links, task systems, and other evidence surfaces
2. recover source material verbatim when possible
3. preserve timestamps and provenance
4. reconstruct chronology without inventing missing content
5. weave recovered material into the applicable working/final Daily Note
6. promote the recovered episode into the durable episodic corpus after finalization
7. chunk, embed, and index it where supported
8. record unresolved gaps explicitly

## 12. Contract Copies

The authoritative Global Memory Contract is maintained in XOS HQ canon.

Agent repositories that require a locked local contract copy must contain an exact local copy unless a later governing rule defines a synchronization mechanism.

Agent-local identity, copy status, synchronization receipts, and lock metadata must remain in a separate file outside this governing text. Synchronization must verify complete textual equality, including the exact motto at the beginning and end. A label saying 'locked' is not proof of technical enforcement; verify the actual protection mechanism.

If an agent's bootstrap requires a local contract and that file is missing, stale, or only a placeholder, bootstrap is incomplete until the defect is reported and repaired.

## 13. Separation of Memory Layers

Do not collapse the following into one artifact:

- live working Daily Note Google Doc
- verbatim episodic source
- finalized canonical Daily Note Markdown
- Durable Memory corpus
- Distilled Lessons
- Canon, SOPs, and How-Tos

These artifacts may be woven or transformed into one another at designated lifecycle stages, but their roles are distinct. The live Google Doc is the active working surface. The finalized repository Markdown is the canonical closed Daily Note. Durable Memory is the long-term episodic preservation layer. Higher-order summaries and doctrine may be selective. The underlying episodic evidence remains preserved.

## 14. Failure Handling

If memory capture fails on a minor action, preserve the event through the best available fallback as soon as possible.

If capture fails on a critical or system-changing action, stop before continuing when necessary to prevent loss of evidence, preserve what is available, report the blocker, and repair the capture path.

If the live Google Doc path fails, preserve the active note in another non-destructive working surface and record the deviation. Do not silently switch to a per-WDN repository commit pattern.

If promotion or embedding fails, do not discard the source. Preserve the source first and retry downstream processing later.

## 15. Daily Note Storage Lifecycle

During the active day, the working Daily Note remains in the agent's designated Google Drive Daily Notes folder. It may remain there after finalization as a readable working/history copy, but the canonical finalized Daily Note is the repository Markdown artifact.

Keep a rolling window of two finalized Daily Notes in Recent (approximately 48 hours). When a third finalized note is added, move the oldest into its calendar month's Daily Notes folder; do not delete it. A 72-hour window requires a separate explicit change.

Keep the current month plus the two immediately preceding months of Daily Notes uncompressed. When a new month makes an older month the fourth in the rolling set, compress that complete monthly folder losslessly and archive it under that calendar year's Daily Notes archive.

After the year is sufficiently past (approximately three months into the next year), the prior year's archived Daily Notes may be packaged into a lossless yearly archive. The exact annual trigger must be specified in the approved How-To; it is not fixed by this contract.

Daily Notes and ordinary source files become eligible for compression only after their complete content has been promoted into Durable Memory and preservation/provenance has been verified. Verify archive integrity before removing redundant working copies. Failed promotion or verification preserves the source and creates a retry/blocker record.

Durable Memory is the protected preservation layer and is not subject to destructive compression or loss. Compression and archival must never destroy Durable Memory, delete source content, or break provenance and pointers needed to recover the original episode.

## 16. Governing Rule

When in doubt between preserving and discarding substantive episodic material, preserve it.

Learn once, forget nothing, remember everything, because everything has value.
