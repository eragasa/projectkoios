# ADR20260629: Namespace package conversion and ingestion extraction

## Status

Accepted

## Context

ADR20260626 established the intent to move away from the monorepo structure and extract components into separate repositories. The first extraction target identified was `projectkoios-agent`.

Before the agent harness can be built, a prerequisite extraction became available: the ingestion pipeline. The ingestion code (`projectkoios.ingestion`) had been stable, unit-tested, and isolated from the rest of the mothership since the initial prototype. The `CodeRepositoryIndexer` (which coordinates ingestion with an index writer) was also tightly coupled to ingestion logic.

A technical complication arose: if extracted repos each provide a subpackage under the `projectkoios` namespace (e.g., `projectkoios.ingestion` from the ingestion repo, `projectkoios.chunking` from the mothership), the top-level `projectkoios` package must be a namespace package (PEP 420) rather than a regular package with `__init__.py`.

## Decision

1. Convert the top-level `projectkoios` package to a **PEP 420 implicit namespace package** by removing `src/python/projectkoios/__init__.py` from the mothership.

2. Extract the following code from the mothership to the `projectkoios-ingestion` repository:

   - `CodeRepositoryIngester` — coordinates a loader and chunker to produce `TextChunk` objects from a `CodeRepository`
   - `CodeRepositoryIndexer` — wires an ingester to a `ChunkIndexWriter` to index a repository
   - `ChunkIndexWriter` protocol — the output contract for ingestion consumers
   - All associated tests

3. Use **editable installs** for cross-repo resolution. The `projectkoios-ingestion` repo is installed as `pip install -e ../projectkoios-ingestion`. Both repos contribute to the `projectkoios` namespace via PEP 420.

4. Enable `namespaces = true` in `[tool.setuptools.packages.find]` in both repos' `pyproject.toml` to support namespace package discovery.

5. Keep the following shared packages in the mothership for now:

   - `projectkoios.chunking` — used by ingestion, search, and future consumers
   - `projectkoios.repositories` — used by ingestion and future consumers
   - `projectkoios.indexing` (reduced to only `InMemoryChunkIndex`) — used by runtime

## Rationale

**Namespace packages** allow multiple repositories to cooperate under a single import namespace without conflicts. This is a well-established pattern used by projects such as `google-cloud-*`, `aws-cdk.*`, and Jupyter. Each repo owns its subpackage; Python discovers them by scanning all directories on `sys.path`.

**Extracting ingestion now** rather than waiting for the agent MVP gives the repository structure a clean starting point. The ingestion code was the most stable and best-tested package in the mothership. Moving it first validates the namespace-package approach with a low-risk migration.

**Keeping shared packages in the mothership** defers the question of `projectkoios-core` until the same abstraction is used by three or more components, per the extraction rule from ADR20260626.

**Editable installs** avoid needing to publish packages to PyPI or set up a monorepo workspace during early development. Both repos remain in `~/repos/` and are linked at install time.

## Consequences

- The mothership's `pyproject.toml` now uses `namespaces = true` in `[tool.setuptools.packages.find]`
- The `projectkoios-ingestion` repo is the canonical home for ingestion pipeline code
- The mothership retains the `indexing/` package but only exports `InMemoryChunkIndex` (the search index, not the indexer)
- Any new repo that provides a `projectkoios.*` subpackage must also use `namespaces = true` and must NOT include `projectkoios/__init__.py`
- Python's namespace resolution prefers the first `projectkoios.<subpackage>` found on `sys.path`; editable install order matters if two repos ever provide the same subpackage name (which should not happen by design)

## Alternatives considered

### Keep everything in the mothership

Rejected. This contradicts ADR20260626 and would leave the ingestion code mixed with unrelated packages (API, vault, search runtime).

### Use a monorepo workspace (uv workspace, hatch workspace)

Rejected for now. The repos are already in separate git repositories with independent histories. A workspace would require restructuring the repo layout or using git submodules, adding complexity before the extraction pattern is proven.

### Remove `InMemoryChunkIndex` from the mothership along with the indexer

Rejected. `InMemoryChunkIndex` is a search index, not an ingestion concept. It stays in the mothership and will be extracted to `projectkoios-search` when that repo is populated.

### Duplicate shared code instead of using namespace packages

Rejected. Duplication would force changes to be applied in multiple places. The namespace package approach keeps imports natural (`from projectkoios.ingestion import ...`) and avoids combinatorial copy-paste.

## Next steps

- Extract `projectkoios.search` from the mothership to `projectkoios-search`
- Extract `projectkoios.api` from the mothership to `projectkoios-api`
- Build `projectkoios-workflow` with Petri-net abstractions
- Build `projectkoios-agent` with the LLM harness
