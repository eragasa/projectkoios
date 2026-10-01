# Current Architecture Documentation

## Purpose

Architecture pages describe the code and system that exist in the containing Git
tree. They are not plans, task state, or a decision ledger. Git history carries
rationale; the current indexes under this directory carry architecture authority.

## Ownership

The repository that owns an implementation owns its package, module, class, and
implementation documentation. `projectkoios` owns cross-repository and system
architecture. Documentation must not claim behavior owned by another repository.

The index-only topology and validator below apply only to architecture
documentation in this product-architecture repository. `projectkoios` is the
exception because it owns product and cross-repository architecture rather than
component implementation architecture. Component repositories maintain and
enforce the common source-mirroring trio/`ClassName` convention in their own
repositories and do not invent repository-specific topologies. This repository's
validator does not validate component trees.

## Topology

All architecture Markdown pages are directory indexes. The sole exception is
this root `README.md`. Named leaves such as `implementation.md`,
`mathematics.md`, `references.md`, and `testing.md` are invalid.

Python documentation mirrors its present ownership hierarchy:

```text
docs/architecture/<package>/index.md
docs/architecture/<package>/<module>/index.md
docs/architecture/<package>/<module>/<ClassName>/index.md
docs/architecture/<package>/<module>/<ClassName>/implementation/index.md
docs/architecture/<package>/<module>/<ClassName>/implementation/mathematics/index.md
docs/architecture/<package>/<module>/<ClassName>/implementation/references/index.md
docs/architecture/<package>/<module>/<ClassName>/implementation/testing/index.md
```

Package indexes summarize the package and link immediate documented subpackages
or modules. Module indexes summarize the module and link immediate documented
classes. Class indexes state the current contract and link implementation detail
when present. The implementation index links its present mathematics,
references, and testing indexes. Detail indexes link back to their implementation
and class indexes.

Reserved system topics use `docs/architecture/_system/<topic>/index.md` and are
owned only by this system repository. Canonical examples live under
`docs/architecture/examples/`; `_templates/` is obsolete and prohibited.

## Content

Keep pages current, concise, and evidence-linked. Use repository-relative code
and test paths. Mathematics should use readable LaTeX with named equations,
symbols, units, assumptions, and validity domains. Research-derived claims need
a source version, pinpoint locator, license, role, derivation basis, and declared
deviation.

Keep evidence kinds separate:

- implementation conformance shows that code matches the documented contract;
- numerical verification states comparator, tolerance, environment, and domain;
- scientific validation states the reference artifact and scientific claim; and
- human acceptance names the responsible authority or says it is not evaluated.

Passing code tests does not imply scientific validation or human acceptance.
The worked hierarchy is illustrative: its mapped example source and test files
are not claimed to exist in `projectkoios`. Copy a relevant example only as a
starting point, then replace every illustrative path, symbol, claim, source, and
evidence statement.

## Current indexes

- [`Citation-document control`](_system/citation-document-control/index.md)
- [`LineChunker` vertical slice](projectkoios/index.md)

## Change Rule

An architecture-relevant change is a vertical slice: update implementation,
its owning architecture indexes, and mapped tests in the same change. Pure
formatting, comments, and behavior-preserving moves require only repairs to
mappings made false by the move. Untouched legacy code does not require bulk
migration.

## Validation

Run from the repository root:

```bash
python tools/validate_architecture_docs.py
```

The validator checks only bounded filesystem topology in this repository. It
does not parse Markdown meaning, Python symbols, citations, scientific truth,
Git state, or any component repository.
