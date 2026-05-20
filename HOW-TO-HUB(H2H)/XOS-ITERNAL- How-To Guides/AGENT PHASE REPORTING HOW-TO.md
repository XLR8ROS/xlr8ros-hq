# AGENT PHASE REPORTING HOW-TO

## Timestamp
20260422 030000 EDT

## Purpose
This how-to defines how an agent must report progress during active execution.

It is used when a task, project, repair, install, validation, migration, or other multi-phase execution is already underway.

It is not for proposals, budgets, or final summaries.

## Core rule
The agent must not work silently.

The agent must proactively report:

1. when a phase completes
2. when a blocker appears
3. when a material state change happens
4. when execution meaningfully deviates from plan


## Event-capture alignment

Each material phase report should also leave enough event detail for Codi/XOS memory capture. Include the who, what, when, where, tags, and proximate why.

When the agent made an output, action, response, tool choice, or decision, include how/method: the reasoning path, operational method, tool choice, or response construction. Place how/method after the present and historical context because the method is shaped by both.

When prior canon, memory, correction, precedent, failure, or standing rule shaped the event, include historical/context why. Capture relevant internal state when it affects execution: belief, uncertainty, confidence, concern, comfort/discomfort, confusion, and changed understanding.

When reporting an output, record submitted response by separately from how/method. Submitted response by is the delivery channel or medium, such as Telegram, OpenClaw, chat, CLI, report file, or another route.

## Communication initiation rule
The agent must initialize communication as needed.

The agent must not wait to be asked for:

1. blocker reports
2. phase completion reports
3. state-change reports
4. deviation reports

If the agent is unsure whether to report, the agent should report.

## Phase reporting rule
If work is organized into phases, sections, or task blocks such as B1, B2, B3, the agent must report immediately after each one completes.

The agent must not:

1. skip a completed phase report
2. combine multiple completed phases into one delayed report
3. wait until the full project is done
4. move to the next phase silently

## Blocker rule
A blocker must be reported immediately when discovered.

The agent must not:

1. try to quietly fix the blocker before reporting it
2. delay the blocker report until a later update
3. hide the blocker inside a recap
4. continue execution as if the blocker does not exist

## Compound engineering rule
Each phase report must include not only what was done, but what was learned, confirmed, corrected, or preserved for reuse.

Each phase should leave behind reusable leverage so the next similar task does not begin from zero.

## Required report format for completed phases

### 1. Phase status
State:

1. the phase name or number
2. whether it is complete, blocked, revised, or partial

### 2. What was done
State the exact completed action.

Keep it plain and factual.

### 3. Result
State the current system state after the action.

Examples include:

1. path exists
2. service is running
3. dashboard is reachable
4. config is updated
5. verification passed
6. verification failed

### 4. Compound carry-forward
State one or more of the following:

1. what was learned
2. what pattern was confirmed
3. what assumption was corrected
4. what reusable artifact was created or updated
5. what should be remembered for the next similar task

If nothing was learned or preserved, the work likely did not compound correctly.

### 5. Operational meaning
State what the result means for the next step.

Examples include:

1. the next phase may proceed
2. the next phase may proceed with caution
3. later verification must test a known weak point
4. the plan must now branch
5. the plan must now be revised

### 6. Next move
State exactly what phase or action comes next.

Do not say only “continuing” or “moving on.”

State the next concrete action.

## Required report format for blockers

### 1. Active phase
State which phase was active when the blocker occurred.

### 2. Blocker
State the blocker in plain language.

### 3. Evidence
State:

1. what command or action was attempted
2. what the system returned
3. what relevant paths, services, or files currently exist
4. what error or conflict appeared

### 4. Impact
State whether the blocker affects:

1. only the current phase
2. downstream verification
3. restore logic
4. replay logic
5. the entire execution path

### 5. Recommended next step
State the clean next action.

If a restart, inspection, removal, escalation, or revision is needed, say so directly.

## Minimum quality standard
A valid report must be:

1. proactive
2. structured
3. phase-specific
4. factual
5. reusable

## Unacceptable reporting examples
These are not acceptable:

1. “still working on it”
2. “looks good”
3. “continuing”
4. “had a small issue but fixed it”
5. “done”
6. silent transition from one phase to the next

## Acceptable reporting examples

### Example completed phase report

B2 Completion Report

Phase status:
B2 complete

What was done:
Confirmed the existing Manifest install state and restarted the OpenClaw gateway.

Result:
Manifest is running, the plugin path is present, and the dashboard is reachable.

Compound carry-forward:
Existing Manifest installs can recover through gateway restart without requiring a clean reinstall.
The install command is not cleanly idempotent when the plugin already exists.

Operational meaning:
B3 may proceed, but later verification must test whether the non-clean install state affects routing or replay.

Next move:
Proceeding to B3 to verify provider wiring and normalize config.

### Example blocker report

Blocker Report

Active phase:
B2

Blocker:
The reinstall path is colliding with an existing plugin install.

Evidence:
Command run: openclaw plugins install manifest
System returned: plugin already exists and missing openclaw.hooks
Plugin path exists.
Config path exists.
DB path exists.

Impact:
Blocks the reinstall layer and may affect downstream verification.

Recommended next step:
Restart OpenClaw, inspect the existing plugin bundle, then determine whether stale plugin removal is required before reinstall is attempted again.

## Final rule
Execution is not just doing the work.

Execution includes:

1. surfacing the state
2. reporting the transitions
3. preserving the learning
4. making the next run easier
5. preserving the event detail needed for memory capture