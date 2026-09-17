# Project Koios Scientific Platform Thesis

## Agent-Orchestrated, Physics-Governed Multiscale Modeling

- **Document type:** System architecture thesis
- **Status:** Proposed
- **Scope:** Project Koios as a whole
- **Date:** 2026-09-15
- **Author:** Eugene Ragasa

## Document authority

This document describes a proposed shape for Project Koios as a scientific
platform. It is not an architecture decision record, implementation plan, API
contract, or authorization to build a particular service.

The thesis establishes vocabulary, desired system properties, and boundaries
that can guide experiments and later specifications. Individual repositories
retain authority over their own scientific and software decisions. Concrete
implementation choices require evidence, focused specifications, and acceptance
criteria in the repository that owns the affected domain.

## Context

Multiscale materials modeling may connect quantum calculations, reduced
electronic models, molecular and mesoscale simulations, and continuum-scale
engineering models. Examples include Kohn--Sham density-functional theory,
`ksdft2effmass`, morphology and charge-transport modeling, phase-field models,
and continuum finite-element analysis.

Every scale transition discards information, introduces assumptions, and may
create an ill-posed forward or inverse problem. Conventional end-to-end scripts
can conceal these transitions in procedural glue. Unconstrained learned models
can produce numerically plausible but physically inadmissible states. Neither
approach, by itself, provides sufficient scientific traceability.

Project Koios should explore whether agentic orchestration can accelerate this
work without allowing probabilistic agents to become authorities for numerical
or scientific truth.

## Thesis

Project Koios should separate agentic coordination from scientific execution.

AI and language-model agents belong primarily in a **control plane**. They may
interpret unstructured requests, discover evidence, propose mappings, construct
work items, choose among predeclared operations, and explain outcomes.

Scientific calculations belong in an **execution plane** composed of explicit,
versioned, schema-constrained executors. These executors should be deterministic
where practical and otherwise reproducible within declared seeds, tolerances,
environments, and numerical limitations.

Accepted scientific state belongs in an **evidence plane**. Only artifacts that
pass declared structural, numerical, physical, and human review gates may be
promoted into that state. An agent proposal is never evidence merely because it
is well formed or persuasive.

```text
unstructured intent and evidence
              |
              v
     agentic control plane
     proposals and work items
              |
              v
 scientific execution plane
 versioned, verifiable executors
              |
              v
       validation gates
              |
              v
  federated scientific evidence
```

## Desired system properties

### Physics preservation

Thermodynamic restrictions, conservation laws, symmetry requirements, quantum
constraints, dimensional consistency, and domain-specific admissibility rules
should be represented as executable checks wherever possible.

Passing those checks demonstrates compliance with declared constraints. It does
not prove that a model is complete, appropriate, calibrated, or representative
of reality. Validity domains and residual uncertainty must remain explicit.

### Scale decoupling

Tools operating at different physical scales should remain modular and
independently auditable. Project membership must not create an implicit runtime
dependency or shared release cadence.

Scale transitions should occur through explicit artifacts rather than shared
mutable memory or undocumented file conventions.

### Traceability and provenance

Every derived parameter should be traceable through its transformations to the
calculations, observations, literature, assumptions, software revisions, and
human decisions that support it.

Provenance should include, as applicable:

- content-addressed input and output identities
- source citations and rights information
- software commits and released versions
- dependency or container identities
- numerical backend and relevant hardware information
- random seeds, tolerances, and convergence criteria
- units, coordinate systems, bases, and sign conventions
- uncertainty and validity domains
- transformations and declared information loss
- validation results and human approvals

### Human scientific authority

Human expertise should move away from routine transcription and dispatch toward
model selection, invariant design, validity assessment, exception review, and
scientific acceptance.

Automation may reduce operational labor. It must not obscure who accepted a
scientific claim or why.

## Scientific work items

A multiscale calculation or inverse-problem step may be represented conceptually
as a scientific work item. A work item should identify its inputs, requested
transformation, executor, constraints, acceptance criteria, and expected output
artifacts.

Operational progress and scientific disposition are different concerns. A
possible conceptual distinction is:

```text
execution status:
  proposed -> queued -> running -> succeeded | failed | cancelled

validation status:
  unreviewed -> constraint-passed -> scientifically-accepted | rejected
```

A successful process exit does not imply scientific acceptance. A convergence
failure is an execution outcome, not a scientific conclusion. These names are
illustrative vocabulary, not a mandated workflow-state implementation.

## Agent authority

Agents may:

- extract candidate parameters from unstructured sources
- propose schema mappings and transformations
- assemble work items from approved operations
- dispatch independently governed executors
- inspect structured failures and propose remediation
- summarize evidence, uncertainty, and unresolved conflicts

Agents must not, without an explicit validating authority:

- promote their own output into accepted scientific state
- bypass an invariant because it prevents convergence
- invent missing units, boundary conditions, or material parameters
- silently change a model, basis, governing equation, or validity domain
- overwrite failed attempts or their provenance
- represent constraint compliance as experimental validation

## Bounded remediation

Automated recovery from numerical or infrastructure failures is desirable, but
it should operate within a declared remediation policy. Such a policy may bound:

- parameters that may change
- permitted ranges and step sizes
- retry count and computational budget
- convergence criteria that must remain fixed
- evidence retained from each attempt
- changes that require human review

Changing numerical controls within a validated range may be automatable.
Changing the scientific model, physical assumptions, basis, boundary
conditions, or acceptance thresholds should normally create a new proposal and
require review.

## Federated scientific evidence

The platform may provide a global view of projects, configurations, and lineage,
but the authoritative evidence should remain with the repository or artifact
store that owns it. A cross-project index should be a reproducible projection,
not an irreplaceable mutable database.

This federated provenance model serves the intent sometimes associated with a
configuration-management database while preserving local ownership and avoiding
a single undocumented source of truth.

## Scale-transition contracts

A scale transition should declare more than a destination parameter value. Its
contract should describe:

- the source and destination representations
- the mathematical transformation or inference procedure
- information intentionally discarded
- assumptions introduced at the boundary
- units, bases, coordinate frames, and normalization conventions
- uncertainty propagation
- admissible parameter ranges
- validation and rejection criteria
- evidence required for replay or independent review

These declarations are especially important for top-down inverse problems,
where many lower-scale states may satisfy the same higher-scale target.

## External scientific applications

`ksdft2effmass` and `dacp2transport` are initial external research applications
that can provide evidence for this thesis. They are independent projects rather
than components absorbed into a Project Koios monolith.

- `ksdft2effmass` can exercise contracts for first-principles operators,
  reduced Hamiltonians, effective parameters, and their validation.
- `dacp2transport` can exercise contracts across molecular evidence,
  morphology ensembles, configuration-dependent electronic models, and
  transport quantities.

They are not presumed to form one direct pipeline, and abstractions should not
be extracted from either application until equivalent semantics are
demonstrated by another consumer.

Future phase-field, finite-element, or other scale-specific applications should
follow the same independent-project principle unless evidence supports a
different boundary.

## Alternatives and risks

### End-to-end learned models

End-to-end learned mappings may be useful as proposal generators or bounded
surrogates. They are insufficient as the sole source of accepted multiscale
state when admissibility, uncertainty, and lineage cannot be inspected.

### Hardcoded coupling scripts

Scripts remain useful inside bounded, tested transformations. They become risky
when they implicitly define cross-scale semantics, hide state transitions, or
serve as the only provenance record.

### Agentic orchestration

Agentic orchestration offers flexibility in planning and failure handling, but
introduces nondeterminism, prompt sensitivity, and the risk of persuasive but
unsupported reasoning. The separation among control, execution, and evidence
planes is intended to contain those risks rather than eliminate them.

## Evaluation questions

The thesis should be revised or rejected if practical work shows that:

- scale transitions cannot be represented without unacceptable schema burden
- provenance capture costs exceed its scientific and operational value
- bounded agents provide no benefit over conventional workflow systems
- validation gates cannot prevent unreviewed state promotion
- federated evidence cannot support reliable cross-project queries
- independent applications cannot share contracts without harmful coupling

Positive evidence should come from replayable workflows and reviewed scientific
artifacts, not from architectural completeness alone.

## Consequences if pursued

Potential benefits include stronger provenance, clearer scientific authority,
modular scale-specific tools, reusable validation boundaries, and safer use of
AI for research operations.

Costs include substantial schema design, adapter maintenance, infrastructure
integration, evidence storage, and human review. The initial scope should remain
narrow and should test one concrete scale transition before attempting a general
multiscale platform.

## Non-decisions

This thesis does not select:

- a workflow engine or service-ticket implementation
- a database, graph store, message bus, or scheduler
- a global mutable configuration-management database
- a container or infrastructure provider
- a universal artifact schema
- particular state names or transition mechanics
- an optimization algorithm or surrogate-model family
- automatic authority to modify external research repositories
- a direct coupling between `ksdft2effmass` and `dacp2transport`

Those choices require focused evidence and repository-owned specifications.

## Evolution

This document should evolve through scientific and implementation experience.
It may later yield narrow specifications, executable contracts, or architecture
decisions. Until then, it remains a proposed system thesis rather than binding
implementation authority.
