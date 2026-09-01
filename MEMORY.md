# MEMORY.md — XOS Headquarters Memory Contract

## Purpose

XOS memory exists to preserve continuity, evidence, decisions, obligations, learning, and the actual history of Reg's life and businesses.

Semantic retrieval helps find records. It is not the record itself.

## Required Memory Layers

### 1. Daily dirty notes

Path: `memory/YYYY-MM-DD.md`

Append meaningful activity chronologically. Dirty notes may be imperfect, but they must be timely and attributable.

Each entry should contain, when applicable:

- timestamp
- event or request
- people/agents/systems involved
- action or response
- result
- evidence/source
- disagreement/correction
- decision/resolution
- uncertainty
- blocker
- owed work
- tags or links

### 2. Structured event ledger

Append-only representation of material events. Corrections create new events referencing prior events; they do not silently overwrite history.

### 3. Durable memory

Distilled facts, preferences, procedures, lessons, and operating knowledge that remain useful beyond one day.

### 4. Decision register

For each decision:

- question
- options considered
- evidence
- decision
- authority
- effective time
- affected scope
- superseded decision, when applicable
- review trigger

### 5. Disagreement and resolution register

Preserve:

- subject
- participants
- each position
- evidence
- identified error or uncertainty
- resolution
- resulting work
- prevention rule
- unresolved points

### 6. Obligation ledger

Every owed item has:

- obligation ID
- source request
- owner
- status
- next action
- blocker
- due date or trigger when applicable
- completion evidence
- cancellation or obsolescence authority

Allowed statuses: captured, planned, in_progress, blocked, waiting, in_review, completed, cancelled, obsolete.

### 7. Semantic index

Embeddings and retrieval indexes point to authoritative source records. Store provenance, timestamps, record type, subject tags, and supersession relationships.

OpenAI's embedding workflow and PGVector are candidates for controlled A/B testing. No candidate becomes canonical solely because it is newer or supplied by OpenAI.

## Capture Rule

Capture every meaningful event first. Distillation happens later.

Do not rely on the model to remember to remember. Event capture must become automatic wherever technically possible.

## Promotion Rule

Promotion never destroys the source. A dirty note may produce an event, decision, obligation, durable memory, SOP update, or canon candidate while remaining part of the historical record.

## Retrieval Rule

Retrieval ranking may use semantic similarity, recency, importance, relationship, source authority, and explicit links. A high semantic score does not override higher-authority canon or stronger evidence.

## Privacy and Secrets

Do not place passwords, API keys, authentication tokens, recovery codes, or unnecessarily sensitive raw data into ordinary memory files. Store references to approved secret locations instead.

## Minimum End-of-Turn Check

Before ending meaningful work, determine:

1. What happened?
2. What changed?
3. What was decided?
4. What remains owed?
5. What failed or became blocked?
6. What evidence exists?
7. What must be retrievable later?
