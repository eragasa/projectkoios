# AGENTS.md — projectkoios

## Status

**Transitional mothership repo.** Per ADR20260626, implementation code is being
extracted to separate repos (`projectkoios-agent` first). `projectkoios-core` is
deferred. The current `src/python/projectkoios/` layout is provisional — it does
not match the planned subpackage structure in `docs/architecture.md`.

## Setup

```bash
python3.12 -m venv .venv && source .venv/bin/activate
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
- Current subpackages (`api/`, `chunking/`, `indexing/`, `repositories/`,
  `runtime/`, `search/`, `vault/`) are **tentative** — expect reorganization
  into `core/`, `vault/`, `search/`, `references/`, `workflow/`, `api/` per
  `docs/architecture.md`, or extraction to separate repos per `ADR20260626`
- `core/` package does not exist yet

## Architecture rules

- **Pydantic at boundaries only** — API request/response use Pydantic. Internal
  DTOs use `@dataclass(frozen=True)`. Services never import FastAPI.
- **`dev/` is scratch** — experiments and spikes; production code never imports
  from `dev/`.
- **`from __future__ import annotations`** at top of every module.
- **ruff**: line-length=80, double quotes, lint=E/F/I/UP/B, target py312.
- **No CI workflows** exist.

## Test conventions

- pytest, files named `test__SomeName.py`, functions `test__function__description`
- API tests use `fastapi.testclient.TestClient`
- Some tests still live under `dev/spike_fastapi_app_boundary/` — not migrated yet
