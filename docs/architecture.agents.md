# Agents incubation and extraction boundary

## Status

Accepted; workspace extraction is deferred.

## Context

Project Koios has two intentionally different agent namespaces:

- `projectkoios.agent` is supplied by the `projectkoios-agent` repository and
  contains reusable agent-domain components with demonstrated boundaries.
- `projectkoios.agents` is a mothership incubation namespace for persistent
  workspace state under `src/python/projectkoios/agents/`.

The extracted repository already owns the bounded literature-review assessment
component. Its existence does not make every object with "agent" in its name
part of that repository.

The mothership workspace prototype currently contains:

- `AgentWorkspace` — an immutable workspace data object; and
- `AgentWorkspaceAction` — an action object that renders and writes state,
  session, decision, and handoff artifacts.

## Current ownership decision

Keep `projectkoios.agents` in the mothership during incubation. Do not copy or
move it to `projectkoios-agent` yet.

The workspace package is isolated and tested, but no production consumer in an
independent repository uses its public API. Its filesystem records may also be
a Project Koios-specific coordination concern, which would make
`projectkoios-bootstrap` the incubation owner under the
[bootstrap Pi harness incubation ADR](adr.20260918.bootstrap-pi-harness-incubation.md)
rather than `projectkoios-agent`.

The plural `projectkoios.agents` namespace is not a compatibility alias for the
singular `projectkoios.agent` namespace. A future move must choose an explicit
stable target API instead of allowing both repositories to provide the same
subpackage.

## Extraction readiness

| Gate | Current evidence | Result |
|---|---|---|
| Isolated implementation and tests | The package uses only the standard library and has focused tests. | Met |
| Independent reuse | References outside the package are documentation and its mothership tests. | Not met |
| Stable domain boundary | Workspace records may be agent-domain state or bootstrap coordination artifacts. | Not met |
| Stable public API and namespace | The generic action type and plural namespace are still incubation choices. | Not met |
| Target-repository acceptance | No accepted target contract covers workspace lifecycle or record semantics. | Not met |

Passing the technical isolation gate alone is insufficient. The ownership and
reuse gates prevent a premature extraction.

## Migration checklist

Use this checklist when an independent consumer demonstrates the boundary:

1. Record the consumer and the concrete workspace behavior it reuses.
2. Decide whether the behavior is reusable agent-domain logic or a
   Project Koios-specific Pi coordination helper.
3. Select the owner from that decision:
   `projectkoios-agent` for a stable reusable component, or
   `projectkoios-bootstrap` for harness incubation.
4. Define the target import path, workspace lifecycle, overwrite behavior,
   path-safety rules, serialization format, and compatibility policy.
5. Split rendering from filesystem mutation if consumers need either behavior
   independently; do not preserve `AgentWorkspaceAction` solely for source
   compatibility.
6. Add the implementation and focused tests to the target repository without
   creating a second provider of the same `projectkoios` subpackage.
7. Migrate every real consumer to an explicit dependency on the target
   repository and run a cross-repository editable-install smoke test.
8. Remove `src/python/projectkoios/agents/` and
   `tests/test__AgentWorkspace.py` from the mothership in the coordinated
   cleanup change.
9. Update this note, `docs/architecture.md`, the target repository boundary
   document, and the bootstrap repository map if repository topology changes.
10. Run `pytest`, `ruff check .`, and `mypy src/python` in every changed Python
    repository before declaring the move complete.

Stop the migration if there is still only one consumer, ownership remains
ambiguous, or the target would need to depend on mothership implementation
code.

## Consequences

- Workspace state retains one implementation owner while its boundary is
  tested by use.
- `projectkoios-agent` remains limited to demonstrated reusable agent-domain
  components.
- Project-specific harness prototypes remain eligible for bounded incubation
  in `projectkoios-bootstrap` rather than being promoted by name alone.
- The workspace model does not replace the repository map in
  `projectkoios-bootstrap/maps/repositories.md`.
