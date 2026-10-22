# Evidence and release plan: audit-first methodology report

- **Plan status:** Draft
- **Report:** [Project Koios: An audit-first, LLM-assisted workflow for
  verifiable computational physics](project-koios-audit-first-methodology.md)
- **Evidence ledger:** [Bounded machine-readable
  JSON](project-koios-audit-first-methodology-evidence.json)
- **Current authority:** Local drafting and review preparation only
- **Not authorized:** Commit, push, release, publication, arXiv submission,
  Zenodo deposit, or DOI reservation

## 1. Objective

Develop one evidence-bounded living source that can later support an immutable
technical or documented-experience milestone. The report must remain useful if
none of its broader scientific or productivity hypotheses are established.

The plan does not authorize the work it describes. Completion of a technical
check does not grant scientific, editorial, release, or publication authority.

## 2. Document placement and lifecycle

The mothership repository owns the cross-repository report because the subject
is the Project Koios workflow rather than one component's implementation or one
application's scientific result.

- Living source:
  `docs/reports/project-koios-audit-first-methodology.md`
- Supporting plan:
  `docs/reports/project-koios-audit-first-methodology-plan.md`
- Bounded machine-readable evidence ledger:
  `docs/reports/project-koios-audit-first-methodology-evidence.json`
- Catalog:
  `docs/reports/README.md`

Proposed report states:

1. **Draft living source** — mutable, evidence gaps visible, no release claim.
2. **Review candidate** — frozen claim ledger and complete public locators;
   rights and independent review still explicit.
3. **Milestone candidate** — render and deposit bundle reproducible locally;
   authorship, rights, metadata, and human release decision complete.
4. **Released milestone** — a versioned Zenodo record exists after separate
   authorization, with its checksum manifest retained at a separately cited
   immutable Git revision.
5. **Optional submitted article** — later arXiv or venue submission, separately
   authorized and versioned.

This task creates only state 1.

## 3. Claim-admission rule

An affirmative Project Koios methodology or case-study evidence claim enters
the main narrative only when the ledger records:

- a stable claim identifier;
- exact wording and evidence class;
- owner repository and immutable revision;
- repository-relative artifact and pinpoint locator;
- public or local-only evidence status;
- relevant command, checker, comparator, tolerance, and environment;
- what the evidence does not establish;
- rights and third-party provenance status;
- technical review disposition; and
- human decision state where acceptance is required.

The narrative location of every admitted claim must carry a stable `PKAM-C-*`
anchor. The ledger's `report_locator` must identify that anchor rather than a
mutable paragraph description.

A plan, issue, directory name, branch name, or model statement is not completion
evidence. A public provisional branch may support an experience observation but
must not be represented as an adopted release. Local or uncommitted results may
be recorded as leads, not as immutable milestone evidence.

## 4. Evidence classes

Use these labels consistently:

| Label | Meaning |
|---|---|
| `SOFTWARE_CONFORMANCE` | Mapped software behavior under declared tests |
| `LEAN_THEOREM` | Kernel-checked proposition under explicit assumptions and axiom report |
| `EXACT_CHECKED_CERTIFICATE` | Exact data accepted by a checker with a proved conclusion bridge |
| `NUMERICAL_VERIFICATION` | Bounded comparison with explicit oracle, tolerance, environment, and domain |
| `SCIENTIFIC_VALIDATION` | Scope-limited scientific claim assessed against identified reference evidence and protocol |
| `HUMAN_DECISION` | Acceptance, rejection, authorization, release, or publication decision by the responsible person |
| `EXPERIENCE_OBSERVATION` | Documented project occurrence that is not promoted into another evidence class |
| `PLANNED` | Specified future work with no completion claim |

Never combine `LEAN_THEOREM` and `EXACT_CHECKED_CERTIFICATE` merely because both
occur in Lean. Never call binary64 KKT ratios, residuals, rank decisions,
Hermiticity defects, or high-precision comparisons exact certificates. Never
call verification against an analytical model material validation.

## 5. Current evidence snapshot

### 5.1 Mothership

- Revision: `965181d89d607fb00469560c94fd50b7a28eaa9d`
- Role: proposed control/execution/evidence-plane thesis; current evidence-kind
  and outcome-dimension boundaries
- Maturity: public main; architecture thesis itself remains Proposed
- Use: methodology vocabulary, not evidence that the whole platform exists

### 5.2 Formal

- Revision: `26603110e9d64cd51c9101eff68060307f258a18`
- Role: pinned Lean/Mathlib environment, theorem manifest, exact analytic source
  certificate, proof dossiers, and explicit non-claims
- Maturity: immutable public checkpoint on
  `origin/work/paper-a-diagnostic-producer-audit`; not main, a tag, or a release
- Completed evidence admitted: `LEAN_THEOREM` and one bounded
  `EXACT_CHECKED_CERTIFICATE` for the encoded analytic construction
- Not admitted: runtime scientific certificate, numerical/material validation,
  independent expert review, or publication acceptance
- Local/uncommitted exclusion: later dirty worktree content is not cited;
  local-only checkpoints `002e1a2b...`, `2b2f9c05...`, and `289f1194...`
  remain outside the public Draft regardless of their local checks
- Review item: reconcile any stale summary/count language across Formal's
  authority and certificate documents before a milestone; the certificate
  inventory and theorem manifest must be the claim source of record

### 5.3 Optimization and Numerics

- Accepted public-main reference:
  `be104c0211e2aae3c712fcbefac451815e84e87b`
- Broader public provisional reference:
  `b722edab216ef416b8b4affa902b04a26e3da98b`
- Role: finite-periodic transforms and diagnostics, least squares, affine and
  quadratic methods, Procrustes alignment, spectra/projectors, source-level test
  definitions for prospective numerical verification, provenance mappings
- Maturity: `b722ed...` is a clean public migration branch at package version
  `0.1.0.dev0`; it is not a tag, release, or adopted downstream baseline
- Documented evidence admitted from the provisional branch:
  source-level test definitions for prospective numerical verification and
  correction history; no executed numerical-verification result is admitted
- Not admitted: exact arithmetic certificate, backward-error certificate, UQ,
  scientific interpretation, adopted release, or publication authority
- Local rerun exclusion: reported 869-test, lint, type, and reproducible-build
  results are local observations rather than retained CI evidence
- Milestone choice required: either cite the branch explicitly as provisional or
  wait for an adopted immutable commit designated as the main or release
  baseline; never imply release status

### 5.4 PhysKit

- Revision: `11e58938ac8d0022f9e6df3aba7ca8757b4a9f88`
- Role: reusable computational-physics contracts, source-level numerical
  consistency-check definitions, extraction provenance, rejected-prototype
  review
- Maturity: public main at inspection; development version `0.1.3.dev0`, not a
  release
- Documented evidence admitted: source-level consistency-check definitions and
  `EXPERIENCE_OBSERVATION` for rejection, correction, replacement, and byte
  preservation; no executed numerical-verification result is admitted
- Not admitted: material validation or human scientific acceptance
- Local rerun exclusion: reported repository tests, Ruff, and formatting results
  are local observations rather than retained public evidence

### 5.5 `ksdft2effmass`

- Revision: `5aaff25b784c7d1bc079a3030a73be387dc11a0f`
- Role: retained illustrative particle-in-a-box numerical experiment,
  independent verifiers, SHA-256 manifest, explicit interpretation limits,
  historical-interface deprecation, prospective composite-band protocol
- Maturity: immutable public checkpoint identified through
  `origin/work/monograph-current-library-capabilities`; the exact commit is also
  reachable from public `main`, but branch reachability is not evidence of an
  adopted release and no release or publication status is claimed
- Completed evidence admitted: bounded `NUMERICAL_VERIFICATION` for the finite
  illustrative model and `EXPERIENCE_OBSERVATION` for deprecation/preservation
- Planned evidence: composite-band successor remains `MIGRATION_IN_PROGRESS`,
  with no immutable experiment version or maintained run
- Not admitted: semiconductor/material validation, DFT or Wannier validation,
  UQ, or new production calculation evidence
- Local/uncommitted exclusion: the dirty active worktree is not used as evidence

### 5.6 Pi/LLM coordination harness

- Revision: `7fa09bc3b631984d3b049b00d858935575d5687d`
- Role: accepted incubation boundary and Candidate startup, deterministic naming,
  scoped coordination guard, and read-only continuity diagnostic
- Maturity: public `origin/master`; candidate mechanics are not validated generic
  tooling
- Completed evidence admitted: `SOFTWARE_CONFORMANCE` and bounded
  `EXPERIENCE_OBSERVATION` for an operational failure and fail-closed response
- Local rerun exclusion: 26 focused Python tests, 7 Node checks, Ruff, and Mypy
  were reported passing locally but are not retained public CI evidence
- Not admitted: proof that an LLM follows prompts, authorization/security
  service, end-to-end availability, recurrence, or productivity gain

## 6. Case-study completion matrix

| Case | Completed/documented | Planned or missing |
|---|---|---|
| Formal/Lean | Pinned kernel/dependencies; theorem manifest; exact analytic source certificate; axiom and boundary reporting | Runtime data/parser binding; owner-reviewed scientific crosswalk; independent expert review |
| Optimization | Provisional public source; source-level test definitions for prospective numerical verification; correction commits; exact source/provenance mappings | Executed retained numerical-verification result; adopted release baseline; retained CI evidence; exact certificate layer where scientifically required; consumer scientific decisions |
| PhysKit | Public-main source-level Morse consistency-check definition; provenance; rejected prototype and maintained replacement | Executed retained check result; material-specific validation |
| `ksdft2effmass` | Retained finite illustrative experiment; independent verifiers; checksums; limitations; historical CLI deprecation | Composite-band maintained run and immutable `.v1`; material validation; authorized production calculations |
| Pi harness | Public candidate source/tests; deterministic and fail-closed boundaries; documented pane-loss incident | Independent recurrence; promotion decision; real end-to-end evidence; LLM compliance study; productivity study |

## 7. Failures, reviews, corrections, and rollback ledger

The milestone ledger should include at least one bounded example in each
available category without inventing symmetry across cases.

| Category | Current public example | Claim boundary |
|---|---|---|
| Scientific counterexample | Formal exact constructed false positive | A proved finite analytic construction, not runtime or material evidence |
| Diagnostic correction | Optimization independent Hermiticity defect evidence | A specific corrected test path, not global independence |
| Failed prototype review | PhysKit oblique-periodic notebook | Invalid source and nonreproducible saved outputs; corrected behavior lives in maintained destinations |
| Deprecation with preservation | `ksdft2effmass` Stage C CLI | Historical bytes remain authoritative for old results; newer adapters grant no execution/scientific authority |
| Operational failure | Bootstrap pane closure instead of detach | One observed failure supports a bounded read-only diagnostic, not recurrence or automatic recovery |

Before a milestone, record for each example:

- initiating defect or finding;
- exact pre-correction revision/blob where public and redistributable;
- review outcome;
- exact correction or replacement revision;
- verification performed;
- whether rollback was exercised, merely available, or not evaluated; and
- unresolved limitations.

The current report may say selected artifacts are recoverable. It may not claim
that a general rollback mechanism was tested.

## 8. Review plan

### 8.1 Technical evidence review

For every repository:

1. Verify that each cited commit is reachable on the stated public remote using
   read-only evidence available at review time.
2. Verify every path and line locator at that commit.
3. Re-run only commands authorized by the owner, recording tool versions and
   exact results in a public, immutable artifact if they will support a claim.
4. Check that evidence labels match owner terminology.
5. Confirm that planned items are not narrated in the past tense.
6. Check negative cases and non-claims, not only passing paths.

### 8.2 Independent claim review

Request at least:

- one formal-method review of theorem/certificate wording;
- one numerical-method review of comparator independence and tolerance claims;
- one computational-physics review of validation boundaries;
- one reproducibility/provenance review; and
- one editorial review for overclaiming and internal consistency.

A finding disposition is not an aggregate review outcome, operator request,
scientific decision, or publication decision. Record the dimensions separately:

- `FindingDisposition`:
  `MUST_FIX | HUMAN_DECISION_REQUIRED | SAFE_TO_DEFER | NO_ACTION_REQUIRED`;
- aggregate `ReviewOutcome`:
  `CHANGES_REQUIRED | REVIEW_INCONCLUSIVE | NO_BLOCKING_FINDINGS`; and
- `OperatorRequest`:
  `NONE | CLARIFICATION_REQUIRED | DECISION_REQUIRED |
  AUTHORIZATION_REQUIRED | OUTCOME_CONFIRMATION_REQUIRED`.

A technical review may have `NO_BLOCKING_FINDINGS` while a protected next action
still has `AUTHORIZATION_REQUIRED`. None of these enums establishes scientific
validation, publication acceptance, or release authority.

### 8.3 Scientific review

No scientific-validation conclusion is currently planned for the first
milestone. If one is later proposed, add a separate protocol identifying:

- scientific claim and applicability domain;
- reference observations or artifacts;
- uncertainty and discrepancy treatment;
- competing explanations and falsification conditions;
- reviewer expertise and conflicts; and
- accountable human disposition.

## 9. Productivity-study boundary

Do not add productivity language unless a prospective study exists. A minimally
credible study would predeclare:

- task inventory and sampling;
- baseline and LLM-assisted conditions;
- model, prompt, tool, and environment versions;
- time, cost, correctness, review burden, and rework metrics;
- handling of failed or abandoned tasks;
- reviewer blinding or other bias controls where feasible; and
- statistical and qualitative analysis limits.

Repository growth, commit counts, passing tests, or anecdotal time savings are
not substitutes. Until then the report states only that LLM assistance occurred
in identified artifacts where owners disclosed it.

## 10. Rights and provenance plan

Before a milestone:

1. Confirm authorship and contributor roles.
2. Confirm Apache-2.0 coverage for project-owned cited material without
   extending that conclusion to separately licensed dependencies or artifacts.
3. Review and carry applicable repository notices and license material,
   including Optimization's BSD-2-Clause PyPosPack attribution, PhysKit's KSD
   adaptation notice and provenance mappings, and `ksdft2effmass`
   `THIRD_PARTY_NOTICES.md` entries for SNAKES, Pint, Matplotlib/fonts, and
   `elsarticle`.
4. Inventory every figure, table, quotation, dataset, dependency artifact, and
   third-party source proposed for the deposit.
5. Record permission or license and any required attribution for each deposited
   file; an installed dependency notice does not itself authorize bundling that
   dependency.
6. Exclude private paths, transcripts, credentials, runtime payloads, protected
   excerpts, and unpublished results.
7. Select the report/deposit license through an explicit human decision; do not
   infer it solely from repository code licensing.
8. Record LLM assistance in a venue-appropriate disclosure without presenting
   the model as author or authority.

A digest proves identity, not redistribution rights.

## 11. Reproducible milestone bundle

A future local staging build should produce, without network access:

```text
project-koios-audit-first-methodology-<version>/
├── README.md
├── report.md
├── report.pdf
├── evidence-ledger.csv
├── evidence-manifest.json
├── CITATION.cff
├── LICENSE
├── NOTICE
├── THIRD_PARTY.md
├── build-environment.txt
└── SHA256SUMS
```

The evidence manifest should record report Git commit, source-tree identity,
render command, renderer versions, evidence repository commits, and file hashes.
It should link to owner artifacts rather than vendoring large results or
third-party content. The build must fail if unresolved absolute paths, private
locators, draft-only placeholders, or missing rights fields are detected.

No such bundle is created or published by the current task.

## 12. Zenodo milestone design

Official Zenodo guidance distinguishes:

- a DOI for each specific version; and
- an all-versions/concept DOI representing the linked version family.

Each released report milestone should use a new Zenodo version. Ordinary
corrections should use another version rather than silently changing the same
record. Because Zenodo permits limited post-publication file modification
without changing the DOI, DOI identity alone does not prove byte immutability.
Cite the **version DOI** together with a SHA-256 manifest retained at a
separately cited immutable Git revision when discussing the exact files and
evidence ledger. Use the **all-versions/concept DOI** only for the evolving
report family, and never imply that it freezes one version's files.

Release checklist:

1. Freeze report Git commit and bundle hashes.
2. Complete technical, rights, authorship, and privacy review.
3. Obtain explicit human release/publication authorization.
4. Create the Zenodo version and inspect metadata and files.
5. Record both DOI roles without conflation.
6. Add the version DOI back to the living source only in a later authorized Git
   change.
7. Preserve ordinary corrections as a new version; do not replace the
   historical milestone silently. Record any exceptional rights, privacy, or
   similar remediation performed under the service policy.

Zenodo supports advance DOI reservation, but **no DOI reservation is authorized
or needed now**.

Official guidance:

- <https://help.zenodo.org/docs/deposit/manage-versions/>
- <https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning>
- <https://help.zenodo.org/docs/deposit/about-records/>
- <https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/>
- <https://help.zenodo.org/docs/deposit/manage-files/#modify>

These operational pages are mutable guidance and must be rechecked at any
release-authorization boundary.

## 13. Optional later arXiv path

Consider arXiv only after the report is a refereeable scholarly article rather
than a repository experience note. Required decisions include category,
authors, title/abstract, source format, figures, license, moderation readiness,
and relationship to Zenodo milestones.

If authorized later:

- cite the exact Zenodo version DOI for the accompanying milestone;
- preserve arXiv's own version history for corrections;
- keep repository and evidence locators in the article;
- do not treat arXiv moderation as peer review; and
- do not treat an arXiv identifier as scientific validation.

Official submission overview:
<https://info.arxiv.org/help/submit/index.html>.

This operational page is mutable guidance and must be rechecked at any
submission-authorization boundary.

## 14. Current blockers

- A bounded machine-readable cross-repository evidence ledger exists for this
  Draft, but targeted re-review of the consolidated corrections remains
  incomplete.
- Optimization's broadest evidence is on a public provisional migration branch,
  not an adopted release.
- Formal has no runtime scientific certificate and no recorded independent
  expert scientific review for the cited construction.
- The completed computational examples are primarily finite illustrative or
  numerical-verification cases, not material validation.
- The composite-band successor and broader prospective cases remain planned or
  in migration.
- Harness recurrence, end-to-end availability, and LLM policy compliance are
  unestablished.
- No productivity study exists.
- Report authorship, deposit license, third-party notice set, and figure rights
  are not yet approved for release.
- No human publication decision exists.

## 15. Next safe actions

Without release authority, the safe next actions are:

1. review the Draft for factual overstatement and broken immutable links;
2. maintain and independently review the bounded machine-readable evidence
   ledger as claims change;
3. ask owner repositories to reconfirm evidence classification and maturity for
   any later milestone;
4. resolve Formal summary inconsistencies and Optimization provisional-status
   wording;
5. complete targeted independent technical re-review of corrected claims;
6. decide whether the first milestone remains Markdown-only or adds a rendered
   PDF; and
7. stop before commit, push, release, publication, submission, deposit, or DOI
   reservation unless each action is separately authorized.
