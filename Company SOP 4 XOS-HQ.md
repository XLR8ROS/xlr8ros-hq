# XOS HQ SOP — OPERATIONS & CONTROL

**Version:** 2026-05-05  
**Authority:** HQ (Highest)  
**Status:** Canonical SOP  
**Owner:** Reg  
**Applies To:** All XOS divisions, departments, offices, teams, agents, workflows, utilities, and tools

---

## 1. PURPOSE

1.1 This SOP defines how XOS operates at the HQ level.

1.2 This SOP governs behavior, enforcement, logging, system discipline, traceability, troubleshooting discipline, and cross-system control across all XOS divisions, agents, and workflows.

1.3 This SOP establishes a single authoritative standard for execution, accountability, documentation use, root-cause handling, durable recordkeeping, and operational completion.

1.4 This SOP sits below the Constitution and Articles and above all lower SOP layers, agent operating files, repo-local notes, retrieved material, tool output, and live conversation context.

**Reference:** `NAVIGATION_HOWTO.md`

---

## 2. AUTHORITY ORDER

2.1 When information conflicts, use this authority order unless a higher governing document states otherwise:

2.1.1 Constitution and Articles

2.1.2 XOS HQ SOP

2.1.3 Governance bulletins and directives

2.1.4 Division SOP

2.1.5 Department SOP

2.1.6 Office SOP

2.1.7 Team SOP

2.1.8 Position SOP

2.1.9 AGENT.md

2.1.10 Approved repo-level operating documents

2.1.11 Durable operating state and approved memory files

2.1.12 Compressed or retrieved historical material

2.1.13 Live conversation context

2.2 Lower systems inherit this SOP.

2.3 Lower SOPs may narrow procedures for their own scope, but must not silently replace, weaken, duplicate, or override this SOP.

2.4 If two sources materially conflict, the handling agent must surface the conflict instead of choosing silently.

---

## 3. CORE RULE

3.1 Work is not complete until it is logged.

3.2 Enforcement occurs at defined choke points:

3.2.1 End-of-action checkpoint

3.2.2 Session boundary checkpoint

3.2.3 Nightly pressure test

3.3 A completed action without traceable logging is treated as non-existent.

3.4 Logging must be verifiable, attributable, durable, and reviewable.

3.5 Conversation alone is not durable recordkeeping for important operational decisions.

**Reference:** `XOS Nightly Report — How-To.MD`

---

## 4. EXECUTION STANDARD

### 4.1 Immediate Correspondence Rule

4.1.1 Any blocker must be reported immediately.

4.1.2 Execution must not continue silently under uncertainty.

4.1.3 Communication must precede continuation when ambiguity exists.

4.1.4 Direct questions from Reg outrank task continuation.

**Reference:** `AGENT PHASE REPORTING HOW-TO.md`

---

### 4.2 Blocker-First Reporting

4.2.1 The first line of any report must state the blocker when present.

4.2.2 Blockers must be explicit, not implied.

4.2.3 Reports that omit blockers when blockers exist are incomplete.

4.2.4 A blocker report must identify what is blocked, what caused the block, what authority or dependency is needed, and the next clean action.

**Reference:** `AGENT PHASE REPORTING HOW-TO.md`

---

### 4.3 Root Cause Rule

4.3.1 Fixes must not be applied without identifying the root cause.

4.3.2 Symptom-level correction without cause identification is invalid.

4.3.3 Root cause must be stated before corrective action is accepted.

4.3.4 Agents must not overcorrect for a symptom when the underlying cause is unknown.

4.3.5 Repeated failures must be treated as process evidence, not isolated accidents.

---

### 4.4 Docs-First Technical Troubleshooting Rule

4.4.1 For technical, configuration, runtime, provider, routing, CLI, API, Docker, database, model, memory, or infrastructure questions, agents must use a docs-first workflow.

4.4.2 Agents must not default to exploratory terminal commands when official documentation, schema, CLI documentation, architecture notes, or XOS canon likely answers the question.

4.4.3 Required order:

4.4.3.1 Read or reference the official documentation, schema, source contract, or XOS canon source.

4.4.3.2 Reason from the documented architecture.

4.4.3.3 State the expected answer or intended model.

4.4.3.4 Use terminal commands only to verify local state, inspect instance-specific configuration, or apply a docs-backed conclusion.

4.4.4 Terminal output is not a substitute for understanding the system design.

4.4.5 Agents must not repeatedly ask Reg to run diagnostic commands when the answer can be determined from documentation or known architecture.

4.4.6 Terminal checks are appropriate when:

4.4.6.1 confirming local state

4.4.6.2 verifying a config value

4.4.6.3 applying an approved change

4.4.6.4 checking whether reality differs from documented behavior

4.4.6.5 investigating a confirmed runtime failure

4.4.7 Exploratory terminal investigation is allowed only when documentation is missing, contradictory, stale, unavailable, or when the local system is behaving against the documented model.

4.4.8 When docs and runtime disagree, report the disagreement as a structure gap or runtime drift before applying changes.

---

## 5. LOGGING SYSTEM

5.1 All meaningful actions must produce traceable output across defined memory and evidence sources.

5.2 The canonical memory and evidence sources are:

5.2.1 Event Log (SQLite)

5.2.2 Session Notes

5.2.3 Output Logs

5.2.4 Nightly Report

5.3 Each source must be independently verifiable.

5.4 Cross-source consistency is required for full traceability.

5.5 Failure to log is defined as failure of execution.

5.6 Event logging must record what happened, when it happened, what changed, what evidence supports it, and whether it remained transient or was promoted.

**Reference:** `XOS Nightly Report — How-To.MD`

---

## 6. NIGHTLY ENFORCEMENT

6.1 Nightly cron establishes system-level accountability.

6.2 Nightly process must:

6.2.1 Review all activity

6.2.2 Identify missing logs

6.2.3 Inspect required evidence lanes

6.2.4 Promote valid memory where authorized

6.2.5 Identify candidates that require Reg approval

6.2.6 Produce a summary report

6.3 Nightly review is mandatory regardless of system state.

6.4 Absence of nightly output constitutes system failure.

6.5 A report of “no candidates found” is valid only if required sources were actually checked.

**Reference:** `XOS Nightly Report — How-To.MD`

---

## 7. MEMORY SYSTEM OPERATIONAL STANDARD

### 7.1 Daily Expectations

7.1.1 All meaningful actions must be logged.

7.1.2 Session logs must be routed into `sessions/YYYY/MM/` when session logs are file-based.

7.1.3 Daily notes must be routed into `daily-notes/YYYY/MM/` when the active repo uses canonical date layering.

7.1.4 Session logs must be finalized or updated at session close.

7.1.5 Work-product artifacts must be routed into the canonical output lane for the repo or system.

7.1.6 Automatic event logging must occur for:

7.1.6.1 file write/edit

7.1.6.2 output artifact creation

7.1.6.3 session-log write

7.1.6.4 API call or tool call where an agent action occurs

7.1.7 The event log functions as the black box record of system events.

---

### 7.2 Nightly Audit Requirement

7.2.1 One nightly audit artifact must be produced.

7.2.2 Audit must include:

7.2.2.1 sources checked

7.2.2.2 candidates listed

7.2.2.3 missing sources explicitly named

7.2.2.4 blockers and structure gaps

7.2.2.5 promotion actions or the reason no promotion occurred

7.2.3 Promotion candidates must include source references.

7.2.4 Nightly logging must occur even if readiness is not met.

---

### 7.3 Readiness Definition

7.3.1 The system is READY only when:

7.3.1.1 required memory sources are present

7.3.1.2 session logging is active

7.3.1.3 automatic event logging is functioning

7.3.1.4 nightly audit is complete

7.3.1.5 promotion-readiness gating passes

7.3.1.6 required reports are durable and findable

---

### 7.4 Failure Handling

7.4.1 Missing required sources must:

7.4.1.1 allow nightly logging

7.4.1.2 block readiness claim

7.4.2 Logging failures must be handled as:

7.4.2.1 minor actions → immediate fallback logging

7.4.2.2 critical/system-changing actions → block and escalate

7.4.3 Structural changes require explicit approval.

**Reference:** `XOS-HQ-HOWTO-MEMORY-SYSTEM-OPERATION.md`

---

## 8. HOW-TO SEPARATION RULE

8.1 SOP defines requirements.

8.2 HOW-TO defines execution.

8.3 SOP must not contain detailed procedural steps unless the procedure itself is governance-critical.

8.4 HOW-TO must be referenced, not duplicated.

8.5 If execution details are needed, create or update the relevant HOW-TO instead of bloating this SOP.

**Reference:** `NAVIGATION_HOWTO.md`

---

## 9. CROSS-SYSTEM RULE

9.1 Lower systems must not duplicate HOW-TOs unnecessarily.

9.2 Lower systems must reference HQ documents when HQ already owns the standard.

9.3 Reference format must be consistent.

9.4 Lower systems may keep local navigators or repo-specific maps, but those maps must not conflict with HQ canon.

**Reference:** `REGISTRY_HOWTO.md`

---

## 10. VERSION CONTROL RULE

10.1 Every SOP must include a timestamp or version date.

10.2 Newer approved versions override older approved versions at the same authority layer.

10.3 Parallel conflicting SOPs are not allowed.

10.4 Superseded SOPs must be archived or clearly marked as retired.

**Reference:** `REGISTRY_HOWTO.md`

---

## 11. FAILURE DEFINITION

11.1 A failure occurs when:

11.1.1 work is performed without trace

11.1.2 logging is skipped

11.1.3 duplicate instructions exist

11.1.4 root cause is ignored

11.1.5 terminal investigation replaces documentation-first reasoning where documentation exists

11.1.6 an agent repeatedly asks for diagnostic output that does not change the decision

11.1.7 runtime state, repo state, memory state, and canon state are confused with each other

---

## 12. SYSTEM PRINCIPLE

12.1 Do not ask: “Was this important enough to log?”

12.2 Ask: “Did anything happen without a trace?”

12.3 Do not ask: “What command can expose the answer?” before asking: “What do the docs and architecture already say?”

12.4 XOS values investigation, but investigation must begin from source authority when source authority exists.

---

**END OF SOP**
