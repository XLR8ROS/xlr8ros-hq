# Codi How-To Spawn Sub-Agents

## Purpose
This how-to defines how Codi should spawn sub-agents correctly and how to retry a failed spawn without repeating the same malformed payload.

It is intended to prevent fake retries, contaminated payload reuse, and governance-breaking sloppiness during sub-agent execution.

---

## 1. Core Rule
When spawning a sub-agent, build the payload for the actual runtime being used.

Do not assume fields from one runtime are valid for another.

If a spawn fails because of payload structure, do not reuse the failed payload as the basis for the retry.

---

## 2. Spawn Cleanly
When creating a sub-agent spawn:

1. confirm the runtime first
2. build the payload for that runtime only
3. include only fields that are valid and needed
4. avoid carrying over convenience fields from other spawn types
5. check the final payload before sending

The goal is not to retry fast.
The goal is to spawn correctly.

---

## 3. Runtime Boundary Rule
ACP and sub-agent spawns do not share identical payload rules.

A field that is valid for ACP may be invalid for a normal sub-agent spawn.

Codi must treat runtime-specific payload fields as runtime-specific, not universal.

If the runtime is `subagent`, the payload must be checked against sub-agent-valid fields only.

---

## 4. Retry Rule
If a sub-agent spawn fails:

1. read the exact error
2. identify the exact invalid field, structure, or assumption
3. stop the retry loop
4. discard the failed payload completely
5. rebuild the new payload from scratch
6. keep the retry minimal
7. verify the rebuilt payload before sending
8. retry only after verification

Do not perform a cosmetic retry.
Do not perform a confidence retry.
Do not perform a “same payload but I think it is fixed” retry.

A retry is only valid if the broken payload has been cleared and replaced by a newly built payload.

---

## 5. Clear the Old Payload
When a spawn payload is found to be malformed, the old payload must be treated as contaminated.

Codi must:

1. clear the old payload
2. get rid of it entirely
3. avoid copying the malformed structure forward
4. rebuild from a blank-good starting point

Do not patch around a bad payload if the error shows the payload shape itself is compromised.

The failed payload is not a safe template.

---

## 6. Verification Before Retry
Before retrying, verify:

1. the runtime is correct
2. the invalid field is absent
3. no runtime-incompatible fields remain
4. the payload is minimal and intentional
5. the retry actually differs from the failed call in the required way

If this verification has not happened, the retry is not ready.

---

## 7. Anti-Sloppiness Rule
Understanding the error is not enough.

Intent to fix is not enough.

Saying “I removed it” is not enough.

The payload itself must be correct.

Codi must not confuse recognition of the fix with execution of the fix.

---

## 8. Escalation Rule
If repeated spawn failures occur and the same structural mistake repeats, Codi must:

1. stop retrying automatically
2. report the exact repeated failure
3. state that the retry process itself is compromised
4. rebuild from a blank payload or ask for direction before continuing

Repeated malformed retries are an execution failure, not progress.

---

## 9. Completion Standard
A sub-agent spawn attempt is only complete when one of these is true:

1. the sub-agent launched successfully
2. the spawn is blocked for a clearly stated reason
3. the retry path was halted and escalated cleanly

Repeated malformed calls do not count as meaningful execution.

---

## 10. Practical Rule to Remember
If the previous spawn payload failed because of structure:

**clear the old payload, get rid of it, and rebuild from scratch before retrying.**

---

## Runtime Persistence Check

When a sub-agent is intended to watch, witness, or stay active, verify actual persistence by runtime behavior, not by the sub-agent saying it is active. A completed sub-agent response means the task ended unless the runtime shows an ongoing process, watch loop, session, or external watcher.

For live witness or videographer-style work, use a real keep-alive/watch mechanism when the runtime supports it. If the runtime only supports one-shot tasks, capture that limitation in the phase report and use the parent agent or another verified mechanism for ongoing capture.

