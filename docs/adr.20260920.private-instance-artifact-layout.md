# ADR20260920: Private instance artifact layout

## Status

Proposed and implemented as a non-destructive local prototype. This proposal
does not authorize migration, deletion, publication, or mutation of a source
vault.

## Context

Project Koios currently has private extraction artifacts under
`~/projectkoios/.koios`, an exploratory RAG database under a separate subtree,
and citation-review state under `~/.local/share/projectkoios`. Source PDFs may
reside in an Obsidian vault, a cloud-synchronized folder, or another controlled
collection.

The intended document pipeline produces several artifacts with different
semantics:

```text
source PDF
  -> literal transcript
      -> transcript chunk set
      -> document distillation
          -> distillation chunk set
```

Source bytes, transcript evidence, generated interpretation, rebuildable search
indexes, and mutable human review state must not be confused merely because
they share a filesystem. The accepted reference-authority architecture also
requires immutable historical records and treats SQLite as a rebuildable
projection rather than historical authority.

## Proposed decision

A Project Koios deployment uses one explicitly configured private data root.
The initial local prototype uses:

```text
~/projectkoios/.koios/store-v1
```

The path is machine-local configuration, not a repository constant. A
machine-local TOML file is the primary configuration source. CLI and environment
values may override it for bounded runs.

The store has these top-level roles:

```text
store-v1/
├── blobs/          # content-addressed immutable payload bytes
├── records/        # immutable observations and manifests
├── collections/    # deterministic corpus-membership projections
├── artifacts/      # immutable extraction and derivation generations
├── projections/    # disposable databases and exported views
├── state/          # mutable local human/application state
└── staging/        # incomplete atomic writes; never retrieval input
```

### Source bytes

Acquisition reads the configured source locator without changing it. The exact
bytes are copied into the local content-addressed store before durable
processing:

```text
blobs/sha256/<first-two-hex>/<full-sha256>
records/sources/<source-sha256>/manifest.json
records/source-origins/<origin-observation-sha256>.json
```

The source manifest records byte identity, media type, size, and blob location.
A separate origin observation records the private vault-relative locator,
access mode, instance, and observed source identity. A source locator is
provenance, not identity. Identical bytes from multiple locations share one
blob while retaining separate immutable origin observations.

A managed byte snapshot is preferred over a locator-only record. It permits
replay if a cloud file moves, changes, becomes unavailable, or is evicted from
local storage. The cloud or vault copy remains an acquisition origin and is not
rewritten by ingestion.

### Immutable generations

Each derivation is written to a new identity-bearing directory and finalized
atomically:

```text
artifacts/extractions/<extraction-id>/
    manifest.json
    document.json
    pages/page-000001.json

artifacts/transcripts/<transcript-id>/
    manifest.json
    transcript.jsonl
    transcript.txt
    pages/page-000001.json

artifacts/chunksets/transcript/<chunkset-id>/
    manifest.json
    chunks.jsonl

artifacts/distillations/<distillation-id>/
    manifest.json
    distillation.json
    distillation.md

artifacts/chunksets/distillation/<chunkset-id>/
    manifest.json
    chunks.jsonl
```

Extraction, transcript, chunk-set, and distillation identities bind exact
upstream identities, schema and implementation versions, configuration, and
payload hashes. Existing finalized generations are never overwritten. A
correction or supersession is a new record.

Transcript chunks retain exact transcript spans, source block identities,
physical pages, and bounding boxes where available. Distillation statements
retain links to supporting transcript spans. Distillation chunks are a separate
retrieval role and cannot silently become source evidence.

### Collections

Collections name corpus membership without duplicating artifact bytes:

```text
collections/<instance>/<collection>/manifest.json
collections/<instance>/<collection>/documents/<logical-name>.json
```

A collection document is a projection that points to source and accepted
processing identities. A filename or proposed citekey is display metadata; it
does not establish canonical bibliographic identity.

### Projections and state

Rebuildable retrieval databases live under:

```text
projections/search/<instance>/<index-id>/index.sqlite3
```

An index manifest binds its exact transcript or distillation chunk sets,
retrieval configuration, schema, and implementation version. Deleting an index
must not destroy source, transcript, distillation, or human-decision history.

Mutable application state is isolated from immutable records:

```text
state/reviews/<instance>/reviews.sqlite3
state/runs/<run-id>/
```

Human review revisions should also produce append-only decision records when
that contract is implemented. A mutable SQLite database is only the current
working projection.

### Security and filesystem policy

- The store root and directories use mode `0700`.
- Private payloads, manifests, and SQLite files use mode `0600`.
- Symlinked inputs and destinations are rejected.
- Writes use a same-filesystem temporary destination followed by atomic rename.
- A different existing payload at an immutable destination fails closed.
- Private paths and excerpts do not enter Git, public issue text, or public
  logs.
- `staging/` is never indexed and may be garbage-collected after bounded
  recovery checks.

## Configuration

The default machine-local configuration location is:

```text
~/.config/projectkoios/config.toml
```

Example:

```toml
schema_version = 1
data_root = "~/projectkoios/.koios/store-v1"

[instances.dlsu]
vault_root = "~/Library/CloudStorage/.../My Drive/DLSU"
source_access = "read_only"
```

Resolution precedence is:

1. explicit CLI option;
2. environment override;
3. machine-local configuration;
4. fail closed for writes when no root is configured.

The environment may point to an alternate configuration using `KOIOS_CONFIG`.
`KOIOS_DATA_ROOT` remains a bounded override, not the durable authority.

## Initial prototype boundary

The local prototype may create the store skeleton, content-addressed source
snapshots, separate origin observations, and an immutable collection generation
without moving existing artifacts. The initial DLSU generation inventories all
regular PDF files below the configured `03_references` root. Existing extraction
directories, RAG databases, and review databases remain authoritative only for
their current prototype workflows until a concrete migration inventory and
replay validation exist.

A future migration must:

1. inventory every existing private artifact and source identity;
2. classify it as immutable evidence, rebuildable projection, mutable state, or
   disposable scratch;
3. regenerate from authoritative inputs where possible rather than copying
   ambiguous products;
4. compare counts, hashes, search behavior, and review state;
5. switch readers only after validation; and
6. delete nothing without separate authorization.

## Consequences

- Source PDFs remain untouched in their owning vaults or cloud folders.
- Exact source bytes remain replayable through local content-addressed
  snapshots.
- Literal transcripts and distillations can coexist without sharing evidence
  authority.
- Multiple chunking experiments do not require retranscription or redistillation.
- Search indexes remain disposable and independently reproducible.
- Current private artifacts are temporarily split across old and new layouts
  until an explicit migration is implemented.
