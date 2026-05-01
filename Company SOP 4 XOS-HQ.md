# XOS HQ SOP — OPERATIONS & CONTROL  
**Version:** 2026-04-30 20:30 EST  
**Authority:** HQ (Highest)  

---

## 1. PURPOSE  
Define how XOS operates at the HQ level.  
This SOP governs behavior, enforcement, logging, and system discipline across all divisions, agents, and workflows.

---

## 2. CORE RULE  
**Work is not complete until it is logged.**

Enforcement occurs at three choke points:  
- End-of-action checkpoint  
- Session boundary checkpoint  
- Nightly pressure test  

Reference:  
XOS Nightly Report — How-To.MD  

---

## 3. EXECUTION STANDARD  

### 3.1 Immediate Correspondence Rule  
- If blocked → report immediately  
- Do not continue silently  

Reference:  
AGENT PHASE REPORTING HOW-TO.md  

---

### 3.2 Blocker-First Reporting  
- First line of any report must state the blocker (if present)  

Reference:  
AGENT PHASE REPORTING HOW-TO.md  

---

### 3.3 Root Cause Rule  
- Do not apply fixes blindly  
- Identify root cause before correction  

---

## 4. LOGGING SYSTEM  

All actions must produce traceable output across:

- Event Log (SQLite)  
- Session Notes  
- Output Logs  
- Nightly Report  

Failure to log = failure of execution.

Reference:  
XOS Nightly Report — How-To.MD  

---

## 5. NIGHTLY ENFORCEMENT  

Nightly cron must:  
- Review all activity  
- Identify missing logs  
- Promote valid memory  
- Produce summary report  

Reference:  
XOS Nightly Report — How-To.MD  

---

## 6. HOW-TO SEPARATION RULE  

SOP = tells what must be done  
HOW-TO = tells how to do it  

SOP must NEVER contain procedural steps.  
All execution details are externalized.

Reference:  
NAVIGATION_HOWTO.md  

---

## 7. HQ HOW-TO REFERENCES  

The following HQ-level HOW-TOs define execution:

- GitHub Access  
  → XOS-HQ-HOWTO-GITHUB-ACCESS.md  

- Agent Origination  
  → AGENT_ORIGINATION_HOWTO.md  

- Navigation System  
  → NAVIGATION_HOWTO.md  

- Registry System  
  → REGISTRY_HOWTO.md  

- Project Budgeting  
  → Agent Project Budget Proposal How-To.md  

- Phase Reporting  
  → AGENT PHASE REPORTING HOW-TO.md  

- Nightly Reporting  
  → XOS Nightly Report — How-To.MD  

- Sub-Agent Spawning  
  → Codi How-To Spawn Sub-Agents.md  

---

## 8. CROSS-SYSTEM RULE  

Lower systems (SEAD, agents, repos):  
- MUST NOT duplicate HOW-TOs  
- MUST reference HQ documents instead  

Format:

Reference:  
XOS-HQ-HOWTO-<NAME>.md  

Reference:  
NAVIGATION_HOWTO.md  

---

## 9. VERSION CONTROL RULE  

- Every SOP must include timestamp  
- Newer versions override older ones  
- No parallel conflicting SOPs allowed  

Reference:  
REGISTRY_HOWTO.md  

---

## 10. FAILURE DEFINITION  

A failure occurs if:  
- Work is done without a trace  
- Logging is skipped  
- Duplicate instructions exist across systems  
- Root cause is ignored  

---

## 11. SYSTEM PRINCIPLE  

Do not ask:  
“Was this important enough to log?”  

Ask:  
“Did anything happen without a trace?”  

---

**END OF SOP**