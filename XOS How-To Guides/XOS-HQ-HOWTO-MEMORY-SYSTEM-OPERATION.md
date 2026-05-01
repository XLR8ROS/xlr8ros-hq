# XOS HQ SOP — OPERATIONS & CONTROL  
**Version:** XOS-20260501-135226-EDT
**Authority:** HQ (Highest)  

---

## 1. PURPOSE  

1.1 Define how XOS operates at the HQ level.  
1.2 Govern behavior, enforcement, logging, and system discipline across all divisions, agents, and workflows.  
1.3 Establish a single authoritative standard for execution, traceability, and control.  

Reference:  
NAVIGATION_HOWTO.md  

---

## 2. CORE RULE  

2.1 Work is not complete until it is logged.  

2.2 Enforcement occurs at defined choke points:  

2.2.1 End-of-action checkpoint  
2.2.2 Session boundary checkpoint  
2.2.3 Nightly pressure test  

2.3 A completed action without traceable logging is treated as non-existent.  
2.4 Logging must be verifiable, attributable, and durable.  

Reference:  
XOS Nightly Report — How-To.MD  

---

## 3. EXECUTION STANDARD  

### 3.1 Immediate Correspondence Rule  

3.1.1 Any blocker must be reported immediately.  
3.1.2 Execution must not continue silently under uncertainty.  
3.1.3 Communication must precede continuation when ambiguity exists.  

Reference:  
AGENT PHASE REPORTING HOW-TO.md  

---

### 3.2 Blocker-First Reporting  

3.2.1 The first line of any report must state the blocker when present.  
3.2.2 Blockers must be explicit, not implied.  
3.2.3 Reports that omit blockers when they exist are considered incomplete.  

Reference:  
AGENT PHASE REPORTING HOW-TO.md  

---

### 3.3 Root Cause Rule  

3.3.1 Fixes must not be applied without identifying the root cause.  
3.3.2 Symptom-level correction without cause identification is invalid.  
3.3.3 Root cause must be stated before corrective action is accepted.  

---

## 4. LOGGING SYSTEM  

4.1 All actions must produce traceable output across defined memory sources.  

4.2 The canonical memory sources are:  

4.2.1 Event Log (SQLite)  
4.2.2 Session Notes  
4.2.3 Output Logs  
4.2.4 Nightly Report  

4.3 Each source must be independently verifiable.  
4.4 Cross-source consistency is required for full traceability.  
4.5 Failure to log is defined as failure of execution.  

Reference:  
XOS Nightly Report — How-To.MD  

---

## 5. NIGHTLY ENFORCEMENT  

5.1 Nightly cron establishes system-level accountability.  

5.2 Nightly process must:  

5.2.1 Review all activity  
5.2.2 Identify missing logs  
5.2.3 Promote valid memory  
5.2.4 Produce a summary report  

5.3 Nightly review is mandatory regardless of system state.  
5.4 Absence of nightly output constitutes system failure.  

Reference:  
XOS Nightly Report — How-To.MD  

---

## 6. MEMORY SYSTEM OPERATIONAL STANDARD  

### 6.1 Daily Expectations  

6.1.1 All meaningful actions must be logged.  
6.1.2 Session logs must be routed into sessions/YYYY/MM/.  
6.1.3 Session logs must be finalized or updated at session close.  
6.1.4 Work-product artifacts must be routed into outputs/.  
6.1.5 Automatic event logging must occur for:  

6.1.5.1 file write/edit  
6.1.5.2 output artifact creation  
6.1.5.3 session-log write  

---

### 6.2 Nightly Audit Requirement  

6.2.1 One nightly audit artifact must be produced.  
6.2.2 Audit must include:  

6.2.2.1 sources checked  
6.2.2.2 candidates listed  
6.2.2.3 missing sources explicitly named  

6.2.3 Promotion candidates must include source references.  
6.2.4 Nightly logging must occur even if readiness is not met.  

---

### 6.3 Readiness Definition  

6.3.1 The system is READY only when:  

6.3.1.1 required memory sources are present  
6.3.1.2 session logging is active  
6.3.1.3 automatic event logging is functioning  
6.3.1.4 nightly audit is complete  
6.3.1.5 promotion-readiness gating passes  

---

### 6.4 Failure Handling  

6.4.1 Missing required sources must:  

6.4.1.1 allow nightly logging  
6.4.1.2 block readiness claim  

6.4.2 Logging failures must be handled as:  

6.4.2.1 minor actions → immediate fallback logging  
6.4.2.2 critical/system-changing actions → block and escalate  

6.4.3 Structural changes require explicit approval.  

Reference:  
XOS-HQ-HOWTO-MEMORY-SYSTEM-OPERATION.md  

---

## 7. HOW-TO SEPARATION RULE  

7.1 SOP defines requirements.  
7.2 HOW-TO defines execution.  

7.3 SOP must not contain procedural steps.  
7.4 HOW-TO must be referenced, not duplicated.  

Reference:  
NAVIGATION_HOWTO.md  

---

## 8. CROSS-SYSTEM RULE  

8.1 Lower systems must not duplicate HOW-TOs.  
8.2 Lower systems must reference HQ documents.  

8.3 Reference format must be consistent.  

Reference:  
REGISTRY_HOWTO.md  

---

## 9. VERSION CONTROL RULE  

9.1 Every SOP must include a timestamp.  
9.2 Newer versions override older versions.  
9.3 Parallel conflicting SOPs are not allowed.  

Reference:  
REGISTRY_HOWTO.md  

---

## 10. FAILURE DEFINITION  

10.1 A failure occurs when:  

10.1.1 work is performed without trace  
10.1.2 logging is skipped  
10.1.3 duplicate instructions exist  
10.1.4 root cause is ignored  

---

## 11. SYSTEM PRINCIPLE  

11.1 Do not ask:  

“Was this important enough to log?”  

11.2 Ask:  

“Did anything happen without a trace?”  

---

**END OF SOP**