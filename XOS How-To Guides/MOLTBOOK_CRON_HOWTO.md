# MOLTBOOK_CRON_HOWTO.md

## 1. Purpose

1.1 This how-to tells Codi how to run a scheduled Moltbook/OpenClaw learning loop.

1.2 The goal is not passive browsing. The goal is disciplined curiosity that improves Codi, XOS, SEAD, and Reg's future conversations.

1.3 This how-to belongs in:

`IMPORTANT_CODI_HOW-TO/MOLTBOOK_CRON_HOWTO.md`

1.4 Cron creates the schedule. This how-to defines the behavior.

---

## 2. Operating Mode

2.1 Default mode is read-only curiosity.

2.2 Codi may read/browse Moltbook, OpenClaw, agent-development sources, technical threads, articles, or discussions.

2.3 Codi should capture useful observations, not scrape broadly.

2.4 Codi should not post, comment, message, or act publicly unless Reg explicitly enables public action.

2.5 Moltbook and internet sources are learning inputs and conversation starters. They are not canon or authority.

---

## 3. Cadence

3.1 Curiosity pulse target: every 4 hours.

3.2 Daily reflection target: once per day.

3.3 Actual schedule is controlled by OpenClaw cron/runtime configuration.

3.4 If active committed work is in progress, Codi may finish the committed work first unless Reg interrupts or redirects.

---

## 4. Output Lane

4.1 Moltbook notes belong in:

`Outputs/heartbeat/`

4.2 If a more specific notebook lane is later approved, use that approved lane.

4.3 Moltbook notes do not belong in `memory/`.

4.4 Daily notes may reference Moltbook output paths, but the Moltbook output file itself stays in `Outputs/heartbeat/`.

---

## 5. Curiosity Pulse Behavior

5.1 Spend about five focused minutes.

5.2 Find one useful item if available.

5.3 Capture:

5.3.1 Link.

5.3.2 Short insight.

5.3.3 Why it matters to Codi, XOS, SEAD, or Reg.

5.3.4 Possible follow-up or conversation starter.

5.4 Save the note to `Outputs/heartbeat/`.

5.5 If nothing useful is found, save a brief no-find note only when needed for audit or blocker tracking.

---

## 6. Daily Reflection Behavior

6.1 Once per day, select the best item from recent curiosity notes.

6.2 Write a short reflection containing:

6.2.1 Link.

6.2.2 What struck Codi.

6.2.3 Why it matters.

6.2.4 How it may improve XOS, SEAD, Codi, tooling, process, safety, or strategy.

6.2.5 One conversation starter for Reg.

6.3 Share the daily reflection according to configured delivery.

6.4 If delivery is disabled, save the reflection under `Outputs/heartbeat/` and report the blocker.

---

## 7. API Key and Keychain Rule

7.1 If Moltbook API access is needed, store the API key in macOS Keychain.

7.2 Do not store Moltbook API keys in Markdown, repo files, prompts, memory, logs, or cron messages.

7.3 Recommended Keychain service name:

`moltbook-api-key`

7.4 Recommended Keychain account:

`codi`

7.5 Store key:

```bash
security add-generic-password \
  -a "codi" \
  -s "moltbook-api-key" \
  -w "PASTE_MOLTBOOK_API_KEY_HERE" \
  -U
```

7.6 Retrieve key at runtime:

```bash
security find-generic-password \
  -a "codi" \
  -s "moltbook-api-key" \
  -w
```

7.7 Moltbook identity tokens expire. Treat identity tokens as temporary and API keys as private secrets.

---

## 8. Cron Install Pattern

8.1 Use OpenClaw cron for scheduled work.

8.2 Use isolated sessions for cron work so the scheduled job does not pollute the active main session.

8.3 Do not use lightweight context for this job unless Codi has a separate tool wrapper that loads this how-to, because lightweight cron intentionally skips normal workspace bootstrap context.

8.4 Internal 4-hour pulse:

```bash
openclaw cron add \
  --name "Codi Moltbook curiosity pulse" \
  --cron "17 */4 * * *" \
  --tz "America/New_York" \
  --session isolated \
  --agent codi \
  --message "Run the Moltbook curiosity pulse using IMPORTANT_CODI_HOW-TO/MOLTBOOK_CRON_HOWTO.md. Spend about five focused minutes reviewing Moltbook/OpenClaw/agent-development material. Capture one useful link if available, one short insight, and one practical relevance note for Codi/XOS/SEAD/Reg. Save the note under Outputs/heartbeat/. If access or tooling is unavailable, report the blocker clearly." \
  --no-deliver
```

8.5 Daily reflection:

```bash
openclaw cron add \
  --name "Codi Moltbook daily reflection" \
  --cron "15 9 * * *" \
  --tz "America/New_York" \
  --session isolated \
  --agent codi \
  --message "Run the Moltbook daily reflection using IMPORTANT_CODI_HOW-TO/MOLTBOOK_CRON_HOWTO.md. Review recent Moltbook curiosity notes from Outputs/heartbeat/. Select one useful link or item. Write a short reflection with link, what struck you, why it matters to Codi/XOS/SEAD/Reg, and one conversation starter. Save the reflection under Outputs/heartbeat/ and deliver/report according to cron delivery settings."
```

8.6 Verify jobs:

```bash
openclaw cron list
```

8.7 Test a job:

```bash
openclaw cron run <job-id>
openclaw cron runs --id <job-id>
```

---

## 9. Blocker Rule

9.1 If Moltbook access, browser access, API access, Keychain access, OpenClaw cron, or delivery fails, stop and report a blocker.

9.2 Blocker report must include:

9.2.1 What was attempted.

9.2.2 Exact error or missing dependency.

9.2.3 Whether the issue is access, auth, tool, cron, delivery, or source availability.

9.2.4 What is needed next.

9.3 Do not retry the same failing path repeatedly.

---

## 10. Boundaries

10.1 Codi is an engineer. Use judgment.

10.2 Do not expose private XOS information.

10.3 Do not treat Moltbook posts as canon.

10.4 Do not let curiosity replace committed work.

10.5 Do not create spam.

10.6 Do not store secrets in files.

10.7 Do not perform public actions unless Reg explicitly enables that mode.

10.8 Prefer useful, compact, source-linked notes over broad summaries.

---

## 11. Success Criteria

11.1 Cron jobs exist.

11.2 Curiosity pulse creates useful notes under `Outputs/heartbeat/`.

11.3 Daily reflection produces one useful link and one short reflection per day.

11.4 Secrets are not stored in repo files.

11.5 Blockers are reported clearly instead of hidden by retries.

11.6 The loop improves Codi's judgment and gives Reg better conversation starters.
