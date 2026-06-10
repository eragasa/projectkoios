# Hello World First Spike

This spike verifies the smallest useful FastAPI application boundary for Project Koios.

The spike is intentionally outside the installed `projectkoios` package. Once the app boundary is clear, stable code can be promoted into:

```text
src/python/projectkoios/
```

## Run

from this directory:

```bash
uvicorn main:app --reload
```

