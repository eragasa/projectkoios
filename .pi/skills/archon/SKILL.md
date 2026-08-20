---
name: archon
description: Use when you want to run Archon workflows from Pi in this repo, inspect run status, or manage detached worktree-based automation.
---

# Archon for Pi

Use this skill when the user wants to run Archon from Pi.

## Rules

- Always use `--branch <name>` unless the user explicitly wants no isolation.
- Prefer `--detach` for long-running workflows.
- One workflow per invocation.

## Core commands

```bash
archon workflow list
archon workflow run <workflow> --branch <branch> --detach "<message>"
archon workflow status --json
archon workflow runs --json
archon workflow get <run-id> --json
```

## Common patterns

- New task: choose the matching workflow from `archon workflow list`
- Start it: run it detached with an explicit branch name
- Monitor it: use `archon workflow status` for active runs or `archon workflow runs` for history
- Inspect details: `archon workflow get <run-id> --verbose`
- Resume a failed run: `archon workflow run <workflow> --branch <branch> --resume --detach "<message>"`

## Examples

```bash
archon workflow run archon-assist --branch assist/debug-login --detach "Investigate the login bug"
archon workflow run archon-fix-github-issue --branch fix/issue-42 --detach "Fix issue #42"
archon workflow runs --status failed --limit 10
```
