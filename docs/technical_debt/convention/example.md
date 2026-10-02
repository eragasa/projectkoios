# Technical debt example

This example applies the [record guidance](records.md). Its names and paths are
illustrative and are not claimed to exist.

## Duplicate export normalization

Two export adapters independently normalize the same record shape, and no
owning boundary has been decided.

### Evidence and current impact

`src/example_export/primary.py` and
`src/example_export/archive.py` contain separate normalization paths.
`tests/test_export_replay.py` fixes the currently matching byte output. The code
locations are direct evidence; future divergence is a risk inferred from the
duplication.

Every normalization correction must be reviewed and applied in two places, and
replay tests can detect drift only after it occurs.

### Owners and must-preserve behavior

The export component owns both paths. The example reader owns compatibility
expectations but does not approve export changes.

UTF-8 output, stable field ordering, and the reader's accepted record shape
remain unchanged unless separately authorized.

### Non-goals and investigation scope

This observation does not propose redesigning the record schema, adding a
migration framework, or changing reader policy.

Investigation compares both paths and fixtures, identifies the narrowest single
owner for normalization, and determines whether either adapter has a necessary
distinct rule.

### Exit criteria

The owning boundary is decided and reflected in current architecture; mapped
tests preserve required output; the duplicate path is removed or justified as
distinct; and this observation is then removed or rewritten to match the
remaining condition.
