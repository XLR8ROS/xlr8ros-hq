# XOS Global Canon

This directory contains machine-readable canonical sources for XOS material whose scope is global.

## Rule

If a governing artifact is global, its canonical source lives here as YAML.

Human-readable Markdown copies are generated mirrors. They are not independent authorities and must not be hand-edited as competing sources.

The synchronization model is:

`canonical YAML -> generated HQ Markdown -> registered downstream mirrors`

A downstream mirror may be local to an agent repository for bootstrap resilience, but its content is derived from the canonical YAML and must identify its source.

## Drift Rule

A mirror that differs from its canonical YAML is stale or corrupted. The YAML wins.

Do not reconcile divergent mirrors by hand. Regenerate them from the canonical source.

## Current Migration State

- Global Memory Contract: migrated to canonical YAML
- Constitution: canonical source not currently present in this repository; recover the authoritative source before migration
- SOPs: canonical global SOP YAML sources not currently present in this repository; recover authoritative sources before migration

Do not create placeholder governing content merely to satisfy the directory structure.
