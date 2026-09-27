# Project Koios pilot catalog

Pilots are bounded demonstrations of product use cases. They connect a use-case
outcome to component contracts, synthetic fixtures, private run evidence, and
review criteria.

A pilot definition is not execution authority. It does not accept a contract,
approve a private source, authorize an external effect, establish scientific
validity, or permit publication.

## Pilot definitions

| Pilot ID | Use case | Definition status | Execution status |
|---|---|---|---|
| `PILOT-UC-01-01` | [Textbook ingestion and RAG](pilot-uc-01.textbook-ingestion-and-rag.md) | Draft | Not authorized |
| `PILOT-UC-02-01` | [Manuscript development](pilot-uc-02.manuscript-development.md) | Draft | Not authorized |
| `PILOT-UC-03-01` | [`ksdft2effmass` prospective research](pilot-uc-03.ksdft2effmass-prospective-research.md) | Draft | Not authorized |

Definition and execution statuses are coordination labels for these pilot
records. They do not replace contract lifecycle, workflow state, review
disposition, or scientific acceptance.

## Routing model

| Material | Authoritative location |
|---|---|
| Cross-repository pilot definition | `projectkoios/docs/pilots/` |
| Product outcome | `projectkoios/docs/use-cases/` |
| Architecture decision | `projectkoios/docs/adr.*.md` |
| Exact component contract | Owning repository under `docs/contracts/` |
| Synthetic fixtures and conformance tests | Owning component repository |
| Mutable coordination | Owner issue and parent roadmap |
| Private source, benchmark, payload, or review data | Configuration-resolved private store |
| Private run evidence | `state/runs/<run-id>/` under the private store |
| Project-specific research protocol and public result | Application repository, when separately authorized |
| Research-program identity and relationship | `projectkoios-research` |

## Pilot-definition requirements

Every pilot definition should state:

- the use case demonstrated;
- bounded scope and exclusions;
- component and deployment owners;
- required contract identities and actual lifecycle states;
- private and public input classes;
- artifact routing;
- deterministic procedure;
- benchmark and metric freeze point;
- acceptance evidence;
- privacy and authority constraints;
- stop conditions; and
- what completion does and does not establish.

## Evidence policy

Public repositories contain pilot definitions, synthetic fixtures, schemas,
and conformance tests. Real documents may supplement validation only through
private run evidence.

Public pilot records must not contain:

- private paths or source locators;
- protected source excerpts;
- unpublished manuscript text;
- private benchmark queries or expected answers;
- credentials or deployment details;
- private workflow payloads; or
- unpublished result payloads.

A public record may refer to an immutable private artifact identity when that
identity does not reveal protected information.

## Independence

The pilots are independent demonstrations. They may reuse component contracts,
fixtures, and deployment capabilities, but completing one pilot is not a
prerequisite for another unless a later accepted contract or pilot revision
states an explicit dependency.
