# MVP TODO: RAG-Supported LLM Coder

## 1. Define MVP Scope

- [ ] Target Python repositories first
- [ ] Defer Obsidian vaults
- [ ] Defer PDFs and references
- [ ] Defer vector search
- [ ] Defer workflow/provenance system
- [ ] Defer agent framework

MVP input:

```text
local Python repository path
```

MVP output:

```text
answer + relevant source paths
```

## 2. Add Repository Loader

Create:

```text
src/python/projectkoios/repositories/
├── __init__.py
├── models.py
├── loader.py
└── filters.py
```

* [ ] Define `RepositoryFile`
* [ ] Define ignored paths
* [ ] Define supported suffixes
* [ ] Implement `PythonRepositoryLoader.load(root)`
* [ ] Return absolute path, relative path, text, and language

Initial supported files:

```text
.py
.toml
.md
```

Initial ignored paths:

```text
.git
.venv
__pycache__
.pytest_cache
.mypy_cache
.ruff_cache
dist
build
```

## 3. Test Repository Loader

Create:

```text
tests/repositories/loader/test__PythonRepositoryLoader.py
```

Tests:

* [ ] `test__load__discovers_python_files`
* [ ] `test__load__discovers_pyproject_toml`
* [ ] `test__load__discovers_markdown_files`
* [ ] `test__load__ignores_venv`
* [ ] `test__load__ignores_git_directory`
* [ ] `test__load__returns_relative_paths`
* [ ] `test__load__skips_unsupported_suffixes`

## 4. Add Chunking

Create:

```text
src/python/projectkoios/chunking/
├── __init__.py
├── models.py
└── fixed.py
```

* [ ] Define `TextChunk`
* [ ] Implement fixed-size chunking
* [ ] Preserve source path
* [ ] Preserve chunk index
* [ ] Preserve character offsets
* [ ] Add overlap support

Initial parameters:

```text
chunk_size = 2000
chunk_overlap = 300
```

## 5. Test Chunking

Create:

```text
tests/chunking/fixed/test__FixedTextChunker.py
```

Tests:

* [ ] `test__chunk__returns_single_chunk_for_short_text`
* [ ] `test__chunk__splits_long_text`
* [ ] `test__chunk__preserves_relative_path`
* [ ] `test__chunk__preserves_offsets`
* [ ] `test__chunk__uses_overlap`

## 6. Add Lexical Search Over Chunks

Create/update:

```text
src/python/projectkoios/search/
├── __init__.py
├── models.py
├── service.py
└── lexical.py
```

* [ ] Define `SearchQuery`
* [ ] Define `SearchHit`
* [ ] Implement lexical substring/token scoring
* [ ] Search over chunk text
* [ ] Rank by score
* [ ] Return top `k` hits
* [ ] Include source path and snippet

First scoring rule:

```text
title/path match > exact text match > token overlap
```

## 7. Test Lexical Search

Create:

```text
tests/search/lexical/test__LexicalSearchService.py
```

Tests:

* [ ] `test__search__returns_matching_chunks`
* [ ] `test__search__returns_empty_list_when_no_match`
* [ ] `test__search__ranks_better_match_first`
* [ ] `test__search__respects_limit`
* [ ] `test__search__includes_source_path`
* [ ] `test__search__is_case_insensitive`

## 8. Add Local LLM Service

Create:

```text
src/python/projectkoios/llm/
├── __init__.py
├── models.py
└── ollama.py
```

* [ ] Define `LLMRequest`
* [ ] Define `LLMResponse`
* [ ] Implement `OllamaLLMService`
* [ ] Call local Ollama API
* [ ] Support configurable model name
* [ ] Support timeout
* [ ] Return generated answer

Default model:

```text
llama3.2
```

## 9. Test LLM Service Boundary

Create:

```text
tests/llm/ollama/test__OllamaLLMService.py
```

Tests:

* [ ] Mock `httpx.post`
* [ ] Verify request payload
* [ ] Verify response parsing
* [ ] Verify model name is passed
* [ ] Verify timeout is used
* [ ] Verify HTTP errors raise cleanly

Do not require a real local model in normal tests.

## 10. Add RAG Prompt Assembly

Create:

```text
src/python/projectkoios/rag/
├── __init__.py
├── models.py
└── prompt.py
```

* [ ] Define `RAGRequest`
* [ ] Define `RAGContext`
* [ ] Define `RAGResponse`
* [ ] Assemble prompt from query and retrieved chunks
* [ ] Include source paths in context
* [ ] Keep prompt deterministic and inspectable

Prompt structure:

```text
You are helping with a Python repository.

Question:
...

Relevant context:
[1] path/to/file.py
...
```

## 11. Test Prompt Assembly

Create:

```text
tests/rag/prompt/test__RAGPromptBuilder.py
```

Tests:

* [ ] `test__build__includes_user_question`
* [ ] `test__build__includes_context_chunks`
* [ ] `test__build__includes_source_paths`
* [ ] `test__build__orders_chunks_by_rank`
* [ ] `test__build__is_deterministic`

## 12. Add `/ask` API Endpoint

Create/update:

```text
src/python/projectkoios/api/routers/ask.py
```

* [ ] Define `AskRequest`
* [ ] Define `AskResponse`
* [ ] Accept repository root
* [ ] Accept user question
* [ ] Load repository files
* [ ] Chunk files
* [ ] Search chunks
* [ ] Build RAG prompt
* [ ] Call LLM service
* [ ] Return answer and sources

Endpoint:

```text
POST /ask
```

## 13. Test `/ask` API Boundary

Create:

```text
tests/api/routers/ask/test__create_ask_router.py
```

Tests:

* [ ] `test__ask_endpoint__accepts_question`
* [ ] `test__ask_endpoint__rejects_empty_question`
* [ ] `test__ask_endpoint__returns_answer`
* [ ] `test__ask_endpoint__returns_sources`
* [ ] Mock repository loader
* [ ] Mock search service
* [ ] Mock LLM service

## 14. Manual MVP Test

Use Project Koios itself as the first target repo.

Questions:

* [ ] “Where is the FastAPI app assembled?”
* [ ] “Which file defines the `/search` route?”
* [ ] “Where is `SearchResult` defined?”
* [ ] “How do I add a new route?”
* [ ] “Summarize the API package.”
* [ ] “What tests cover the ASGI entry point?”

Expected answer must include:

```text
answer
source file paths
relevant snippets or citations
```

## 15. Stop Condition for MVP

The MVP is done when:

* [ ] `POST /ask` works on the local Project Koios repo
* [ ] Answers include source paths
* [ ] Retrieval uses local files
* [ ] LLM call works locally
* [ ] Normal tests do not require Ollama running
* [ ] Manual test questions produce useful coding help
