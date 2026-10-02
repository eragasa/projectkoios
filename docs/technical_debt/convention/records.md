# Technical debt records

The [owner-repository convention](index.md) uses durable records for observed
conditions, not speculative plans or mutable task state.

## When to create a record

Create a record when current, inspectable evidence demonstrates a maintenance
cost, correctness risk, ownership gap, or replacement constraint that should
survive beyond one issue or pull request. Do not create one merely to preserve
an idea, proposed design, speculative concern, task checklist, or transient
implementation note.

A record describes an observed condition and the boundary of useful
investigation. It does not decide the replacement, authorize work, assign
priority, grant approval, or establish that affected behavior may change.

## Content guidance

A useful record covers the following information. Authors may combine, rename,
or reorder headings when the meaning remains explicit; this is guidance, not a
rigid document schema.

- **Observation** — the current condition, without presenting a replacement as
  decided.
- **Evidence** — repository-relative code, test, contract, document, failure,
  measurement, or immutable artifact identities that support the observation.
  Direct evidence is distinguished from inference.
- **Current impact** — the present maintenance cost, failure mode, risk, or
  constraint rather than a hypothetical future benefit.
- **Affected owners** — the repositories, components, or human authority
  boundaries affected. Naming an owner does not assign work or approval.
- **Must-preserve behavior** — current compatibility, safety, scientific,
  privacy, data, or user-visible behavior that investigation and replacement
  must not silently lose.
- **Non-goals** — adjacent redesign, migration, cleanup, or policy questions
  excluded from the record.
- **Investigation scope** — the bounded questions and evidence needed before a
  replacement boundary can be decided.
- **Exit criteria** — observable conditions under which the record is removed
  or rewritten because the debt is resolved, disproved, accepted as current
  architecture, or split into separately owned observations.

## Record maintenance

Do not add mutable progress logs, assignee state, queues, approval fields, or
copied issue histories. Link an execution record when useful instead of
replicating its status or chronology.

When exit criteria are met, update or remove the current debt record in the
owning repository. Git history preserves the superseded observation; do not
retain a tombstone solely to narrate its history.
