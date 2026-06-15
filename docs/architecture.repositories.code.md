# Code Repository Package Architecture

## Purpose

The `projectkoios.repositories.code` package provides structured access to local code repositories.

A code repository is a local software project rooted at a directory. The first supported case is a local Python project controlled by Git.

This package loads supported repository files and returns explicit data objects for later processing.

It does not chunk, search, embed, call an LLM, build RAG prompts, expose HTTP endpoints, or modify repository contents.

## Package Boundary

The package answers:

* What repository root did the caller provide?
* Which supported files exist under that root?
* Which paths should be ignored?
* What language or file type is each file?
* What repository-relative path identifies each file?
* What raw text was loaded from each file?

The package does not decide how files are chunked, indexed, searched, ranked, cited, or passed to an LLM.

## Package Layout

```text
src/python/projectkoios/repositories/
├── __init__.py
└── code/
    ├── __init__.py
    ├── models.py
    ├── filters.py
    └── loader.py
```

## Core Objects

| Object                 | Meaning                                                              | Status  |
| ---------------------- | -------------------------------------------------------------------- | ------- |
| `CodeRepository`       | Local code project root with repository-level metadata.              | current |
| `CodeFile`             | Loaded repository file with path, relative path, text, and language. | current |
| `CodeRepositoryLoader` | Service that loads supported files from a supplied repository root.  | current |

## `CodeRepository`

```python
@dataclass(frozen=True)
class CodeRepository:
    root: Path
    name: str
    remote_url: str | None = None
```

| Field        | Type          | Meaning                                                                                 |
| ------------ | ------------- | --------------------------------------------------------------------------------------- |
| `root`       | `Path`        | Repository root directory. Defines the coordinate origin for repository-relative paths. |
| `name`       | `str`         | Repository name used in user-facing output and internal records.                        |
| `remote_url` | `str \| None` | Optional remote metadata. Local loading does not depend on this field.                  |

## `CodeFile`

```python
@dataclass(frozen=True)
class CodeFile:
    repository_root: Path
    path: Path
    relative_path: Path
    text: str
    language: str
```

| Field             | Type   | Meaning                                                                |
| ----------------- | ------ | ---------------------------------------------------------------------- |
| `repository_root` | `Path` | Absolute path to the repository root.                                  |
| `path`            | `Path` | Absolute path to the loaded file.                                      |
| `relative_path`   | `Path` | Path relative to the repository root. Used in later source references. |
| `text`            | `str`  | Raw file contents.                                                     |
| `language`        | `str`  | File language or type, such as `python`, `toml`, or `markdown`.        |

The relative path is the stable user-facing file identifier.

Use:

```text
src/python/projectkoios/api/app.py
```

not:

```text
/Users/eugene/repos/projectkoios/src/python/projectkoios/api/app.py
```

## Loader Interface

`CodeRepositoryLoader` loads files from a supplied `CodeRepository`.

The caller currently provides the repository root. The loader does not discover the root automatically.

| Method                   | Return type          | Use                                                                                                |
| ------------------------ | -------------------- | -------------------------------------------------------------------------------------------------- |
| `iter_files(repository)` | `Iterator[CodeFile]` | Normal loader interface. Yields files one at a time.                                               |
| `load(repository)`       | `list[CodeFile]`     | Convenience wrapper for tests, small repositories, and inspection. Materializes files into memory. |

`iter_files()` should be used by downstream ingestion code.

`load()` is acceptable for tests and small repositories.

## File Selection Rules

Initial supported suffixes:

| Suffix  | Language   |
| ------- | ---------- |
| `.py`   | `python`   |
| `.toml` | `toml`     |
| `.md`   | `markdown` |

Initial ignored path parts:

```python
IGNORED_PARTS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
}
```

A file is ignored if any part of its repository-relative path is in `IGNORED_PARTS`.

The ignore check should use `relative_path.parts`, not absolute `path.parts`.

## Responsibility Split

| Object                 | Input                         | Output                                   | Responsibility                                       |
| ---------------------- | ----------------------------- | ---------------------------------------- | ---------------------------------------------------- |
| `CodeRepository`       | Repository root metadata      | Data object                              | Stores repository identity and coordinate origin.    |
| `CodeRepositoryLoader` | `CodeRepository`              | `Iterator[CodeFile]` or `list[CodeFile]` | Loads supported files below the repository root.     |
| `CodeFile`             | Loaded file metadata and text | Data object                              | Stores file path, relative path, text, and language. |

Repository-root discovery is not implemented yet. If added later, it should be a separate object and not hidden inside `CodeRepositoryLoader`.

## Exclusions

This package does not:

* discover repository roots automatically
* chunk files
* search files
* rank results
* build embeddings
* call an LLM
* build RAG prompts
* expose HTTP endpoints
* read Obsidian vault semantics
* modify repository contents

## Tests

Tests belong under:

```text
tests/projectkoios/repositories/code/
```

Current test file:

```text
tests/projectkoios/repositories/code/test__CodeRepositoryLoader.py
```

Current test behaviors:

| Test                                     | Behavior                                                  |
| ---------------------------------------- | --------------------------------------------------------- |
| `test__load__discovers_python_files`     | Loads `.py` files.                                        |
| `test__load__discovers_pyproject_toml`   | Loads `pyproject.toml`.                                   |
| `test__load__discovers_markdown_files`   | Loads `.md` files.                                        |
| `test__load__ignores_venv`               | Ignores `.venv`.                                          |
| `test__load__ignores_git_directory`      | Ignores `.git`.                                           |
| `test__load__returns_relative_paths`     | Computes paths relative to the repository root.           |
| `test__load__skips_unsupported_suffixes` | Skips unsupported file types.                             |
| `test__iter_files__yields_code_files`    | Yields `CodeFile` objects through the iterator interface. |

Tests should use temporary directories and should not depend on the real Project Koios repository.

## Package Invariant

The `projectkoios.repositories.code` package is valid when it can load supported files from a supplied local code repository root, preserve repository-relative paths, ignore unsupported or excluded files, and return explicit data objects without performing downstream processing.
