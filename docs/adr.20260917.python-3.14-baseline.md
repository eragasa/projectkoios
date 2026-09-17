# ADR20260917: Python 3.14 baseline across Project Koios

## Status

Accepted

## Context

Project Koios Python packages initially declared Python 3.12 as their minimum runtime. The intended first managed research project, `ksdft2effmass`, requires Python 3.14, and the operator has selected Python 3.14 as the common Project Koios target. Retaining two runtime baselines would add avoidable compatibility work to shared workflow contracts and cross-repository validation.

## Decision

All Project Koios repositories that publish or execute Python code require Python 3.14 or later. Their package metadata declares `requires-python = ">=3.14"`, Ruff targets `py314`, and type-checker configuration identifies Python 3.14 where an explicit version is configured.

Repository instructions, setup commands, user documentation, and architecture examples use Python 3.14. Repositories without Python code, including the current `projectkoios-bootstrap` and `projectkoios-web` implementations, retain their applicable non-Python runtime requirements and do not add a synthetic Python dependency.

External research applications retain their own runtime declarations. Project Koios management does not rewrite an external application's Python policy, although a concrete integration may require an explicitly compatible runtime boundary.

## Consequences

- Existing Python 3.12 virtual environments must be recreated with Python 3.14 before package installation or validation.
- New Project Koios Python code may rely on Python 3.14 language and standard-library behavior after the owning repository's tests establish it.
- Maintained tests, lint, type checking, package builds, and installation checks run under Python 3.14.
- Python 3.12 compatibility is no longer a Project Koios requirement.
- Dependency compatibility with Python 3.14 must be verified per repository; metadata alignment alone is not software verification.
- The common Python baseline removes one compatibility mismatch from the proposed `ksdft2effmass` workflow shadow-conformance pilot but does not establish API, wire-format, or behavioral compatibility.

## Alternatives considered

### Retain Python 3.12 compatibility

Rejected. It would require the reusable workflow implementation to preserve a runtime target that the intended first managed research consumer does not use.

### Support both Python 3.12 and Python 3.14

Rejected for now. The additional test matrix and compatibility constraints are not justified by a demonstrated Project Koios consumer requiring Python 3.12.

### Target Python 3.14 only in `projectkoios-workflow`

Rejected. A shared baseline is simpler for namespace packages, local development, and cross-repository integration.
