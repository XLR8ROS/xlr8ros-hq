**Learn once. Forget nothing. Remember everything. Because everything has value.**

# Global Memory Contract

**Authority:** XOS HQ
**Status:** Authoritative memory contract
**Effective:** 2026-09-14

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

### 3.2 Verbatim Episodic Record

Recovered or directly captured conversation episodes, transcripts, messages, external interactions, and other source chronology are preserved in full when available.

Do not curate, summarize away, or drop material because it appears trivial, repetitive, humorous, off-topic, mistaken, or presently useless.

Corrections, wrong turns, topic shifts, failed assumptions, and seemingly incidental details remain part of the episode.

### 3.3 Durable Memory

Durable Memory is the persistent episodic corpus used for long-term continuity.

For complete episodic promotion, the underlying source record is preserved exhaustively. Durable storage may normalize structure, attach provenance, deduplicate exact technical duplicates, split material into chunks, or add metadata, but it must not delete substantive source content merely because an agent predicts low future value.

### 3.4 Distilled Lessons

Distilled Lessons are a separate selective layer derived from preserved evidence. They may summarize recurring patterns, procedures, failures, preferences, decisions, and lessons.

Distillation never replaces the underlying episodic record.

## 4. Capture Rule

Capture comes before classification, weighting, distillation, or promotion.

Every meaningful turn, action, tool call, correction, decision, blocker, failure, recovery, output, external interaction, and changed understanding must be captured before it disappears from operational context.

A completed action without traceable memory is operationally incomplete.

## 5. WDN Rule

`WDN` is an explicit instruction to write a timestamped Daily Note entry immediately through the available persistent write path.

A valid WDN entry records the current operational state, what changed, what was learned, tool activity and outcomes, corrections, decisions, unresolved state, and context that may not be recoverable from the raw transcript alone.

Saying that WDN was triggered without persisting the entry does not satisfy the instruction.

## 6. Daily Finalization and Verbatim Weave

When a day's verbatim conversation material is available, the final Daily Note for that date should weave together:

1. the existing operational Daily Note entries
2. recovered timestamped verbatim conversation episodes
3. tool and system state not visible in the transcript
4. corrections, blockers, decisions, and unresolved work

Preserve chronology. Clearly distinguish verbatim/recovered source material from agent-authored operational narration.

Do not selectively omit episodes from the final source chronology based on present usefulness judgments.

## 7. Promotion Rule

The complete recoverable episodic source is eligible for promotion into Durable Memory.

Promotion is not a relevance contest. The promotion process must preserve the complete substantive episode while adding structure needed for retrieval.

Permitted promotion operations include:

- timestamp normalization
- source and provenance metadata
- speaker/agent attribution
- exact-duplicate suppression when no substantive information is lost
- chunking
- vector embedding
- indexing
- cross-linking to Daily Notes, files, tasks, commits, and external evidence
- supersession metadata without deleting historical evidence

Promotion must not remove substantive content because an agent thinks it is currently unimportant.

## 8. Chunking, Embeddings, and Retrieval

After preservation and promotion, durable episodic material should be chunked at useful semantic boundaries, vector embedded where supported, and added to the applicable semantic index.

Search and retrieval may be selective, ranked, filtered, weighted, or context-limited. This selectivity belongs at retrieval time, not preservation time.

The purpose of semantic indexing is to allow future queries to surface details whose relevance could not have been predicted when the episode occurred.

## 9. Provenance and Supersession

Memory must preserve source provenance whenever available, including date/time, conversation or session identity, file path, commit, task, external source, and tool evidence.

Newer verified understanding may supersede older understanding without erasing the older evidence.

Corrections should preserve both the earlier state and the corrected state when doing so helps reconstruct what happened and why.

## 10. Bootstrap Recall

At startup, each XOS agent must follow its agent bootstrap sequence and load the most recent 48 hours of Agent Recall according to the available Daily Notes and durable memory sources.

If expected memory material is missing, the agent must state the gap explicitly and continue with the maximum verified continuity available rather than silently pretending the bootstrap is complete.

## 11. Recovery of Missing Memory

When missing Daily Notes, transcripts, or episodic records are discovered:

1. search available conversation history, repositories, files, connectors, shared links, task systems, and other evidence surfaces
2. recover source material verbatim when possible
3. preserve timestamps and provenance
4. reconstruct chronology without inventing missing content
5. promote the recovered episode into the durable episodic corpus
6. chunk, embed, and index it where supported
7. record unresolved gaps explicitly

## 12. Contract Copies

The authoritative Global Memory Contract is maintained in XOS HQ canon.

Agent repositories that require a locked local contract copy must contain an exact local copy unless a later governing rule defines a synchronization mechanism.

If an agent's bootstrap requires a local contract and that file is missing, stale, or only a placeholder, bootstrap is incomplete until the defect is reported and repaired.

## 13. Separation of Memory Layers

Do not collapse the following into one artifact:

- verbatim episodic source
- Daily Notes / operational Agent Recall
- Durable Memory corpus
- Distilled Lessons
- Canon, SOPs, and How-Tos

Each layer has a different purpose. Higher-order summaries and doctrine may be selective. The underlying episodic evidence remains preserved.

## 14. Failure Handling

If memory capture fails on a minor action, preserve the event through the best available fallback as soon as possible.

If capture fails on a critical or system-changing action, stop before continuing when necessary to prevent loss of evidence, preserve what is available, report the blocker, and repair the capture path.

If promotion or embedding fails, do not discard the source. Preserve the source first and retry downstream processing later.

## 15. Governing Rule

When in doubt between preserving and discarding substantive episodic material, preserve it.

**Learn once. Forget nothing. Remember everything. Because everything has value.**
