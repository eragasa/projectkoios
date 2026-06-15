# Repository Architecture
Project Koios treats a repository as the first source object for the RAG-supported LLM coder MVP.  A repository is a local project workspace containing source files, configuration files, documentation, tests, and metadata that together define a software project.  It is also a folder.

At the current time, Project Koios is focusing on python projects that are version controlled by git.
## Purpose
The repository layer provides structured access to local source code.   But likely has a global remote source.

- What is the project root? 
- What files belong to the project?
- Which files should be ignored?
- What language or file type is each file?
- What relative path should be shown to the user?
- What text should be passed to chunking, search, and RAG?

The repository layer does not perform search, chunking, embedding, or LLM calls. It only identifies and loads repository files.

## Position in the RAG Pipeline

```text
repository root
    ↓
RepositoryLoader
    ↓
RepositoryFile[]
    ↓
Chunker
    ↓
TextChunk[]
    ↓
SearchService
    ↓
SearchHit[]
    ↓
RAGPromptBuilder
    ↓
LLMService
    ↓
answer + sources
```

The repository layer is the input boundary for code understanding.

## Core Concepts

|Concept|Meaning|
|---|---|
|`Repository`|A local project root with project-level metadata.|
|`RepositoryFile`|A file loaded from a repository, with path, relative path, text, and language.|
|`RepositoryLoader`|A service that discovers and loads supported files from a repository root.|
|`RepositoryInspector`|A later service that detects project type, source roots, package names, remotes, branch, and commit metadata.|

## Repository

A `Repository` represents the project root and project identity.

Initial model:

```python
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Repository:
    root: Path
    name: str
    remote_url: str | None = None
```

The repository object should stay small at first.

It should not become a large inheritance hierarchy such as:

```python
class Repository:
    pass


class GithubRepository(Repository):
    pass


class PythonGithubRepository(GithubRepository):
    pass
```

That hierarchy mixes independent axes:

|Axis|Examples|
|---|---|
|Location|local, GitHub, GitLab|
|Language|Python, TypeScript, Rust|
|Shape|package, monorepo, docs repo|
|Role|source repo, teaching repo, tool repo|

Project Koios uses composition instead of deep inheritance.

A Python GitHub repository is represented as a repository with metadata, not as a subclass.

```python
Repository(
    root=Path("/Users/eugene/repos/projectkoios"),
    name="projectkoios",
    remote_url="https://github.com/projectkoios/projectkoios",
)
```

Python-specific behavior belongs in Python repository inspectors or loaders.

Git-specific behavior belongs in Git inspectors.

## RepositoryFile

A `RepositoryFile` is a loaded source artifact from a repository.

Initial model:

```python
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RepositoryFile:
    repository_root: Path
    path: Path
    relative_path: Path
    text: str
    language: str
```

Field meanings:

|Field|Meaning|
|---|---|
|`repository_root`|Absolute path to the repository root.|
|`path`|Absolute path to the file.|
|`relative_path`|Path relative to the repository root. This is what should be shown in answers.|
|`text`|File contents.|
|`language`|File language or type, such as `python`, `toml`, or `markdown`.|

The relative path is important for RAG responses.

Example answer source:

```text
src/python/projectkoios/api/app.py
```

not:

```text
/Users/eugene/repos/projectkoios/src/python/projectkoios/api/app.py
```

## Supported Files

The MVP supports Python repository files needed for coding assistance.

Initial supported suffixes:

|Suffix|Language|
|---|---|
|`.py`|`python`|
|`.toml`|`toml`|
|`.md`|`markdown`|

This covers:

- source files
    
- tests
    
- `pyproject.toml`
    
- README files
    
- architecture notes
    

Later suffixes may include:

|Suffix|Language|
|---|---|
|`.yaml` / `.yml`|`yaml`|
|`.json`|`json`|
|`.txt`|`text`|
|`.js` / `.ts`|`javascript` / `typescript`|
|`.rs`|`rust`|

## Ignored Paths

Repository loading must ignore generated, cached, virtual-environment, and version-control directories.

Initial ignored parts:

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

A file is ignored if any part of its path is in `IGNORED_PARTS`.

Examples:

```text
.venv/lib/python3.12/site-packages/...
.git/objects/...
src/python/projectkoios/__pycache__/...
.pytest_cache/...
```

These files should not be loaded into the RAG context.

## Loader Responsibility

The loader discovers supported files and returns `RepositoryFile` objects.

Initial package layout:

```text
src/python/projectkoios/repositories/
├── __init__.py
├── models.py
├── filters.py
└── loader.py
```

Initial loader:

```python
from pathlib import Path

from projectkoios.repositories.filters import IGNORED_PARTS, SUPPORTED_SUFFIXES
from projectkoios.repositories.models import RepositoryFile


class PythonRepositoryLoader:
    def load(self, root: Path) -> list[RepositoryFile]:
        root = root.resolve()
        files: list[RepositoryFile] = []

        for path in root.rglob("*"):
            if not path.is_file():
                continue

            if any(part in IGNORED_PARTS for part in path.parts):
                continue

            language = SUPPORTED_SUFFIXES.get(path.suffix)

            if language is None:
                continue

            files.append(
                RepositoryFile(
                    repository_root=root,
                    path=path,
                    relative_path=path.relative_to(root),
                    text=path.read_text(encoding="utf-8"),
                    language=language,
                )
            )

        return files
```

## What the Repository Layer Does Not Do

The repository layer does not:

- chunk files
    
- search files
    
- rank results
    
- call an LLM
    
- parse Python ASTs
    
- build embeddings
    
- infer citations
    
- manage workflows
    
- read Obsidian vault semantics
    

Those belong to later layers.

|Responsibility|Package|
|---|---|
|Load repository files|`projectkoios.repositories`|
|Split text/code into chunks|`projectkoios.chunking`|
|Search chunks|`projectkoios.search`|
|Build RAG prompts|`projectkoios.rag`|
|Call local or remote LLMs|`projectkoios.llm`|
|Expose HTTP endpoints|`projectkoios.api`|

## No Deep Repository Inheritance

Avoid this:

```python
class Repository:
    pass


class GithubRepository(Repository):
    pass


class PythonGithubRepository(GithubRepository):
    pass
```

This encodes independent traits as subclasses.

Prefer this:

```python
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Repository:
    root: Path
    name: str
    remote_url: str | None = None
```

Then add behavior through services:

```text
RepositoryLoader
PythonRepositoryInspector
GitRepositoryInspector
RepositoryFileLoader
```

This keeps the model extensible without creating class explosion.

## Future Inspectors

Later repository metadata can be added through inspectors.

Examples:

|Inspector|Purpose|
|---|---|
|`GitRepositoryInspector`|Detect remote URL, branch, commit hash, dirty state.|
|`PythonRepositoryInspector`|Detect `pyproject.toml`, package roots, test paths, import namespaces.|
|`MonorepoInspector`|Detect multiple packages or language roots.|
|`DependencyInspector`|Extract dependencies from `pyproject.toml`.|

These inspectors should return explicit data objects rather than mutating a large repository object.

## Testing Targets

Tests should start with the loader.

Test path:

```text
tests/repositories/loader/test__PythonRepositoryLoader.py
```

Initial tests:

|Test|Behavior|
|---|---|
|`test__load__discovers_python_files`|Loads `.py` files.|
|`test__load__discovers_pyproject_toml`|Loads `pyproject.toml`.|
|`test__load__discovers_markdown_files`|Loads `.md` files.|
|`test__load__ignores_venv`|Ignores `.venv`.|
|`test__load__ignores_git_directory`|Ignores `.git`.|
|`test__load__returns_relative_paths`|Computes paths relative to the repository root.|
|`test__load__skips_unsupported_suffixes`|Skips unsupported file types.|

Use temporary directories for loader tests. Do not depend on the real Project Koios repository for unit tests.

## MVP Rule

The repository layer is complete enough for the MVP when it can load a local Python repository into `RepositoryFile` objects with correct relative paths and ignored directories.

The first useful repository target is Project Koios itself.

Example MVP question enabled by this layer:

```text
Which file defines the FastAPI app?
```

This question cannot be answered reliably until repository files can be loaded, chunked, searched, and passed to the LLM with source paths.