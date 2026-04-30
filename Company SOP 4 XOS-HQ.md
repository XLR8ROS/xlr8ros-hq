# XOS Nightly Report — How-To (Operational Procedure)
Version: 2026-04-30

## Purpose
This document defines how the XOS nightly report is generated, validated, and stored.

The goal is to guarantee:
- zero silent work
- full system visibility
- daily compounding of knowledge

---

## 1. Trigger (When it runs)

The nightly report is executed via scheduled job (cron or equivalent).

Minimum requirement:
- runs once every 24 hours
- runs at a fixed time (recommended: late-night local time)

Example schedule:
- daily at 23:55 local time

---

## 2. Execution Flow (What happens)

The nightly process must run in this exact order:

### Step 1 — Health Check
Collect system health data:

- OpenClaw status
- gateway status
- active services
- database availability (e.g., SQLite, Qdrant)
- API/provider status

Output:
→ health snapshot

---

### Step 2 — Activity Scan
Pull all activity from the last 24h:

- event log (SQLite)
- session logs / notes
- task execution traces
- agent actions

Output:
→ raw activity set

---

### Step 3 — Reporting Gap Detection
Check for missing reporting:

- actions with no report
- sessions with no closure
- logs without interpretation

If any found:
- flag as REPORTING GAP
- include in final report

---

### Step 4 — Blocker Extraction
Identify all blockers:

- unresolved blockers from prior cycles
- new blockers introduced today

Each blocker must include:
- source
- current status
- impact level

---

### Step 5 — State Reconstruction
Build current system state:

- what is complete
- what is active
- what is stalled
- what is inconsistent

This is NOT a log dump.
This is interpreted state.

---

### Step 6 — Compounding Capture
Extract reusable value:

- new patterns
- validated procedures
- fixes that should be reused
- anything that reduces future effort

If nothing is captured:
→ explicitly state: "NO NEW COMPOUNDING OUTPUT"

---

### Step 7 — Integrity Check
Ask and answer:

“Did anything happen without a trace?”

If YES:
- mark as SYSTEM FAILURE CONDITION
- list missing trace areas

---

### Step 8 — Next-State Projection
Define:

- what happens next
- what must be prioritized
- what requires escalation

---

## 3. Report Format (Required Structure)

The nightly report must follow this exact structure:

### 1. System Health
- summary of all system components

### 2. Activity Summary
- high-level description of work performed

### 3. Blockers
- list all blockers (new + existing)

### 4. Reporting Gaps
- list all missing or incomplete reporting

### 5. State Summary
- current system state (complete / active / stalled)

### 6. Compounding Output
- reusable artifacts, patterns, or knowledge

### 7. Integrity Check
- result of no-silence validation

### 8. Next Actions
- prioritized next steps

---

## 4. Storage Rules

Each report must be saved as:

/maintenance/nightly-reports/YYYY-MM-DD.md

Additionally:

- summary version → sent via Telegram (or primary comms)
- full version → stored in repo or system storage

---

## 5. Failure Handling

If the nightly job fails:

- log failure immediately
- run recovery execution as soon as detected
- generate report retroactively if possible

Failure to produce a nightly report = system failure.

---

## 6. Minimum Output Standard

A valid nightly report must:

- cover all 8 sections
- contain no empty critical sections (health, blockers, state)
- explicitly state when something is missing (not omit it)

---

## 7. Completion Condition

The nightly process is only complete when:

1. report is generated
2. report is stored
3. report is communicated (summary or full)
4. no-silence check is executed

If any step is missing → nightly cycle is incomplete