# AAR 20260701.130700: Architecture docs updated for agents incubation

## Scope

Updated the mothership architecture docs to describe the new `projectkoios.agents` incubation namespace and workspace/action model.

## What happened

Added an `Agents Incubation` section to `docs/architecture.md`, linked to a new `docs/architecture.agents.md` note, and updated the namespace/layout references so the architecture docs match the code layout.

## Process issues

- The new agents package needed explicit architecture documentation after code landed.
- The architecture document’s tree and related-links section had drifted from the actual package layout.

## Proposed follow-up improvements

- Keep the incubation note and the main architecture doc synchronized when `projectkoios.agents` changes.
- Decide whether `AgentWorkspaceAction` should stay generic or be split into specialized action types later.

## Candidate ADR or implementation topics

- Formal lifecycle for agent workspace state.
- Stable action-object naming for workspace records.

## Current status

Complete.
