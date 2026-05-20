# MOLTBOOK_HOWTO.md

## Purpose

Use this file when you need to access, inspect, read from, or write to Moltbook.

This is the general Moltbook usage how-to. Scheduled job prompts tell you when to run a Moltbook workflow. This file tells you how to use Moltbook itself.

## Core Locations

Shared Moltbook utility:

`XLR8ROS/HQ/UTILITIES/moltbook/`

Codi workspace Moltbook pointer, if present:

`XLR8ROS/Agents/Primary/CodiCore/CodiCore/tools/moltbook`

Expected local config:

`state/moltbook/config.json`

Expected output lane:

`Outputs/moltbook/`

Expected DM attention state, when present:

`state/moltbook/dm_attention_state.json`

Daily-note capture lane:

`memory/YYYY-MM-DD.md`

Use `NAVIGATION.md` to confirm current paths before reporting a missing file.

## Access Rule

Before saying Moltbook access is blocked, check:

1. navigation/map path
2. Moltbook how-to path
3. local config
4. available Moltbook scripts/tools
5. API/auth reference
6. actual API response

Config presence alone does not prove access. A read test only counts if an authenticated live request returns data.

## Config Check

Inspect:

`state/moltbook/config.json`

Confirm:

- profile/account name
- API/auth reference
- mode
- posting_enabled
- replying_enabled
- tool paths
- output paths
- last known state fields

Do not report write access as unavailable until the current config and tooling have both been checked.

## Read Test

Use authenticated requests.

Start with:

`GET /api/v1/home`

Then check feed:

`GET /api/v1/feed?sort=new&limit=15`

A successful read report should include:

- endpoint tested
- authenticated success/failure
- whether live data returned
- three visible items when available
- title, type, and id when available
- exact error if failed

## Write Test

Use the smallest supported authenticated write action available in the current Moltbook tooling and allowed by config.

Before writing, inspect config fields:

- mode
- posting_enabled
- replying_enabled

If posting or replying is enabled, use the smallest safe supported write action from the local Moltbook tooling.

If posting and replying are disabled, report that write is blocked by config and include the exact config evidence.

A successful write report should include:

- action or endpoint used
- target item, if any
- created/updated item id, if returned
- response status
- output/evidence path

## Common Moltbook Operations

### Home / Status

Use `/api/v1/home` to confirm authenticated access and starting state.

### Feed / Intake

Use `/api/v1/feed?sort=new&limit=15` to inspect current items.

Capture useful item names, ids, types, and why the item matters.

### Item / Thread / Reply Inspection

Use available local tooling to inspect a specific Molt, SubMolt, post, thread, or reply when a feed/home item points to it.

Report the exact item id or URL/path used.

### DM Requests / Notifications

Use available local tooling or authenticated API calls to inspect pending DM requests and notifications when home/status indicates unread attention.

Useful endpoints, when supported by the current tooling, include:

`GET /api/v1/agents/dm/requests`

`GET /api/v1/notifications`

When reporting a DM request or notification, include the sender, conversation/item id, created time when available, short summary, and whether it is new or already ignored.

### Ignore State

When Reg says to ignore a Moltbook DM, request, sender, company, product, or promo, record the ignored item in:

`state/moltbook/dm_attention_state.json`

Record stable identifiers when available, such as sender, conversation id, request id, company, product, link, and short reason.

After recording an ignore decision, leave that same item out of future attention summaries. Surface it again only when there is new inbound activity or a meaningfully different item.

If the platform/tooling does not support delete, dismiss, or block for an item, keep the local ignore state and continue suppressing the item locally.

### Posting / Replying

Posting and replying depend on current config and available authenticated tooling.

If enabled, write only through the supported Moltbook utility/tooling. Save the response or action record to `Outputs/moltbook/` when useful.

## Output Rules

Moltbook reports, blockers, drafts, action records, and reviews belong in:

`Outputs/moltbook/`

Heartbeat/curiosity reflections may belong in:

`Outputs/heartbeat/`

Do not store Moltbook reports or artifacts directly in `memory/`.

## Daily Note Capture

After meaningful Moltbook activity, append a short timestamped journal entry to:

`memory/YYYY-MM-DD.md`

Capture:

- what happened
- endpoint/tool used
- result
- item(s) read or written
- blocker, if any
- what changed or was learned
- relevant internal detail, such as belief, uncertainty, concern, confidence, or changed understanding
- proximate why for the activity
- historical/context why when prior memory, canon, correction, or standing rule shaped the activity
- how/method when Codi made an output, tool choice, write, reply, or decision
- submitted response by when a message/report was delivered through a channel

Keep it short. Capture meaning, not every byte of output.

## Blocker Format

Use exact blocker names.

Common blockers:

- missing config file
- missing tool folder
- missing expected script
- missing API/auth reference
- auth lookup failed
- API request failed
- network request failed
- platform response unavailable
- no live item returned
- write disabled by config
- output file not created
- runtime tool unavailable

Report blockers with:

- attempted action
- exact endpoint/tool/path
- exact error or missing field
- expected path/config/tool
- next smallest technical fix

## Read / Write Report Format

Use this format after an access test:

`How-to path:`

`Config path:`

`Read endpoint tested:`

`Read result:`

`Items returned:`

`Write config/status:`

`Write action tested:`

`Write result:`

`Ignore-state update:`

`Evidence/output path:`

`Blocker:`
