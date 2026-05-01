# XOS-HQ-HOWTO-MEMORY-SYSTEM-OPERATION.md  
**Version:** 2026-05-01  
**Authority:** HQ  

---

## 1. PURPOSE  

Define how to operate the XOS memory system in practice, including daily logging, session handling, event capture, and nightly audit execution.

---

## 2. DAILY EXECUTION  

### 2.1 During Work  

For every meaningful action:

1. Perform the action  
2. Ensure it passes through the wrapper (automatic event logging)  
3. Confirm output is placed correctly:
   - outputs/ for artifacts  
   - sessions/YYYY/MM/ for session logs  

---

### 2.2 Session Handling  

At session end:

1. Open or create session log:
   `sessions/YYYY/MM/<session-id>.md`  

2. Record:
   - objective  
   - actions taken  
   - decisions  
   - blockers  
   - outputs  

3. Save log before session close  

---

## 3. EVENT LOGGING  

Automatic logging:

- occurs via wrapper  
- writes to:
  `memory/sqlite/events.sqlite`  

If logging fails:

- Minor action:
  → immediately log using fallback procedure  

- Critical/system-changing action:
  → STOP  
  → do not proceed  

---

## 4. NIGHTLY AUDIT  

Create one file:

`maintenance/nightly-reports/YYYY-MM-DD.md`

---

### Required Sections

#### Sources Checked
- event log  
- session logs  
- daily notes / MEMORY.md  
- outputs  

#### Candidates Listed
- promotion candidates derived from sources  

#### Missing Sources
- explicitly list any missing sources  
- if none: state "None"  

---

## 5. PROMOTION RULES  

- Every candidate MUST include source reference  
- No source reference = invalid candidate  

---

## 6. READINESS CHECK  

System is READY only if:

- all sources exist  
- session logs exist  
- automatic logging is working  
- audit is complete  

If any fail:

- mark NOT READY  
- continue logging anyway  

---

## 7. FAILURE HANDLING  

If something breaks:

- log it immediately  
- do not hide missing logs  
- do not bypass system rules  

---

## 8. PRINCIPLE  

Do not ask:

“Did I log enough?”  

Ask:

“Did anything happen without a trace?”  

---