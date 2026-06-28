# Roadmap

Project Koios is being built through small working prototypes.

The goal is not to design the final system upfront. The goal is to build useful pieces, see what patterns repeat, and only then decide what deserves to become shared infrastructure.

At this stage, `projectkoios` is the mothership repo. It holds the roadmap, architecture notes, ADRs, examples, configuration ideas, and experimental code. The first separate implementation repo will be `projectkoios-agent`.

`projectkoios-core` is intentionally deferred. Some of the current code may eventually become core, but the boundaries are not stable yet.

## Current direction

The immediate direction is to build several small MVPs instead of one large framework.

Each MVP should do one useful thing. It should have a clear input, a clear output, and enough tests to avoid breaking the basic workflow.

It is acceptable if early MVPs duplicate small objects or use rough local schemas. Shared abstractions should only be extracted after the same pattern shows up in multiple places.

## MVP: Agent note review

This is the first likely `projectkoios-agent` workflow.

The goal is to read one Markdown note and produce a useful review note.

The first version should:

* read a local Markdown file
* send the content to a model backend
* ask for structured review output
* render the result as Obsidian-ready Markdown
* write the output to disk
* record basic provenance

This MVP proves that the harness can control a model, use local files, and produce a real artifact.

## MVP: Vault utilities

This track is for small non-LLM tools that help maintain the Obsidian vault.

Useful first tools include:

* list notes
* find broken links
* inspect backlinks
* check note names
* check definition formatting
* check whether a note has a `back to: [[...]]` line

This does not need to be part of the agent at first. Simple tools are enough.

## MVP: Reference ingestion

This track is for turning references into structured local records.

Useful first tools include:

* read BibTeX
* normalize citation keys
* map PDFs to reference IDs
* generate reference stub notes
* extract title, authors, year, and journal

This can remain rough until the reference workflow becomes clearer.

## MVP: Paper to note

This workflow turns a paper into an Obsidian-ready article note.

The first version should produce:

* bibliographic information
* useful claims
* useful quotations
* possible teaching use
* possible research use
* provenance notes

This should probably come after the simpler note-review workflow, because PDF handling adds extra complexity.

## MVP: Code review

This workflow uses the harness to inspect local code from `physkit`, `msekit`, or Project Koios itself.

The first version should review one Python file or small module.

The review should focus on:

* public API
* tests
* naming
* numerical assumptions
* physics or modeling assumptions
* possible refactors

This connects Project Koios to actual scientific software work.

## MVP: Lecture workflow

This workflow supports course-material development.

The first version should take a rough lecture note and produce one or more useful teaching artifacts, such as:

* a cleaned lecture note
* a short problem set
* a notebook checklist
* a list of missing definitions
* a list of possible implementation tasks

This track should stay close to actual teaching needs rather than becoming a general content generator.

## Working rule

Do not block one MVP because another MVP is unfinished.

The project can move forward through small, partially independent tools. If a tool becomes useful, keep it. If it does not, delete it or leave it as an experiment.

The main thing to avoid is pretending that early abstractions are final.

## Extraction rule

A concept stays local if only one MVP uses it.
[118;1:3u
A concept can be considered for extraction if two MVPs use it.

A concept can move toward `projectkoios-core` if three or more MVPs use it and the interface feels stable.

Possible future core concepts include:

* `ArtifactRef`
* `SourceSpan`
* `ProvenanceRecord`
* `WorkflowSpec`
* `ToolSpec`
* `ModelBackend`
* `ProjectConfig`

For now, these can live locally where they are needed.

## Near-term priorities

The near-term priorities are:

1. Keep the mothership repo readable.
2. Create `projectkoios-agent`.
3. Build the `review-note` MVP.
4. Add a fake model backend for tests.
5. Add one real model backend.
6. Run the workflow on one real Project Koios note.
7. Start the next MVP based on what is most useful at the time.

The first success condition is simple: a local command reads one scientific note and writes one useful, traceable review artifact.

The larger success condition is that several small MVPs reveal what Project Koios actually needs as shared infrastructure.

