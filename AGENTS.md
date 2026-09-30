# AGENTS.md — projectkoios

## Status

**Transitional mothership repo.** Per ADR20260626, implementation code is being
extracted to separate repos (`projectkoios-agent` first). `projectkoios-core` is
deferred. The current `src/python/projectkoios/` layout is provisional — it does
not match the planned subpackage structure in `docs/architecture.md`.

Repository routing is documented in `projectkoios-bootstrap/maps/repositories.md`.
This repo only owns product architecture and durable domain docs.

## Setup

```bash
python3.14 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Commands

| Action | Command |
|--------|---------|
| Run API dev server | `uvicorn projectkoios.api.main:app --reload` |
| Run all tests | `pytest` |
| Lint | `ruff check .` |
| Typecheck | `mypy src/python` |

## Package layout gotchas

- Source root is **`src/python/projectkoios/`** (two levels deep)
- Current subpackages (`agents/`, `api/`, `chunking/`, `indexing/`,
  `repositories/`, `runtime/`, `search/`, `vault/`) are **tentative** — expect
  reorganization into `core/`, `vault/`, `search/`, `references/`,
  `workflow/`, `api/` per `docs/architecture.md`, or extraction to separate
  repos per `ADR20260626`
- `core/` package does not exist yet

## Architecture rules

- **Pydantic at boundaries only** — API request/response use Pydantic. Internal
  DTOs use `@dataclass(frozen=True)`. Services never import FastAPI.
- **Thin base-object boundaries** — `BaseObject` is an architecture
  classification, not a Python class. `projectkoios.base` defines the exact
  thin ABC hierarchy for struct-like `DataObject`/`DataObjectModel` request and
  result records and function-like `DataObjectActionizer` operations. The
  actionizer is the noun that performs the action, not a required `Actionizer`
  suffix. Concrete Composer, Processor, Reconciler, Executor, Validator,
  Detector, Projector, Coordinator, Assembler, Recognizer, Checker, Ingester,
  and similar semantic agent names remain valid.
- **Helper ownership** — in touched code, private helpers belong as methods on
  the DataObject or concrete Actionizer that owns the invariant or action.
  Shared behavior gets a narrowly named collaborator, not module `_helper`
  functions or generic Utils/Helpers containers. Public module functions are
  intentional entry points or factories only.
- **Prototype persistence** — before an external, released, or irreplaceable
  durability boundary, keep one canonical format and replace/regenerate it in
  place. Git holds prototype history; numbered formats and migrations begin only
  at an explicit durability boundary. Strict shape, hashes, and deterministic
  identities still apply.
- **Adapter taxonomy** — `Adapter` is the nominal containing role. A `Binding`
  adapts imported or deliberately vendored code; an `Integration` adapts an
  external application or service. Use base classes for "is-a" relationships
  and composition for "has-a" relationships. Do not add another shared base
  class without freezing implementation for an explicit architecture review.
- **Frankenstein incubation mirror** — paths below
  `projectkoios.frankensteins` mirror intended `projectkoios` paths. Transfer
  removes only the incubation segment and does not rename domain classes or
  redesign inheritance.
- **Capability repository names** — use names such as `projectkoios-github` and
  `projectkoios-lammps`; express adapter roles in Python namespaces rather than
  repository names.
- **`dev/` is scratch** — experiments and spikes; production code never imports
  from `dev/`.
- **`from __future__ import annotations`** at top of every module.
- **ruff**: line-length=80, double quotes, lint=E/F/I/UP/B, target py314.
- **No CI workflows** exist.

## Test conventions

- pytest, files named `test__SomeName.py`, functions `test__function__description`
- API tests use `fastapi.testclient.TestClient`
- Some tests still live under `dev/spike_fastapi_app_boundary/` — not migrated yet
