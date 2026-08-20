# Agents Incubation

## Status

accepted

## Context

Project Koios is adding an incubation namespace for persistent agent workspace
state under `src/python/projectkoios/agents/`.

The immediate goal is to model per-agent workspace state as a data object and a
workspace action object that can render or write session, state, decision, and
handoff artifacts.

This is an incubation area under the mothership repo, not a shared extracted
component yet.

## Decision

Use `projectkoios.agents` as the incubation namespace for:
- `AgentWorkspace` — immutable workspace data object
- `AgentWorkspaceAction` — action object for workspace updates and records

Keep these objects small and filesystem-oriented until the design stabilizes.

## Consequences

- Agent-specific session state can live in one consistent package during
  incubation.
- The design remains simple enough to extract later if it becomes shared
  across repos.
- The workspace model does not replace `maps/` or `docs/agent-charter.md`.
