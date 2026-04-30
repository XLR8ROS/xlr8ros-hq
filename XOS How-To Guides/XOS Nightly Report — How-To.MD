# XOS Nightly Report — How-To
Timestamp: 2026-04-30

## Purpose
Ensure every 24-hour cycle produces a complete, verified, and interpretable system report.

The nightly report eliminates silent work and enforces system visibility.

---

## 1. Schedule (Trigger)

Run once every 24 hours via cron or scheduler.

Recommended:
- Time: 23:55 local
- Must run automatically (no manual trigger dependency)

---

## 2. Execution Steps

Follow this exact sequence:

### Step 1 — System Health
Collect:

- OpenClaw status  
- Gateway status  
- Active services  
- Database status (SQLite, Qdrant, etc.)  
- API/provider health  

---

### Step 2 — Activity Collection
Pull last 24h data:

- Event log (SQLite)  
- Session notes / logs  
- Agent actions  
- Task execution traces  

---

### Step 3 — Reporting Gap Check
Detect:

- actions without reports  
- sessions without closure  
- logs without interpretation  

If found:
→ mark as REPORTING GAP

---

### Step 4 — Blocker Identification
List:

- unresolved blockers  
- new blockers  

Each must include:
- source  
- status  
- impact  

---

### Step 5 — State Build
Construct current system state:

- completed work  
- active work  
- stalled work  
- inconsistencies  

(No raw logs. Interpreted state only.)

---

### Step 6 — Compounding Capture
Extract reusable value:

- patterns  
- fixes  
- procedures  
- artifacts  

If none:
→ explicitly state: NONE

---

### Step 7 — Integrity Check
Answer:

“Did anything happen without a trace?”

If YES:
→ flag SYSTEM FAILURE

---

### Step 8 — Next Actions
Define:

- next priorities  
- required interventions  
- escalation items  

---

## 3. Report Format

Every report must include:

1. System Health  
2. Activity Summary  
3. Blockers  
4. Reporting Gaps  
5. State Summary  
6. Compounding Output  
7. Integrity Check  
8. Next Actions  

---

## 4. Storage

Save as:

/maintenance/nightly-reports/YYYY-MM-DD.md

Also:

- send summary via primary comms (Telegram)
- keep full report in system storage

---

## 5. Failure Handling

If job fails:

- log failure  
- rerun ASAP  
- generate report retroactively if possible  

Missing nightly report = system failure.

---

## 6. Completion Rule

Nightly cycle is complete only if:

1. report generated  
2. report stored  
3. report communicated  
4. integrity check executed  

If any are missing → cycle incomplete