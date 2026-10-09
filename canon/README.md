# XOS Global Canon

This directory contains machine-readable canonical sources for XOS material whose scope is global.

## Rule

If a governing artifact is global, its canonical source lives here as YAML.

Human-readable Markdown copies retain the governing document's exact filename and content. They are synchronized copies, not independent authorities.

The synchronization model is:

`canonical YAML -> synchronized HQ Markdown -> synchronized downstream copies`

A synchronized downstream copy may live in an agent repository for bootstrap resilience. The document itself must not be renamed, branded, or modified to describe synchronization metadata; that metadata belongs in HQ infrastructure.

## Drift Rule

A synchronized copy that differs from its canonical YAML is stale or corrupted. The YAML wins.

Do not reconcile divergent copies by hand. Regenerate them from the canonical source.

## Current Migration State

- Global Memory Contract: migrated to canonical YAML
- Constitution: migrated to canonical YAML; Markdown copies retain the canonical document name and content
- XOS HQ Company SOP: migrated to canonical YAML
- Administrative Services SOP: migrated to canonical YAML

Do not create placeholder governing content merely to satisfy the directory structure.
