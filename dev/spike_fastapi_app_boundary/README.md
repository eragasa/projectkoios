# FastAPI App Boundary Spike

This spike verifies the initial FastAPI application boundary for Project Koios.

It tests:

- ASGI app export through `main.py`
- Application composition through `ProjectKoiosApp`
- App factory construction through `create_app()`
- Route registration through router factories
- Service injection into routers
- Pydantic request and response models
- A minimal `/search` contract using in-memory data
- A module layout that can later be promoted into `src/python/projectkoios/`

## Status

| Path | Responsibility | Promotion target |
|---|---|---|
| `main.py` | ASGI export only. Imports `create_app()` and exposes `app` for `uvicorn`. | `projectkoios/api/main.py` |
| `app.py` | Composition root: builds the FastAPI app, owns services, and includes routers. | `projectkoios/api/app.py` |
| `config.py` | Application configuration: app configuration plus subsystem configuration such as vault and database configuration. | `projectkoios/api/config.py` initially; possibly `projectkoios/core/config.py` later. |
| `models.py` | API boundary models: request and response schemas. | `projectkoios/api/models.py` |
| `services.py` | Application services used by the API spike. | Split into domain packages such as `projectkoios/search/`, `projectkoios/vault/`, or `projectkoios/workflow/`. |
| `routers/` | HTTP interface modules. | `projectkoios/api/routers/` |
| `routers/core.py` | Root and health endpoints. | `projectkoios/api/routers/core.py` |
| `routers/search.py` | Search endpoint wiring. | `projectkoios/api/routers/search.py` |

## Run

From the repository root:

```bash
python -m uvicorn dev.spike_fastapi_app_boundary.main:app --reload
```

## Endpoints

```\text
GET /
GET /health
POST /search
```

## Development Checks

Run these checks before promoting spike code into `src/python/projectkoios/`.

| Tool | Purpose | Command |
|---|---|---|
| `ruff` | Linting, import checks, formatting, and simple bug patterns. | `python -m ruff check .` |
| `pytest` | Runtime behavior tests. | `python -m pytest -vv` |
| `mypy` | Static type checking. | `python -m mypy .` |

For the current FastAPI spike:

| Tool | Command |
|---|---|
| `ruff` | `python -m ruff check dev/spike_fastapi_app_boundary` |
| `pytest` | `python -m pytest -vv dev/spike_fastapi_app_boundary` |
| `mypy` | `python -m mypy dev/spike_fastapi_app_boundary` |