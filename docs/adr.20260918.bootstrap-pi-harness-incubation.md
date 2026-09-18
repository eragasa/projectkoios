# ADR20260918: Bounded bootstrap ownership of Project Koios Pi harness incubation

## Status

Accepted

## Context

`projectkoios-bootstrap` originally served as the Project Koios meta-harness
repository. Before revision `4d5c8c0b`, it combined harness configuration,
agent-role workspaces, workflow engines, daemons, schemas, operator-console
code, product prototypes, generated state, and extensive process documents.
That revision correctly reduced a 1,270-file monolith to a minimal
multi-repository coordination cockpit.

The reduction also removed an owner for unstable, Project Koios-specific Pi
coordination tooling. The remaining ownership model placed generic Pi
extensions in the operator installation and reserved `projectkoios-agent` for
reusable agent-domain components with a demonstrated stable extraction
boundary. Neither location owns early Project Koios coordination candidates.

A references adversarial-review campaign demonstrated the gap. The bounded
coordination sequence generated independently scoped issues, created them with
partial-progress recovery, updated a parent, cross-linked owner repositories,
and verified completeness and public-record privacy. One-off helpers in
`/tmp` provided prototype evidence, but temporary storage cannot support later
comparison or extraction.

Versioned harness source and sanitized fixtures are not the same as live
orchestration state. Preventing task databases, transcripts, queues,
checkpoints, daemons, and telemetry does not require discarding bounded harness
candidates.

## Decision

`projectkoios-bootstrap` owns development and validation of the **Project
Koios-specific Pi coordination harness**.

It may contain:

- bounded coordination helpers;
- Project Koios-specific Pi skills and prompt templates;
- deterministic repository, issue, session, and recovery utilities;
- sanitized workflow fixtures and tests;
- explicit harness-candidate manifests and limitations; and
- experimental candidates awaiting evidence of independent reuse.

It does not own:

- Project Koios product or scientific-domain logic;
- implementation already assigned to a component repository;
- roadmap or task databases, replicated owner state, session transcripts,
  persistent queues, checkpoints, or generated handoffs;
- daemons, telemetry services, generic workflow engines, schema catalogs,
  installers, or operator consoles;
- the historical Hermes/Athena/Vulcan/Koios role system;
- credentials or machine-specific configuration; or
- stable generic Pi extensions that belong in the operator installation or an
  extracted owner repository.

GitHub issues, Git commits, owner documents, and owner artifacts remain the
durable project and task records. Private, generated, or machine-bound harness
observations remain under managed operational state and may be referenced by
content identity without publishing their paths or contents.

## Candidate lifecycle

A harness candidate advances through independently recorded states:

1. **Observed** — one bounded coordination instance exists.
2. **Candidate** — sanitized source, fixtures, limitations, and private
   observation identity are preserved.
3. **Repeated** — a second independent instance exercises substantially the
   same coordination sequence.
4. **Validated** — deterministic tests and at least one failure/recovery case
   pass.
5. **Extracted or retained** — stable generic tooling moves to its proper
   owner; Project Koios-specific tooling may remain in bootstrap.

One occurrence permits preservation and candidate analysis. It does not by
itself authorize production promotion, persistent runtime instrumentation, or
a generalized workflow engine.

## Consequences

- `projectkoios-bootstrap` again has a narrow harness-incubation responsibility
  without recovering the historical monolith.
- Source code, fixtures, and tests are distinguished from prohibited runtime
  state.
- Project-specific coordination behavior can be reviewed and reproduced in
  Git before it becomes generic tooling.
- Stable generic Pi extensions remain outside the bootstrap repository.
- Cross-repository product architecture remains in `projectkoios`; component
  implementation remains in component repositories.
- Bootstrap instructions and the task/recovery policy must describe this
  boundary consistently.

## Alternatives considered

### Keep bootstrap routing-only and discard one-off helpers

Rejected. It prevents durable comparison of emerging Project Koios
coordination patterns and leaves no incubation owner.

### Put every prototype directly in the operator Pi installation

Rejected. Project-specific candidates would become machine-bound and difficult
to review, reproduce, or extract without first demonstrating generic value.

### Restore the historical meta-harness

Rejected. The former repository mixed product code, roles, runtime state,
daemons, workflow engines, and interfaces far beyond a bounded coordination
harness.

### Put early candidates in `projectkoios-agent`

Rejected for now. That repository is reserved for reusable agent-domain
components after a stable extraction boundary is demonstrated.

## Authority and follow-up

The operator authorized this bounded recommendation. Implementation is tracked
by:

- https://github.com/eragasa/projectkoios/issues/4
- https://github.com/eragasa/projectkoios-bootstrap/issues/2

This decision does not authorize commit, push, release, extension
installation, telemetry, daemon creation, historical restoration, or
production promotion.
