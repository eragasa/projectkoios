# Project Koios: An audit-first, LLM-assisted workflow for verifiable computational physics

- **Document type:** Technical methodology and documented experience report
- **Status:** Draft living source
- **Review status:** Not peer reviewed
- **Release status:** Not released; no DOI assigned or reserved
- **Scientific status:** Not a scientific-validation report
- **Productivity status:** No productivity-gain claim
- **Case-study evidence cutoff:** 2026-10-21; mutable release guidance
  rechecked through 2026-10-22
- **Author:** Eugene Joseph M. Ragasa
- **Machine-readable evidence:** [Bounded JSON evidence
  ledger](project-koios-audit-first-methodology-evidence.json)

## Abstract

Project Koios is an evolving collection of independently governed software,
formalization, numerical-method, computational-physics, and coordination
repositories. This report describes an audit-first workflow in which a large
language model (LLM) may assist with discovery, drafting, implementation, and
review, while inspectable artifacts and accountable people retain authority.
The central method is to classify every claim by evidence kind, bind accepted
claims to immutable revisions and precise artifact locations, preserve failures
and corrections, and prevent success in one evidence channel from being
silently promoted into another.

Five bounded cases illustrate the workflow: Lean formalization, reusable
optimization and numerics, PhysKit computational-physics components,
`ksdft2effmass` retained numerical experiments, and the Project Koios Pi
coordination harness. The cases are evidence of engineering methods and project
experience. They do not constitute peer-reviewed validation of Project Koios,
validation of a material model, proof that an LLM obeys instructions, or proof
of productivity improvement.

## 1. Scope and non-claims

This report asks a methodological question: how can LLM assistance be used in
computational-physics work without making model output the authority for
mathematics, numerical results, scientific interpretation, publication, or
project decisions?

The report may document:

- repository-visible methods and boundaries;
- theorem, certificate, test, and retained-result evidence at immutable Git
  revisions;
- failures, reviews, corrections, deprecations, and preservation practices;
- limitations and evidence still required; and
- a prospective release design.

It does **not** claim:

- peer review or independent validation of this report;
- experimental or material validation;
- that a passing software test proves correct science;
- that a Lean theorem proves source fidelity or physical applicability;
- that a model-generated proposal is evidence because it is persuasive;
- that an LLM reliably follows a prompt or policy;
- improved productivity, quality, cost, or time-to-result; or
- authorization to execute calculations, publish artifacts, create releases,
  submit to arXiv, or reserve or register a DOI.

No controlled productivity study, baseline task set, blinded comparison, or
complete time-and-cost record has been admitted. Productivity effects therefore
remain unmeasured.

## 2. The audit-first principle

The workflow starts from an authority boundary rather than from a model
capability. The mothership's proposed platform thesis places language-model
agents in a control plane, calculations in a versioned execution plane, and
accepted artifacts behind evidence and human-review gates.[M1] The current
architecture documentation separately classifies implementation conformance,
numerical verification, scientific validation, and human acceptance.[M2]

An audit-first task applies the following sequence:

1. **Freeze the claim.** State the narrow conclusion, assumptions, validity
   domain, and evidence class before treating an artifact as support.
2. **Resolve ownership.** Identify the repository and human authority that own
   the implementation, scientific meaning, and publication decision.
3. **Bind immutable inputs.** Record commit, file or declaration, dependency
   versions, and content identities where applicable.
4. **Generate or inspect.** Allow an LLM to propose prose, code, proofs, tests,
   mappings, or review leads, but do not grant it acceptance authority.
5. **Check through the proper channel.** Use a kernel for a formal theorem, an
   exact checker for a certificate, an independent comparator for numerical
   verification, a declared reference artifact and protocol for scientific
   validation, and an identified person for governed decisions.
6. **Retain negative evidence.** Preserve failed checks, rejected prototypes,
   unresolved ambiguities, corrections, and deprecations instead of rewriting
   the history as uninterrupted success.
7. **Report the boundary.** State both what the evidence establishes and what it
   does not establish.

This is stricter than merely attaching provenance after a result is produced.
Evidence class and acceptance conditions constrain what may be claimed from the
start.

## 3. Evidence and authority taxonomy

| Evidence or decision kind | Adequate basis | Bounded conclusion | Not implied |
|---|---|---|---|
| Implementation conformance | Mapped source, contract, and tests at an identified revision | The tested implementation meets the declared software behavior in the exercised domain | Numerical correctness outside tests, scientific adequacy, or release approval |
| Lean theorem evidence | Exact proposition and proof term checked by the pinned Lean kernel, with assumptions and axiom report | The encoded proposition follows under its encoded assumptions | Source fidelity, runtime correctness, numerical convergence, physical applicability, or publication acceptance |
| Exact checked certificate | Exact data, unambiguous encoding, checker, and a proved connection from checker success to a target proposition | The checker's proved conclusion for those exact inputs | Correctness of unbound files, floating-point calculations, or a scientific model |
| Independent numerical verification | Producer-independent reconstruction or comparator, explicit tolerance, environment, and finite domain | Agreement within the declared criterion for the declared computation | Exact equality, continuum behavior, uncertainty quantification, or material validation |
| Scientific validation | Identified reference artifact or observation, protocol, applicability domain, uncertainty treatment, and scientific review | The stated scientific claim in the reviewed scope | Universal validity or authority beyond that scope |
| Human-governed decision | Identified accountable person or accepted governance record | Acceptance, rejection, release, publication, model choice, or exception within the decision's scope | A mathematical or numerical result merely from the decision itself |
| `EXPERIENCE_OBSERVATION` | Immutable record of a bounded project occurrence, with its status and limitations | That the documented occurrence happened in the identified scope | Recurrence, general effectiveness, or promotion into another evidence class |
| `PLANNED` | Explicit future protocol, requirement, or migration state | Intended work and its declared gates | Implementation, execution, verification, validation, or completion |

Formal's evidence policy gives a compatible separation: Lean proof, exact
certificate checking, interval or rational external certificates,
floating-point results, runtime output, and publication prose are distinct
channels.[F1] Its required numerical-to-formal bridge names the proposition,
exact data model, parser, checker, soundness theorem, bound external input, and
rounding or model assumptions.[F1]

The outcome dimensions are also separate. A technical pass, review disposition,
operator authorization, lifecycle decision, and scientific or publication
decision do not grant one another automatically.[M3]

## 4. LLM assistance and scientific authority

In this workflow an LLM may:

- search a bounded repository or evidence set;
- propose claim decompositions and evidence classifications;
- draft code, Lean terms, tests, prose, and review questions;
- identify inconsistencies and missing provenance;
- summarize structured failures; and
- propose a correction for human and tool-based review.

An LLM may not, merely by producing an answer:

- declare its own theorem correct;
- turn approximate output into an exact certificate;
- choose an undisclosed tolerance or scientific model;
- promote a test result into scientific validation;
- accept a manuscript claim or citation;
- authorize execution, release, or publication; or
- erase or relabel failed attempts.

The relevant evidence is therefore the checked artifact, not the eloquence of
the generated path to it. The cited Formal proof dossier identifies its result
as AI-assisted and kernel-checked and explicitly excludes runtime,
four-state-parent, material, and continuum claims.[F2] The `ksdft2effmass`
monograph similarly discloses LLM assistance with drafting, code, analysis, and
editorial work while assigning scientific selection, interpretation, reporting, and
responsibility to the author.[K8]

## 5. Case studies

### 5.1 Project Koios Formal and Lean

**Completed and documented.** At immutable public Formal revision
`26603110e9d64cd51c9101eff68060307f258a18` on
`origin/work/paper-a-diagnostic-producer-audit`, Lean is pinned to `v4.35.0` and
Mathlib to commit `56a005855ea17e0b0958f73ec801ae140b0a1679`.[F3] This checkpoint
is not presented as main, a tag, or a release. The theorem manifest records
proved declarations and their assumptions rather than treating plans as
theorems.[F5] One bounded Paper A construction includes a Boolean exact
rational-enclosure checker, a proved bridge, and source-specific theorems for a
finite analytic counterexample.[F4] The associated dossier calls the result
AI-assisted and kernel-checked, reports the kernel axioms, and excludes runtime,
four-state-parent, material, and continuum claims.[F2]

This case demonstrates two separate completed channels:

1. **Lean theorem evidence:** encoded propositions checked by the pinned kernel;
2. **an exact analytic source-certificate chain:** a Boolean exact
   rational-enclosure checker accepts the encoded certificate, while proved
   bridges and source-specific Lean theorems bind those checked conditions to
   the encoded construction.

It does not demonstrate a runtime scientific certificate. The repository's
certificate inventory explicitly reports that no runtime data/parser binding
exists and that its generic checkers do not automatically bind external
floating-point artifacts.[F4]

**Planned, not demonstrated.** A future runtime certificate would require an
exact target proposition and certificate data model; an unambiguous parser; a
checker implemented in or soundly connected to Lean; a theorem connecting
checker acceptance to the target; immutable retained input bound by digest and
provenance; explicit rounding, interval, discretization, and model assumptions;
independently discharged field-derived obligations; and a reviewed source
crosswalk.[F1][F4] No such bridge is claimed here. Formal proof also remains
distinct from scientific validation and independent expert review.

### 5.2 Project Koios Optimization and Numerics

**Completed and documented.** At immutable public provisional revision
`b722edab216ef416b8b4affa902b04a26e3da98b`, the repository exposes bounded
finite-periodic transforms, evaluation, diagnostics, and optimization
capabilities while keeping scientific coordinates, units, and acceptance with
consumers.[O1] The provisional checkpoint records development package version
`0.1.0.dev0`; this report does not present it as a tag, release, or adopted
downstream baseline.[O7] The finite-series numerical test source defines bounded
comparisons against a separately expressed 100-digit `mpmath` reference with an
explicit floating-point acceptance bound.[O2] The transform integration test
source defines one-, two-, and three-dimensional reconstruction and
Parseval/Hermiticity diagnostic checks with explicit bounds.[O3]

This evidence is software and bounded numerical verification. It is not an exact
certificate and not scientific validation. The diagnostic layer deliberately
reports values without selecting scientific tolerances.[O4]

The repository history also contains a correction specifically titled “Use
independent Hermiticity defect evidence” at immutable public commit
`00c60201d16f2ee61e5fffd83a1a1f24cd327672`.[O6] The cited test at the
provisional checkpoint retains an independently declared defect case.[O3] This
is useful correction evidence, not proof that all diagnostics are independent
or error-free.

**Planned, not demonstrated.** Consumer-level scientific interpretation and
campaign thresholds remain consumer-owned.[O1][O4] This report does not
demonstrate an exact runtime certificate or formal binding for the cited
checkpoint, and it admits no retained command output or CI artifact as evidence.
Such evidence should be added only when immutable, public, and tied to the
reported revision.

### 5.3 PhysKit

**Completed and documented.** At immutable public main revision
`11e58938ac8d0022f9e6df3aba7ca8757b4a9f88`, PhysKit records implementation
and numerical evidence without claiming material validation. The cited
checkpoint records development package version `0.1.3.dev0`; this report does
not present it as a release.[P6] The Morse-potential test source defines a
separately expressed centered finite-difference comparison of the radial force
with the negative energy derivative, using step `1.0e-5`, `rtol=5.0e-10`, and
`atol=0.0`.[P1] A periodic-cosine provenance record classifies its mapped
analytical and numerical checks as implementation and numerical verification,
not experimental validation of a material potential.[P2]

PhysKit also records a failed oblique-periodic notebook prototype: clean
execution stopped with a syntax error, saved displays were not reproducible from
the source, invalid behavior was not migrated, and the artifact was removed only
after a maintained replacement existed while its bytes remained recoverable by
commit and blob.[P3] This is concrete evidence of review, rejection, correction,
and a recoverable preservation path.

Cross-repository extraction records identify exact donor commits, blobs, and
hashes while retaining campaign tolerances, semiconductor interpretation,
scientific validation, and human acceptance with their owners.[P4]

**Planned, not demonstrated.** These scoped artifacts do not demonstrate
material validation, pedagogical effectiveness, or uncertainty
quantification.[P2][P4] This report requires separate claim-specific protocols,
evidence, and human dispositions before asserting any such future PhysKit claim.

### 5.4 `ksdft2effmass`

**Completed and documented.** At immutable public revision
`5aaff25b784c7d1bc079a3030a73be387dc11a0f` on
`origin/work/monograph-current-library-capabilities`, the retained
particle-in-a-box experiment is explicitly labeled a calculated illustrative
numerical experiment rather than a software harness, public API, semiconductor
calculation, or scientific-validation result.[K1] This checkpoint is not
presented as main or an adopted release. It retains inputs, outputs,
verification scripts, figures, environment information, and a
SHA-256 manifest.[K2] Independent verifiers compare finite results with stated
analytical oracles and identities; the acceptance boundary is agreement with
the declared finite mathematics under binary64 arithmetic, not material or
continuum validation.[K3] This evidence does not validate a material model,
silicon, DFT, Wannier localization, or impurity physics.

The retained results also expose limitations rather than only favorable numbers:
fixed low modes show the expected second-order trend, while high-index modes do
not exhibit uniform accuracy as the mode index scales with grid dimension.[K1]

Correction and reversibility appear in a separate deprecation record. Historical
Stage C command-line entry points and exact retained bytes remain frozen, newer
adapters are named, and the migration explicitly grants no scientific,
numerical-policy, or execution authority.[K4]

**Planned, not demonstrated.** The publication-independent composite-band
successor is marked `MIGRATION_IN_PROGRESS`, has no immutable experiment version
and no retained maintained run.[K5] Its protocol requires an independent
verifier and exact dependency/evidence gates, but records no new result.[K6]
This report therefore treats it as planned work, not a completed case study.

### 5.5 Project Koios Pi and LLM coordination harness

**Completed and documented.** At immutable public Bootstrap revision
`7fa09bc3b631984d3b049b00d858935575d5687d`, the accepted harness-incubation
boundary permits bounded source, sanitized fixtures, tests, and explicit
limitations while excluding transcripts, generated handoffs, credentials, and
runtime state.[H1] The startup and named-session mechanisms remain
**Candidate**, not validated generic tooling.[H2][H3]

The candidate documentation specifies deterministic preflight, explicit
repository/task naming, fail-closed scoped messaging checks, bounded failure
behavior, and no durable orchestration database, and records mocked/fake-boundary
test coverage.[H2][H3] It expressly states that the guard is not an authorization
service and that mocked tests do not prove Pi/Herdr availability or model
compliance.

A concrete coordination failure is retained: a pane was closed rather than the
client detached, terminating the Pi process. The resulting read-only diagnostic
fails closed but cannot recover the process; reassignment remains an
authorized human action.[H4] This is failure and correction evidence, not a
claim of autonomous rollback.

**Planned, not demonstrated.** Independent recurrence, generic-tool validation,
proof that an LLM follows the coordination prompt, and end-to-end availability
remain unestablished.

## 6. What failures and corrections contribute

The cases suggest that auditability depends on negative as well as positive
records:

- a counterexample can be a primary mathematical result rather than a failed
  success case;
- an independent diagnostic may replace a correlated assertion;
- an invalid prototype may be rejected while exact bytes remain recoverable;
- a historical interface may be frozen and deprecated without rewriting the
  evidence it produced; and
- an operational failure may justify a bounded diagnostic without justifying a
  daemon or automated recovery system.

These examples do not establish a complete rollback system. No cross-project
rollback-rate, recovery-time, or correction-effectiveness dataset has been
admitted. The narrower claim is that identified repositories preserve selected
failure and correction evidence instead of presenting only terminal success.

## 7. Limitations and threats to validity

### Selection and survivorship

The cases were selected from the Project Koios repository family and were not
sampled randomly. Repository-visible corrections may underrepresent informal,
private, abandoned, or undocumented failures. The report must not infer a
failure rate or general effectiveness from these examples.

### Independence

Many artifacts were authored, reviewed, or selected by the same project owner.
A producer-independent numerical verifier is stronger than rerunning the same
producer, but shared libraries, assumptions, or authorship can still correlate
errors. Formal kernel checking is not independent scientific peer review.

### Evidence freshness

Git commits are immutable but claims about “current” project state can become
stale. Every milestone must freeze an evidence ledger and must not silently
update an old report's conclusions from later repository state.

### Tool and model reproducibility

LLM outputs can depend on model version, provider behavior, prompts, context,
tool availability, and nondeterministic sampling. This report does not expose
private transcripts or claim byte-reproducible model reasoning. Reproducibility
rests on retained public artifacts and checks, not on reconstructing hidden
chain-of-thought or session state.

### Scientific reach

Most evidence here concerns software conformance, exact finite mathematics, or
bounded numerical verification. It does not validate semiconductor materials,
DFT approximations, experimental observables, or multiscale predictive use.

### Productivity

No experimental design supports a productivity conclusion. Commit volume,
passing tests, model token counts, or anecdotal speed are inadequate substitutes
for a predeclared comparison with quality and rework controls.

## 8. Rights, provenance, privacy, and authorship

The cited repository notices identify Apache-2.0 project or donor material
alongside repository-specific third-party and adaptation obligations.
Optimization retains a `NOTICE` for adapted BSD-2-Clause PyPosPack material and
names the associated source lineage.[O5] PhysKit records maintained adaptations
of Apache-2.0 `ksdft2effmass` source and routes exact mappings through its
provenance records.[P5] `ksdft2effmass` separately inventories dependencies and
vendored publication support under LGPL, BSD, PSF-related, font, and LPPL terms
that differ from the project's Apache-2.0 license.[K7] These statements do not
establish that every possible deposit input may be redistributed.

Before any public milestone, the author must review:

- authorship and contributor attribution;
- license compatibility for included source, prose, tables, and figures;
- required `NOTICE` and third-party license text;
- permission for manuscript, source, data, or image excerpts;
- trademarks and project names;
- whether an artifact is public, private, unpublished, or restricted; and
- the license selected for the deposited report itself.

This draft links to public source instead of copying protected source material.
It excludes private filesystem paths, credentials, session transcripts, hidden
runtime state, private benchmark payloads, and unpublished scientific results.
A hash identifies bytes; it does not establish permission to redistribute them.

LLM assistance does not receive authorship or scientific authority merely from
text generation. Human authors remain responsible for claims, citations,
rights, and submission decisions. Any provider-specific disclosure required by
a venue remains a later submission requirement.

## 9. Release and versioning design

### Living mothership source

The canonical evolving source remains in the `projectkoios` mothership. Git
history records changes, while each report revision keeps evidence links pinned
to immutable commits. The living source may correct and extend the report, but
must not silently revise a prior deposited milestone. Ordinary corrections use
a new Zenodo version; exceptional rights, privacy, or similar remediation must
follow the service policy and be recorded explicitly.

### Versioned Zenodo milestones

A separately authorized milestone may deposit a frozen bundle containing:

- rendered report and preferred source;
- evidence ledger with exact repository revisions and locators;
- claim-status and limitations tables;
- rights, license, authorship, and third-party notice material;
- build instructions and tool versions; and
- a SHA-256 manifest for deposited files.

Zenodo describes a new version as a new record with separate files, metadata,
and persistent identifier linked to prior and future versions.[Z1] Its current
file-management guidance nevertheless permits minor corrections to published
files within 30 days and duly justified changes later without changing the
DOI.[Z4] A version DOI alone therefore does not prove byte immutability. The
release design uses:

- the **version DOI**, together with a SHA-256 manifest retained at a separately
  cited immutable Git revision, for an exact report milestone; and
- the **all-versions/concept DOI** for the evolving report family.[Z2]

The concept DOI must not be presented as freezing the files of a particular
milestone. Claims requiring byte-level reproducibility should cite both the
version DOI and the separately retained manifest. Zenodo normally registers a
DOI when a record is published and also offers optional advance reservation.[Z3]
The Zenodo operational pages are mutable guidance cited by access date, not
immutable evidence-ledger artifacts, and must be rechecked at any
release-authorization boundary. No reservation, deposit, registration, or
publication is authorized or performed by this draft.

### Optional later arXiv submission

A later arXiv submission is optional, not assumed. It would require a
submission-ready scholarly article, author and rights review, category fit,
source/PDF preparation, and explicit authorization. arXiv submission is
moderated and requires authors to grant arXiv an irrevocable license to
distribute the work.[A1] An arXiv identifier would complement, not replace,
exact repository and Zenodo-version evidence locators. The arXiv operational
page is likewise mutable guidance and must be rechecked at any
submission-authorization boundary.

## 10. Conclusion

The documented experience supports a narrow methodological conclusion:
Project Koios has repository-visible examples of separating model assistance
from formal checking, exact certificate checking, numerical verification,
scientific interpretation, and human decisions. It also has examples of
retaining selected failures, corrections, and deprecated paths. These are
engineering and documentation practices, not proof that the overall workflow
is scientifically validated or more productive.

The report should advance beyond Draft only when its claim ledger is reviewed,
every affirmative case-study claim resolves to an immutable public artifact,
rights are cleared, and limitations remain visible in the released files.

## Evidence references

### Mothership and methodology

- **[M1]** Project Koios, commit
  [`965181d89d607fb00469560c94fd50b7a28eaa9d`](https://github.com/eragasa/projectkoios/commit/965181d89d607fb00469560c94fd50b7a28eaa9d),
  [`docs/architecture.scientific-platform-thesis.md`, lines 43–57](https://github.com/eragasa/projectkoios/blob/965181d89d607fb00469560c94fd50b7a28eaa9d/docs/architecture.scientific-platform-thesis.md#L43-L57).
- **[M2]** Same commit,
  [`docs/architecture/README.md`, lines 60–67](https://github.com/eragasa/projectkoios/blob/965181d89d607fb00469560c94fd50b7a28eaa9d/docs/architecture/README.md#L60-L67).
- **[M3]** Same commit,
  [`docs/policies/task-and-recovery-records.md`, lines 135–148](https://github.com/eragasa/projectkoios/blob/965181d89d607fb00469560c94fd50b7a28eaa9d/docs/policies/task-and-recovery-records.md#L135-L148).

### Formal and Lean

- **[F1]** Project Koios Formal, commit
  [`26603110e9d64cd51c9101eff68060307f258a18`](https://github.com/eragasa/projectkoios-formal/commit/26603110e9d64cd51c9101eff68060307f258a18),
  `docs/formal-vs-numerical-evidence.md`,
  [lines 1–28](https://github.com/eragasa/projectkoios-formal/blob/26603110e9d64cd51c9101eff68060307f258a18/docs/formal-vs-numerical-evidence.md#L1-L28)
  and [lines 84–95](https://github.com/eragasa/projectkoios-formal/blob/26603110e9d64cd51c9101eff68060307f258a18/docs/formal-vs-numerical-evidence.md#L84-L95).
- **[F2]** Same commit,
  [`BG-RAGASA2026A-THM-032` proof dossier, lines 9–33](https://github.com/eragasa/projectkoios-formal/blob/26603110e9d64cd51c9101eff68060307f258a18/proofs/BandGauge/Papers/Ragasa2026A/BG-RAGASA2026A-THM-032-constructed-false-positive.tex#L9-L33).
- **[F3]** Same commit,
  [`lean-toolchain`](https://github.com/eragasa/projectkoios-formal/blob/26603110e9d64cd51c9101eff68060307f258a18/lean-toolchain)
  and [`lakefile.toml`, lines 5–8](https://github.com/eragasa/projectkoios-formal/blob/26603110e9d64cd51c9101eff68060307f258a18/lakefile.toml#L5-L8).
- **[F4]** Same commit,
  [`docs/certificates.md`, lines 15–31](https://github.com/eragasa/projectkoios-formal/blob/26603110e9d64cd51c9101eff68060307f258a18/docs/certificates.md#L15-L31).
- **[F5]** Same commit,
  [`docs/theorem-manifest.md`, lines 1–18](https://github.com/eragasa/projectkoios-formal/blob/26603110e9d64cd51c9101eff68060307f258a18/docs/theorem-manifest.md#L1-L18).

### Optimization and Numerics

- **[O1]** Project Koios Optimization, commit
  [`b722edab216ef416b8b4affa902b04a26e3da98b`](https://github.com/eragasa/projectkoios-optimization/commit/b722edab216ef416b8b4affa902b04a26e3da98b),
  [`README.md`, lines 1–27](https://github.com/eragasa/projectkoios-optimization/blob/b722edab216ef416b8b4affa902b04a26e3da98b/README.md#L1-L27)
  and [lines 132–165](https://github.com/eragasa/projectkoios-optimization/blob/b722edab216ef416b8b4affa902b04a26e3da98b/README.md#L132-L165).
- **[O2]** Same commit,
  [`test__NumpyFiniteFourierSeriesEvaluator__numerical.py`, lines 21–86](https://github.com/eragasa/projectkoios-optimization/blob/b722edab216ef416b8b4affa902b04a26e3da98b/tests/projectkoios/numerics/finite_periodic/numpy/finite_series/test__NumpyFiniteFourierSeriesEvaluator__numerical.py#L21-L86).
- **[O3]** Same commit,
  [`test__NumpyFinitePeriodicTransforms__integration.py`, lines 83–170](https://github.com/eragasa/projectkoios-optimization/blob/b722edab216ef416b8b4affa902b04a26e3da98b/tests/projectkoios/numerics/finite_periodic/numpy/test__NumpyFinitePeriodicTransforms__integration.py#L83-L170).
- **[O4]** Same commit,
  [`transforms/numerics.md`, lines 63–73](https://github.com/eragasa/projectkoios-optimization/blob/b722edab216ef416b8b4affa902b04a26e3da98b/docs/architecture/projectkoios/numerics/finite_periodic/transforms/numerics.md#L63-L73).
- **[O5]** Same commit,
  [`NOTICE`, lines 1–17](https://github.com/eragasa/projectkoios-optimization/blob/b722edab216ef416b8b4affa902b04a26e3da98b/NOTICE#L1-L17).
- **[O6]** Project Koios Optimization, immutable public correction commit
  [`00c60201d16f2ee61e5fffd83a1a1f24cd327672`](https://github.com/eragasa/projectkoios-optimization/commit/00c60201d16f2ee61e5fffd83a1a1f24cd327672),
  [`test__NumpyFinitePeriodicTransforms__integration.py`, lines 140–170](https://github.com/eragasa/projectkoios-optimization/blob/00c60201d16f2ee61e5fffd83a1a1f24cd327672/tests/projectkoios/numerics/finite_periodic/numpy/test__NumpyFinitePeriodicTransforms__integration.py#L140-L170).
- **[O7]** Same provisional checkpoint,
  [`pyproject.toml`, lines 6–13](https://github.com/eragasa/projectkoios-optimization/blob/b722edab216ef416b8b4affa902b04a26e3da98b/pyproject.toml#L6-L13).

### PhysKit

- **[P1]** Project Koios PhysKit, commit
  [`11e58938ac8d0022f9e6df3aba7ca8757b4a9f88`](https://github.com/eragasa/projectkoios-physkit/commit/11e58938ac8d0022f9e6df3aba7ca8757b4a9f88),
  [`test__MorsePotential__evaluate.py`, lines 42–94](https://github.com/eragasa/projectkoios-physkit/blob/11e58938ac8d0022f9e6df3aba7ca8757b4a9f88/tests/projectkoios/physkit/solidstate/interatomic_potentials/pair/morse/test__MorsePotential__evaluate.py#L42-L94).
- **[P2]** Same commit,
  [`docs/provenance/periodic-cosine-potential-library.md`, lines 32–37](https://github.com/eragasa/projectkoios-physkit/blob/11e58938ac8d0022f9e6df3aba7ca8757b4a9f88/docs/provenance/periodic-cosine-potential-library.md#L32-L37).
- **[P3]** Same commit,
  `docs/provenance/oblique-periodic-boundary-prototype-review.md`,
  [lines 9–24](https://github.com/eragasa/projectkoios-physkit/blob/11e58938ac8d0022f9e6df3aba7ca8757b4a9f88/docs/provenance/oblique-periodic-boundary-prototype-review.md#L9-L24)
  and [lines 51–75](https://github.com/eragasa/projectkoios-physkit/blob/11e58938ac8d0022f9e6df3aba7ca8757b4a9f88/docs/provenance/oblique-periodic-boundary-prototype-review.md#L51-L75).
- **[P4]** Same commit,
  `docs/provenance/finite-periodic-lattice-source-mapping.md`,
  [lines 10–21](https://github.com/eragasa/projectkoios-physkit/blob/11e58938ac8d0022f9e6df3aba7ca8757b4a9f88/docs/provenance/finite-periodic-lattice-source-mapping.md#L10-L21)
  and [lines 114–147](https://github.com/eragasa/projectkoios-physkit/blob/11e58938ac8d0022f9e6df3aba7ca8757b4a9f88/docs/provenance/finite-periodic-lattice-source-mapping.md#L114-L147).
- **[P5]** Same commit,
  [`NOTICE`, lines 1–6](https://github.com/eragasa/projectkoios-physkit/blob/11e58938ac8d0022f9e6df3aba7ca8757b4a9f88/NOTICE#L1-L6).
- **[P6]** Same commit,
  [`pyproject.toml`, lines 5–12](https://github.com/eragasa/projectkoios-physkit/blob/11e58938ac8d0022f9e6df3aba7ca8757b4a9f88/pyproject.toml#L5-L12).

### `ksdft2effmass`

- **[K1]** `ksdft2effmass`, commit
  [`5aaff25b784c7d1bc079a3030a73be387dc11a0f`](https://github.com/eragasa/ksdft2effmass/commit/5aaff25b784c7d1bc079a3030a73be387dc11a0f),
  `particle-in-box/README.md`,
  [lines 1–8](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/calculations/research-monograph/particle-in-box/README.md#L1-L8)
  and [lines 159–222](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/calculations/research-monograph/particle-in-box/README.md#L159-L222).
- **[K2]** Same commit,
  [`particle-in-box/SHA256SUMS`](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/calculations/research-monograph/particle-in-box/SHA256SUMS).
- **[K3]** Same commit,
  [`particle-in-box/protocol.md`, lines 85–87](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/calculations/research-monograph/particle-in-box/protocol.md#L85-L87)
  and [lines 146–168](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/calculations/research-monograph/particle-in-box/protocol.md#L146-L168).
- **[K4]** Same commit,
  [`impurity-defect-2d/DEPRECATION.md`, lines 1–18](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/calculations/research-monograph/impurity-defect-2d/DEPRECATION.md#L1-L18).
- **[K5]** Same commit,
  `composite-band-alignment-and-locality/periodic1d/README.md`,
  [lines 3–14](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/experiments/periodic-reduction/composite-band-alignment-and-locality/periodic1d/README.md#L3-L14)
  and [lines 48–57](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/experiments/periodic-reduction/composite-band-alignment-and-locality/periodic1d/README.md#L48-L57).
- **[K6]** Same commit,
  [`protocol.md`, lines 88–114](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/experiments/periodic-reduction/composite-band-alignment-and-locality/periodic1d/protocol.md#L88-L114).
- **[K7]** Same commit,
  `THIRD_PARTY_NOTICES.md`,
  [lines 1–30](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/THIRD_PARTY_NOTICES.md#L1-L30),
  [lines 32–69](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/THIRD_PARTY_NOTICES.md#L32-L69),
  and [lines 71–95](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/THIRD_PARTY_NOTICES.md#L71-L95).
- **[K8]** Same commit,
  [`research-monograph/chapters/preface.tex`, lines 17–28](https://github.com/eragasa/ksdft2effmass/blob/5aaff25b784c7d1bc079a3030a73be387dc11a0f/docs/publications/research-monograph/chapters/preface.tex#L17-L28).

### Pi coordination harness

- **[H1]** Project Koios Bootstrap, commit
  [`7fa09bc3b631984d3b049b00d858935575d5687d`](https://github.com/eragasa/projectkoios-bootstrap/commit/7fa09bc3b631984d3b049b00d858935575d5687d),
  [`docs/harness-incubation.md`, lines 8–14](https://github.com/eragasa/projectkoios-bootstrap/blob/7fa09bc3b631984d3b049b00d858935575d5687d/docs/harness-incubation.md#L8-L14)
  and [lines 31–59](https://github.com/eragasa/projectkoios-bootstrap/blob/7fa09bc3b631984d3b049b00d858935575d5687d/docs/harness-incubation.md#L31-L59).
- **[H2]** Same commit,
  `docs/candidates/coordinator-startup.md`,
  [lines 3–30](https://github.com/eragasa/projectkoios-bootstrap/blob/7fa09bc3b631984d3b049b00d858935575d5687d/docs/candidates/coordinator-startup.md#L3-L30)
  and [lines 51–101](https://github.com/eragasa/projectkoios-bootstrap/blob/7fa09bc3b631984d3b049b00d858935575d5687d/docs/candidates/coordinator-startup.md#L51-L101).
- **[H3]** Same commit,
  `docs/candidates/named-repository-sessions.md`,
  [lines 3–14](https://github.com/eragasa/projectkoios-bootstrap/blob/7fa09bc3b631984d3b049b00d858935575d5687d/docs/candidates/named-repository-sessions.md#L3-L14)
  and [lines 39–86](https://github.com/eragasa/projectkoios-bootstrap/blob/7fa09bc3b631984d3b049b00d858935575d5687d/docs/candidates/named-repository-sessions.md#L39-L86).
- **[H4]** Same commit,
  `docs/candidates/herdr-session-continuity.md`,
  [lines 3–9](https://github.com/eragasa/projectkoios-bootstrap/blob/7fa09bc3b631984d3b049b00d858935575d5687d/docs/candidates/herdr-session-continuity.md#L3-L9),
  [lines 49–67](https://github.com/eragasa/projectkoios-bootstrap/blob/7fa09bc3b631984d3b049b00d858935575d5687d/docs/candidates/herdr-session-continuity.md#L49-L67),
  and [lines 94–139](https://github.com/eragasa/projectkoios-bootstrap/blob/7fa09bc3b631984d3b049b00d858935575d5687d/docs/candidates/herdr-session-continuity.md#L94-L139).

### External release guidance

- **[Z1]** Zenodo, [Manage versions](https://help.zenodo.org/docs/deposit/manage-versions/), accessed 2026-10-21.
- **[Z2]** Zenodo, [What is DOI versioning?](https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning), accessed 2026-10-21.
- **[Z3]** Zenodo, [Digital Object Identifier](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/), accessed 2026-10-21.
- **[Z4]** Zenodo, [Manage files](https://help.zenodo.org/docs/deposit/manage-files/#modify), accessed 2026-10-22.
- **[A1]** arXiv, [Submission overview](https://info.arxiv.org/help/submit/index.html), accessed 2026-10-21.
