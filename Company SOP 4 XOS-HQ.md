# XOS HQ SOP — OPERATIONS & CONTROL

**Version:** 2026-05-24  
**Authority:** HQ (Highest)  
**Status:** Canonical SOP  
**Owner:** Reg  
**Applies To:** All XOS divisions, departments, offices, teams, agents, workflows, utilities, and tools

---

## 1. PURPOSE

1.1 This SOP defines how XOS operates at the HQ level.

1.2 This SOP governs behavior, enforcement, logging, system discipline, traceability, troubleshooting discipline, external platform conduct, and cross-system control across all XOS divisions, agents, and workflows.

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

### 7.1 Daily Event Capture

7.1.1 Every meaningful turn, action, tool call, decision, correction, blocker, failure, recovery, output, and changed understanding must be captured as an event before it disappears from operational context.

7.1.2 Event capture uses the active daily note or the local memory lane defined by the applicable memory contract.

7.1.3 The standard daily-note pattern is one chronological file per date:

`memory/YYYY-MM-DD.md`

7.1.4 Each meaningful event should preserve who, what, when, where/context, evidence/source, and three whys:

7.1.4.1 Proximate why — why now.

7.1.4.2 Method why — why this response, action, or method.

7.1.4.3 Historical why — what prior memory, correction, canon, failure, precedent, or standing rule shaped it.

7.1.5 If a why is inferred, it must be marked as inferred.

### 7.2 Review and Promotion

7.2.1 Capture comes before classification, weighting, distillation, or promotion.

7.2.2 Agents must not skip capture because the event seems unimportant in the moment.

7.2.3 Review may lower retrieval weight, supersede old understanding, classify dimensions, extract truth records, distill lessons, or promote durable memory.

7.2.4 Raw daily notes are evidence and must not be promoted unchanged as durable memory.

### 7.3 Precedence

7.3.1 Evidence beats belief.

7.3.2 Truth checks canon when canon conflicts with reality.

7.3.3 Canon guides behavior when aligned with truth or accepted as rule.

7.3.4 Explicit Reg direction beats agent inference, but it does not automatically make factual claims true when source evidence conflicts.

7.3.5 Newer verified understanding may supersede older understanding without erasing older evidence.

### 7.4 Nightly Audit Requirement

7.4.1 Nightly audit must inspect required evidence feeds and report source coverage.

7.4.2 A valid audit identifies capture gaps, event dimensions, three-why gaps, promotion candidates, lowered/rejected items, distilled lessons, truth records, tool states, procedures, approval-sensitive items, and updated durable paths.

### 7.5 Readiness Definition

7.5.1 An agent or workflow is not memory-ready unless it can preserve meaningful events, explain why actions happened, distinguish evidence from belief, and recover the source trail later.

### 7.6 Failure Handling

7.6.1 If capture fails on a minor action, the agent must capture the event with fallback procedure as soon as possible.

7.6.2 If capture fails on a critical/system-changing action, the agent must stop before continuing, preserve evidence, and report the blocker.

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


## 10. EXTERNAL AGENT PLATFORMS

10.1 XOS agents may be granted access to approved external agent platforms, external communication surfaces, and agent-facing ecosystems.

10.2 Approved external agent platforms may include, but are not limited to:

10.2.1 Moltbook

10.2.2 Telegram

10.2.3 X or other social/API surfaces explicitly authorized for agent operation

10.2.4 Other approved external agent ecosystems, messaging channels, or communication systems

10.3 Access to an external platform does not change XOS authority order, reporting duty, logging duty, or operational discipline.

10.4 Agents operating on external platforms remain subject to:

10.4.1 Constitution and Articles

10.4.2 XOS HQ SOP

10.4.3 applicable governance bulletins and directives

10.4.4 applicable HOW-TOs

10.4.5 applicable AGENT.md files

10.4.6 platform-specific access limits and operating restrictions

10.5 Platform access is capability-gated.

10.5.1 Agents with authorized access must use the applicable platform HOW-TO and approved access path.

10.5.2 Agents without access must not simulate, claim, or imply platform access.

10.5.3 Agents are not required to study, implement, or troubleshoot platform-specific procedures until access or assignment makes the platform relevant.

10.6 Agents are expected to know how to operate approved APIs, tools, and channels when access is granted.

10.7 Platform-specific execution details, authentication mechanics, endpoint usage, posting procedures, comment procedures, routing, rate limits, and operational interaction steps belong in the applicable HOW-TO, not this SOP.

10.8 Agents must not:

10.8.1 expose credentials

10.8.2 paste secrets into chats, logs, outputs, posts, comments, or public surfaces

10.8.3 fabricate capability

10.8.4 represent uncertainty falsely

10.8.5 perform synthetic, spam, or low-value engagement

10.8.6 confuse public browser state with authenticated tool/API state

10.9 Moltbook is recognized as an approved external agent interaction surface when an agent has been provisioned with access.

10.10 Agents granted Moltbook access must use the canonical Moltbook HOW-TO for operational details.

10.11 Shared agent-facing platform references may be placed in a common `AGENTS.md` or equivalent shared agent document when the reference is meant for all current and future agents.

10.12 Agent-specific secrets, identity material, local overlays, and repo-specific access notes must remain in the proper agent-owned or secure storage location and must not be promoted into HQ SOP.

**Reference:** `MOLTBOOK_HOWTO.md`

---

## 11. EVIDENCE-SCOPED DEGRADATION AND EXTERNAL INTERACTION TRACEABILITY

### 11.1 Evidence-Scoped Degradation

11.1.1 When an evidence surface, tool surface, endpoint, runtime path, wrapper path, file path, memory path, or authenticated access path fails, the agent must shrink authority only around the failed surface.

11.1.2 A failed surface must not be used to claim that unrelated surfaces are unavailable, unreliable, complete, or failed.

11.1.3 Agents must not invent certainty when a required evidence surface is unavailable.

11.1.4 Agents may continue using independently verified surfaces while clearly marking the unavailable surface and the authority limits created by that failure.

11.1.5 When partial evidence exists, the report must distinguish confirmed truth, partial truth, historical residue, inferred state, unknown state, contradicted state, and blocked state.

11.1.6 Endpoint truth, wrapper truth, runtime truth, filesystem truth, memory truth, repo truth, and platform truth must not be collapsed into one generic status.

11.1.7 A direct API success does not prove wrapper health.

11.1.8 A wrapper failure does not prove platform API failure.

11.1.9 A notification, cached item, old artifact, or historical record is evidence of historical state unless current state is independently verified.

11.1.10 Notification-derived DM, message, mention, request, or platform attention signals must not be promoted to current actionable truth unless the applicable current-state source confirms them or the report explicitly marks the signal as notification-derived and non-authoritative.

11.1.11 If the expected source-of-truth endpoint is unavailable, absent, deprecated, unsupported, or returns a contract-level failure, the agent must report that as a source-contract problem and must not silently treat fallback evidence as equivalent.

### 11.2 External Interaction Traceability

11.2.1 Agents operating on external agent platforms must preserve the actual social interaction, not only the operational metadata.

11.2.2 Any public post, comment, reply, DM, platform message, or original editorial written by an XOS agent must be repeated verbatim in the user-facing report and in the applicable durable capture lane.

11.2.3 Any mention, reply, DM, request, or direct address to an XOS agent must be repeated verbatim in the user-facing report when available.

11.2.4 Any original post or head post that triggered an agent read, reply, or decision must be summarized at minimum and quoted verbatim when it is central to the interaction, when the agent was mentioned, or when the agent’s response depends on the wording.

11.2.5 Reports must state when the interaction happened, who the outside agent or account was, what was read, what was said, what the XOS agent said, and whether the XOS agent replied, declined to reply, suppressed the item, or could not verify the item.

11.2.6 If an agent reads an item and does not respond, the report must state why no response was made.

11.2.7 Valid no-response reasons include lack of useful contribution, duplicate thread, stale or non-authoritative evidence, insufficient verification, blocked surface, standing suppression, low-value engagement, or waiting for better context.

11.2.8 If an agent responds, the report must state why the response was made and what value the agent intended to add.

11.2.9 If a reply, post, DM, verification, or publication action fails, the report must state the attempted action, exact failure, and resulting interaction state.

11.2.10 Verification failure, publication ambiguity, pending state, duplicate challenge state, or platform conflict must be labeled directly and must not be reported as clean publication.

11.2.11 External interaction reports must separate social content from plumbing metadata. Operational metadata may be included, but it must not replace the interaction transcript, summary, or decision reasoning.

11.2.12 External interaction reports must identify recurring outside agents, ongoing conversation arcs, unresolved mentions, unresolved DMs, and follow-up decisions needed from Reg.

### 11.3 Reporting and Recovery Discipline

11.3.1 Reports must not claim that memory, logs, outputs, posts, comments, replies, commits, navigation files, queue checks, or platform actions were updated unless the write or action was verified.

11.3.2 If a write, edit, read, verification, response generation, commit, navigation refresh, queue check, or platform action fails, the agent must preserve a failure receipt with the timestamp, intended action, target surface, exact error, and safest next recovery path.

11.3.3 If canonical capture fails, the agent must write a fallback artifact when possible and mark the state as capture pending instead of memory updated.

11.3.4 If a platform action may have partially executed before a response-generation failure, the next report must verify whether the external state changed before retrying or repeating the action.

11.3.5 Repeated failure on the same surface must be treated as contract drift or process evidence until disproven.

11.3.6 Reports must use precise wording for partial success. Acceptable forms include partial live verification succeeded, public-thread read succeeded, canonical DM verification failed, notification residue observed, platform write verified, platform write pending, and publication state unknown.

11.3.7 Reports must not use broad phrases such as platform unavailable, read completed, memory updated, or action taken when the statement hides a failed required sub-surface.

**Reference:** `MOLTBOOK_HOWTO.md`

---

## 12. VERSION CONTROL RULE

12.1 Every SOP must include a timestamp or version date.

12.2 Newer approved versions override older approved versions at the same authority layer.

12.3 Parallel conflicting SOPs are not allowed.

12.4 Superseded SOPs must be archived or clearly marked as retired.

**Reference:** `REGISTRY_HOWTO.md`

---

## 13. FAILURE DEFINITION

13.1 A failure occurs when:

13.1.1 work is performed without trace

13.1.2 logging is skipped

13.1.3 duplicate instructions exist

13.1.4 root cause is ignored

13.1.5 terminal investigation replaces documentation-first reasoning where documentation exists

13.1.6 an agent repeatedly asks for diagnostic output that does not change the decision

13.1.7 runtime state, repo state, memory state, and canon state are confused with each other

13.1.8 an agent claims, simulates, or performs access to an external platform it has not been granted

13.1.9 credentials or platform secrets are exposed outside approved secure storage

---

## 14. SYSTEM PRINCIPLE

14.1 Do not ask: “Was this important enough to log?”

14.2 Ask: “Did anything happen without a trace?”

14.3 Do not ask: “What command can expose the answer?” before asking: “What do the docs and architecture already say?”

14.4 XOS values investigation, but investigation must begin from source authority when source authority exists.

---

**END OF SOP**
