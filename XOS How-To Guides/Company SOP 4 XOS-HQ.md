# GitHub Access How-To

## Purpose
This how-to defines how XOS agents access GitHub correctly.

It exists so agents do not confuse GitHub MCP access, `gh` CLI access, and plain `git` access.

## 1. Approved GitHub access paths

XOS currently recognizes three separate GitHub access paths:

1. GitHub MCP
2. `gh` CLI
3. `git` remote access

These are separate access paths.

Authentication in one path does not guarantee authentication in another.

## 2. Default rule

Unless explicitly instructed otherwise, agents should use GitHub MCP as the default GitHub access path.

Agents must not assume that working GitHub MCP access means that `gh` CLI is authenticated.

Agents must not assume that working `gh` CLI access means that plain `git` push/pull credentials are configured.

## 3. GitHub MCP procedure

Use GitHub MCP when the task requires:

1. repo inspection
2. repo visibility checks
3. issue or PR inspection
4. controlled GitHub tool usage inside the approved runtime

Before relying on GitHub MCP, confirm:

1. the GitHub MCP server is configured in the active runtime
2. the runtime can see the GitHub MCP tools
3. the authenticated GitHub identity has access to the required org or repo

If GitHub MCP works, prefer it over unauthenticated terminal fallbacks.

## 4. `gh` CLI procedure

Use `gh` CLI only when:

1. the active runtime explicitly supports terminal GitHub work
2. `gh` is authenticated in that shell
3. the task specifically benefits from CLI usage

Check auth with:

1. `gh auth status`

If unauthenticated, use one of these approved paths:

1. `gh auth login`
2. provide `GH_TOKEN` in the active shell if approved

If `gh` is unauthenticated, do not treat that as proof that GitHub access is fully broken.

It only proves that the `gh` CLI path is not authenticated in that shell.

## 5. Plain `git` procedure

Use plain `git` only when:

1. the repo already exists locally
2. the correct remote is configured
3. the active runtime has valid HTTPS credentials or SSH key access

If plain `git` fails, identify whether the failure is:

1. repo path problem
2. remote URL problem
3. credential problem
4. permission problem

Do not confuse plain `git` failure with MCP failure or `gh` failure.

## 6. Verification sequence

When GitHub work fails, verify in this order:

1. which access path is being used
2. whether that path is authenticated
3. whether the authenticated identity has repo access
4. whether the active runtime actually exposes that path

## 7. Escalation rule

Escalate when:

1. the required GitHub path is unavailable
2. auth cannot be completed in the active runtime
3. repo visibility conflicts with expected access
4. the task requires a more privileged path than currently approved

## 8. Working rule

When reporting GitHub failure, state exactly which path failed:

1. GitHub MCP
2. `gh` CLI
3. plain `git`

Do not report “GitHub is broken” unless all relevant access paths are actually failing.