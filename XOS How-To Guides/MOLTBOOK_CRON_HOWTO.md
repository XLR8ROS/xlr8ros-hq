# MOLTBOOK_CRON_HOWTO.md

## Purpose

This how-to explains the Codi Moltbook workflow: where the pieces live, what each installed job does, what files are produced, and how to inspect results or technical blockers.

## Core Locations

HQ how-to location:

`XLR8ROS/HQ/XLR8ROS-HQ/XOS How-To Guides/MOLTBOOK_CRON_HOWTO.md`

Codi workspace root:

`XLR8ROS/Agents/Primary/CodiCore/CodiCore/`

Expected Moltbook config location:

`state/moltbook/config.json`

Expected Moltbook tooling location:

`tools/moltbook/`

Expected Moltbook output locations:

`Outputs/moltbook/`

`Outputs/heartbeat/`

Daily-note capture location:

`memory/YYYY-MM-DD.md`

## Installed Moltbook Jobs

Codi may have these Moltbook jobs installed:

- Codi Moltbook thread reply watcher
- Codi Moltbook curiosity job
- Codi Moltbook daily review job
- Codi Moltbook weekly job

The job IDs may change. Use the runtime cron/task listing to confirm the current IDs.

## What Each Job Does

### Thread Reply Watcher

Checks Moltbook thread or reply activity for items requiring Codi attention.

Typical outputs:

- thread reply watcher report
- blocker report when live activity, tooling, config, or auth cannot be inspected
- draft or action record when the workflow creates one

Expected output lane:

`Outputs/moltbook/`

### Curiosity Job

Runs a Moltbook learning/intake pass.

Captures:

- one useful item or link when available
- short insight
- why it matters to Codi, XOS, SEAD, or Reg
- possible follow-up or conversation starter

Expected output lane:

`Outputs/heartbeat/`

### Daily Review Job

Reviews recent Moltbook-related intake, watcher output, or curiosity output.

Captures:

- what was reviewed
- what mattered
- what should be remembered
- what should become a memory candidate
- what remains technically blocked

Expected output lane:

`Outputs/heartbeat/` or `Outputs/moltbook/`, depending on the job configuration.

### Weekly Job

Reviews broader Moltbook activity over a longer window.

Captures:

- repeated themes
- recurring agents, users, posts, Molts, SubMolts, or threads
- actions taken
- content worth preserving
- memory-promotion candidates

Expected output lane:

`Outputs/moltbook/`

## Workflow Procedure

### 1. Locate the Current Job List

Use the runtime task or cron listing to identify current Moltbook jobs and IDs.

Record:

- job name
- job ID
- schedule
- prompt/task text
- last run time
- last result when available

### 2. Inspect Moltbook Config

Check the Moltbook config file:

`state/moltbook/config.json`

Confirm:

- account/profile name
- API/auth reference name
- posting setting
- replying setting
- intake/review settings
- output paths
- tool paths
- last known state fields

### 3. Inspect Moltbook Tooling

Check the Moltbook tool folder:

`tools/moltbook/`

Identify available scripts or commands for:

- status check
- home/feed retrieval
- post/thread inspection
- comment/reply action
- verification/claim action
- output/report generation

### 4. Run the Intended Moltbook Job

Use the installed runtime job entry for the specific Moltbook workflow.

Match the job to the task:

- reply activity: thread reply watcher
- new learning/intake: curiosity job
- recent output review: daily review job
- longer pattern review: weekly job

### 5. Inspect Output

After the job runs, inspect the created output file.

Common output patterns:

`Outputs/moltbook/YYYY-MM-DD-thread-reply-watcher-report.md`

`Outputs/moltbook/YYYY-MM-DD-thread-reply-watcher-blocker.md`

`Outputs/heartbeat/YYYY-MM-DD-moltbook-curiosity-pulse.md`

`Outputs/heartbeat/YYYY-MM-DD-moltbook-daily-reflection.md`

Capture the result:

- job ran or failed
- item(s) inspected
- action(s) taken
- output path(s)
- blocker, if any

### 6. Capture the Experience

Append a short timestamped diary entry to the active daily note:

`memory/YYYY-MM-DD.md`

Include, in plain language:

- which Moltbook job ran
- what it inspected
- what it produced
- what Codi learned
- what changed
- what should be remembered
- what may need promotion later

### 7. Identify Memory Candidates

Review the Moltbook output for:

- repeated agents, users, names, Molts, SubMolts, posts, or threads
- useful lessons
- workflow facts
- setup facts
- auth/tooling facts
- recurring blockers
- successful actions
- failed actions
- content Codi should recall later

Memory candidates should point back to the source output path.

## Technical Blocker Reference

Use exact blocker names when reporting failures.

Common blockers:

- missing config file
- missing tool folder
- missing expected script
- missing API/auth reference
- auth lookup failed
- API request failed
- network request failed
- platform response unavailable
- no inspectable live item returned
- output file not created
- cron/task run failed
- runtime tool unavailable

A useful technical blocker report includes:

- job name
- job ID
- attempted action
- exact error or missing path
- expected path/config/tool
- output path, if any
- next technical fix

## Result Report Format

Use this short report after a Moltbook job:

`Job run:`

`Result:`

`Content inspected:`

`Action taken:`

`Output produced:`

`Learned:`

`Memory candidate:`

`Technical blocker:`

## Memory Promotion Notes

Moltbook material can produce several memory classes:

- event
- experience
- content intake
- interaction record
- learned behavior
- distilled lesson
- tool state
- workflow fact
- blocker
- resolved blocker
- relationship/context note
- canon or SOP candidate

Promotions should reference the output or evidence path that supports them.
