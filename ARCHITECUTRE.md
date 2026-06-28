# Architecture

Project Koios is a local-first system for scientific knowledge work, course materials, references, computational modeling, and LLM-assisted workflows.

The system is not one monolithic application. It is a set of cooperating components organized around notes, sources, code, workflows, and generated artifacts.

## Repository roles

`projectkoios` is the mothership repository.

It contains:

- architecture notes
- roadmap
- ADRs
- examples
- configuration templates
- experimental incubation code

The first extracted implementation repository is `projectkoios-agent`.

`projectkoios-agent` contains:

- LLM harness code
- model backends
- tool registry
- workflow runner
- provenance tracking
- artifact rendering
- tests for agent workflows

`projectkoios-core` is deferred.

Core should only be created after shared abstractions are reused by multiple Project Koios components.

## Current structure

- `projectkoios`
  - mothership and incubation repository
- `projectkoios-agent`
  - first extracted implementation component
- `projectkoios-core`
  - deferred shared kernel
- `physkit`
  - pedagogical physics code
- `msekit`
  - research materials-science code

## System layers

Project Koios has the following conceptual layers.

### Knowledge layer

The knowledge layer contains human-readable scientific material.

Examples:

- Obsidian notes
- lecture notes
- course materials
- references
- PDFs
- bibliographic records
- generated summaries

### Schema layer

The schema layer defines the structure of Project Koios artifacts.

Examples:

- artifact records
- note records
- source records
- provenance records
- workflow records
- citation records

### Tooling layer

The tooling layer transforms and validates local material.

Examples:

- parse Markdown
- inspect Obsidian links
- ingest PDFs
- read BibTeX
- validate note conventions
- build indexes
- export artifacts

### Agent layer

The agent layer uses LLMs through a controlled harness.

The model does not directly own the system. The harness owns:

- state
- tools
- permissions
- workflow steps
- provenance
- validation
- final artifact rendering

The agent layer includes:

- model backends
- prompt construction
- tool registry
- controller
- workflow runner
- provenance ledger
- renderers

### Code layer

The code layer contains scientific and pedagogical software.

Current major code projects:

- `physkit`
- `msekit`

`physkit` is pedagogical code.

`msekit` is research code.

### Interface layer

The interface layer exposes Project Koios workflows to the user.

Possible interfaces:

- command line
- Obsidian
- notebooks
- Quarto
- local web UI

The first interface should be command-line based.

## Agent harness model

The LLM is not the application.

The harness is the application.

The LLM proposes actions. The harness decides whether those actions are allowed.

The basic loop is:

1. receive task
2. build task state
3. call model
4. parse model output
5. validate proposed action
6. run tool if allowed
7. record observation
8. update state
9. render final artifact

The controller is responsible for permissions and execution.

The provenance ledger is responsible for recording where claims and generated artifacts came from.

## First extracted component

The first extracted component is `projectkoios-agent`.

Its initial package path is:

- `src/projectkoios/agent`

Its initial MVP is:

- read one Markdown note
- ask a model for a structured review
- validate the structured result
- render an Obsidian-ready Markdown review
- write the output
- record provenance

## Deferred core

`projectkoios-core` should not be created yet.

The current code under `/src/python/projectkoios` may eventually become core, but the boundaries are not stable enough.

A concept should move into core only after it is reused by multiple components.

Examples of possible future core objects:

- `ArtifactRef`
- `ProvenanceRecord`
- `WorkflowSpec`
- `ToolSpec`
- `ModelBackend`
- `AgentState`

Until then, these objects may live locally inside `projectkoios-agent`.

## Design commitments

Project Koios should remain:

- local-first
- provenance-aware
- model-agnostic
- Obsidian-compatible
- reproducible
- useful for scientific teaching and research

The first goal is not to build a general chatbot.

The first goal is to build controlled workflows that transform local scientific artifacts into useful, traceable outputs.
