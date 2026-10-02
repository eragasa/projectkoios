# Architecture and execution boundary

The [owner-repository convention](index.md) keeps technical-debt observations
separate from decisions, authorization, and execution evidence.

## Observation before decision

Observed debt does not justify speculative architecture changes. Investigation
may identify questions and must-preserve behavior, but the debt record does not
select or approve a replacement.

Only after the owning authority decides a replacement boundary is the owning
architecture updated first, before replacement implementation proceeds.
Architecture publication still follows the owner's current-state rules. In
`projectkoios`, architecture, implementation, and mapped tests remain one
vertical slice, so architecture must not be committed as though absent behavior
already exists.

Component repositories follow their owning repository's architecture
convention. Technical-debt documentation does not create an alternative
architecture hierarchy, an architecture decision record, or a decision ledger.

## Authorization and execution records

Authorization remains with the applicable operator or owner. A GitHub issue,
pull request, technical-debt record, commit, or test result does not grant
permission by itself.

GitHub Issues hold mutable coordination and may record authorization already
granted by the applicable authority. Pull requests hold review discussion.
Commits, tests, and artifacts provide implementation evidence. Git history
preserves superseded implementation and documentation.

Technical-debt records may link those records but do not replicate their
status, chronology, or authority. They are not a backlog, work queue, approval
system, or acceptance result.
