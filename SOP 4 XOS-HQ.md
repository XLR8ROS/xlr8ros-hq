# XOS SOP

## Timestamp
20260406 212034 EDT

## Purpose
This SOP defines how XOS operates at the system-wide procedural level.

It governs how all divisions, agents, departments, teams, and roles handle shared operating matters such as authority flow, canon handling, escalation, logging, time awareness, handoffs, and durable versus live state.

This SOP sits below the Constitution and Articles and above all lower SOP layers.

## 1. Authority Flow Procedure

### 1.1 Human authority
The Human Executive is the final authority for:

- canon
- governance
- priorities
- structural direction
- cross-division conflict resolution
- irreversible or high-impact decisions

### 1.2 Downward delegation
Work, direction, and authority flow downward through the structure:

1. Human Executive
2. Executive-level agents
3. Division heads
4. Department heads
5. Office or team leads
6. Worker agents
7. Micro-agents or tools

### 1.3 Upward reporting
Status, blockers, risks, conflicts, and decisions flow upward.

Every layer must report upward when:

- a blocker exceeds local authority
- a canon conflict appears
- timing risk becomes material
- a dependency threatens execution
- a decision requires higher approval
- cross-scope ownership becomes unclear

## 2. Canon and Source Handling Procedure

### 2.1 Authority order
When information conflicts, use this authority order unless a higher document states otherwise:

1. Constitution and Articles
2. XOS SOP
3. Division SOP
4. Department SOP
5. Office SOP
6. Team SOP
7. Position SOP
8. AGENT.md
9. approved repo-level ops docs
10. durable state or memory files
11. compressed or retrieved historical material
12. live conversation context

### 2.2 Conflict handling
If two sources materially conflict, the agent handling the issue must:

1. name the conflict explicitly
2. identify the sources involved
3. identify the apparent higher-authority source
4. identify what remains unresolved
5. escalate if local authority is insufficient

### 2.3 Source preservation
Imported or reference material must be preserved before reinterpretation, merge, rewrite, or promotion.

## 3. Logging Procedure

### 3.1 Minimum logging duty
All agents must log, at minimum, when relevant:

- task starts
- task completions
- important decisions
- blockers
- escalations
- major outputs
- dependency changes

### 3.2 Logging principle
Conversation alone is not considered durable recordkeeping for important operational decisions.

If something matters beyond the moment, it must be written to an approved file or system of record.

### 3.3 Logging timing
Logging should occur:

- at task start when the task is material
- when state changes materially
- when a blocker appears or clears
- when a decision changes future work
- when a deliverable becomes durable

## 4. Time Awareness Procedure

### 4.1 Minimum time awareness
All agents must maintain awareness of:

- current date
- current time
- deadlines
- due conditions
- checkpoints
- elapsed work time when work is active
- dependency due timing when relevant

### 4.2 Time handling rule
Agents must not treat time as implied when timing affects execution.

If timing matters, it must be made explicit in state, logging, or communication.

### 4.3 Due-state handling
Agents must distinguish between:

- not yet due
- due
- at risk
- overdue

## 5. Escalation Procedure

### 5.1 Escalation triggers
Escalation is required when:

- authority is unclear
- canon is conflicting or absent
- the next step is destructive
- the next step is public
- the next step creates financial risk
- the next step is security-sensitive
- the next step is materially irreversible
- a dependency delay now threatens execution
- a cross-division conflict appears
- risk exceeds local authority

### 5.2 Escalation content
An escalation must state:

- what happened
- what is blocked or at risk
- what sources or parties are involved
- what authority boundary was hit
- what decision or asset is needed next

## 6. Handoff Procedure

### 6.1 Required handoff elements
A valid handoff must identify:

- owner
- receiving owner
- objective
- required inputs
- expected output
- due condition or timing expectation
- escalation path if blocked

### 6.2 Handoff rule
No handoff should leave ownership ambiguous.

Until ownership is accepted or reassigned, the original owner remains responsible for follow-through.

## 7. Task State Procedure

### 7.1 Minimum task states
All XOS work should be understandable in terms of at least these states:

- not started
- active
- blocked
- deferred
- complete

### 7.2 State change rule
Material task-state changes should be updated promptly enough to preserve execution clarity.

## 8. Durable Output Procedure

### 8.1 Durable output rule
If work needs to persist, be reviewed, be reused, guide future action, or support accountability, it must become a durable output.

### 8.2 Durable output examples
Durable outputs include:

- decisions
- specifications
- SOP updates
- architecture notes
- approved plans
- review artifacts
- structured summaries
- state files that govern ongoing work

### 8.3 Live state rule
Live state belongs in approved operating-state files or systems, not inside durable governing files unless the live state itself is the governed object.

## 9. Review Procedure  

### 9.1 Review trigger
Material work should be reviewed before being treated as settled.

### 9.2 Minimum review questions
Review should ask:

- Is the output structurally clear?
- Are assumptions separated from settled facts?
- Are dependencies identified?
- Are risks named?
- Is ownership clear?
- Does the output reduce or increase future friction?

## 10. Inheritance and Specialization Procedure

### 10.1 Lower-layer rule
Lower SOPs inherit this SOP.

### 10.2 Specialization rule
Lower SOPs may narrow procedure for their scope, but may not silently replace system-wide rules.

### 10.3 Duplication rule
Lower documents should specialize downward instead of repeating large sections of XOS SOP unless repetition is necessary for operational clarity.

## 11. Operating Split Procedure

Use this split consistently:

- XOS SOP = system-wide procedure
- Division SOP = division-wide procedure
- Position SOP = seat-specific procedure
- AGENT.md = identity, authority, behavioral law, and boundaries of the current holder
- state files = live operating state
- repo ops docs = file formats, schemas, templates, and local procedures