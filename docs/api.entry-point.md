# Project Koios API Entry Point

Project Koios exposes its FastAPI application through an ASGI entry point.

## ASGI Entry Point

```python
# src/python/projectkoios/api/main.py

from projectkoios.api.app import ProjectKoiosApp


app = ProjectKoiosApp.create_app()
```

The application is served with:

```bash
python -m uvicorn projectkoios.api.main:app --reload
```

## Import String

| Part                    | Meaning                                                   |
| ----------------------- | --------------------------------------------------------- |
| `projectkoios.api.main` | Python module imported by `uvicorn`.                      |
| `app`                   | Module-level ASGI application object inside `main.py`.    |
| `--reload`              | Restarts the development server when source files change. |

## File Responsibilities

| File                        | Responsibility                                            |
| --------------------------- | --------------------------------------------------------- |
| `projectkoios/api/main.py`  | Exposes the module-level ASGI app object.                 |
| `projectkoios/api/app.py`   | Builds the FastAPI application through `ProjectKoiosApp`. |
| `projectkoios/api/routers/` | Contains HTTP route modules.                              |

## Rule

`main.py` stays small.

It does not define routes, construct services manually, or contain domain behavior. Application construction belongs in:

```text
projectkoios.api.app.ProjectKoiosApp
```

For the general ASGI concept, see:

```text
[[Python.Web.ASGI]]
```
