# XOS Paperclip QC Register HOWTO

**XOS Timestamp:** 2026-10-30  
**Scope:** XOS independent review register and Completed by / Reviewed by evidence projection  
**Status:** Implementation candidate for XOS-124; governed by the approved XOS-114 QC plan

## Purpose

Maintain a durable XOS review register without duplicating Paperclip's native execution and review lineage into new issue-table columns.

Paperclip already records the underlying facts in separate first-class records. XOS should project those records into a review view rather than store the same identity twice and create schema drift.

## Native evidence used

The register derives evidence from:

- heartbeat/native runs for the performing agent and run
- issue thread interactions for resolver identity, resolver run, human decisions, and review outcomes
- issue approvals for linked formal approvals
- issue work products for review state and created-by run
- work assessments and status decisions for completion/status lineage
- issue documents/interactions for approved plan revision and approval time

The core `issues` table does not currently contain `completedBy` or `reviewedBy` columns.

## Tool

`scripts/paperclip_qc_register.py`

The generator is read-only. It invokes supported Paperclip CLI reads and produces JSON and Markdown projections.

Example:

```bash
python3 scripts/paperclip_qc_register.py \
  --company-id <company-uuid> \
  --issue XOS-109 \
  --issue XOS-7 \
  --markdown-output /tmp/xos-qc-register.md \
  --json-output /tmp/xos-qc-register.json
```

## Missing non-native facts

Some required QC facts are not reliably native Paperclip fields:

- Reg's exact verbatim request and original received timestamp
- planned due/submission time when it was never encoded in Paperclip
- the applicable XOS canon/SOP revision for the work event
- explicit QC verdict when the review interaction did not record one

Supply these only from reviewed evidence through an optional JSON supplement keyed by issue identifier.

Example:

```json
{
  "XOS-109": {
    "reg_request": "Exact reviewed text",
    "reg_request_timestamp": "2026-10-25T12:00:00Z",
    "reg_request_verbatim_verified": true,
    "planned_due": "2026-10-25T16:00:00Z",
    "canon_revision": "XLR8ROS/xlr8ros-hq@<commit>",
    "canon_compliance": "PASS",
    "qc_verdict": "PASS"
  }
}
```

Do not use supplements to overwrite native `Completed by` or `Reviewed by` identity. Those fields are always projected from Paperclip evidence.

## Verdict rules

The generator is deliberately conservative.

- `FAIL_RETURN` if the same agent is both performer and reviewer.
- `HUMAN_BLOCKER` when a pending human-only interaction is the active gate.
- An explicit `PASS`, `FAIL_RETURN`, `NEEDS_EVIDENCE`, or `HUMAN_BLOCKER` may be read from the independent review result or reviewed supplement.
- Otherwise the result is `NEEDS_EVIDENCE`.

A successful model response, process exit, issue status, or unreviewed receipt never becomes PASS by itself.

## Plan approvals are not final work reviews

An accepted interaction targeting the `plan` document is recorded as plan approval only. It must not populate `Reviewed by` for completed work.

This prevents an approved plan from being mistaken for accepted implementation.

## Independence

`Completed by` is derived from successful task-bound run ownership.

`Reviewed by` is derived from the resolver identity on a non-plan review interaction.

If both resolve to the same agent, QC returns `FAIL_RETURN`. User/human review remains distinct from agent completion.

## No schema fork

Do not add duplicate `completed_by` or `reviewed_by` columns to the Paperclip `issues` table merely for XOS reporting.

If upstream Paperclip later ships first-class equivalent fields, update this projection to prefer the supported upstream fields after verifying semantics and migration behavior.

## Verification

Run:

```bash
python3 -m unittest -v tests.test_paperclip_qc_register
```

Then generate a register from known issues and compare the output against native Paperclip runs/interactions before any automated publishing is enabled.

## Publishing boundary

Generating the register is read-only.

Writing or replacing a Paperclip document must occur under a legitimate authenticated agent/run context and must be read back after persistence. A local-board/operator write is not an authenticated agent receipt.

**Operating rule:** derive facts from native evidence, preserve missing evidence as missing, and never turn status into proof.
