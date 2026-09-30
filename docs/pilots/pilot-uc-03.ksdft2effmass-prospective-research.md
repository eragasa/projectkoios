# PILOT-UC-03-01: `ksdft2effmass` prospective research

## Record status

- **Pilot ID:** `PILOT-UC-03-01`
- **Definition status:** Draft
- **Execution status:** Not authorized
- **Use case:**
  [UC-03](../use-cases/uc-03.evidence-grounded-prospective-research.md)
- **Evidence architecture:** [search](../architecture.search.md) and
  [applications](../architecture.applications.md)
- **Workflow architecture:**
  [planned workflow boundary](../architecture.md#planned-architecture)
- **Parent roadmaps:** `RAG-ROADMAP-01` and `WORKFLOW-TRANSFER-01`

This definition does not authorize a computation, software or manuscript
change, contract acceptance, artifact publication, scientific acceptance,
release, or deployment.

## Objective

Demonstrate one complete prospective-research cycle for `ksdft2effmass`:
identify a bounded unresolved question, freeze a hypothesis and protocol before
execution, run one separately authorized bounded calculation, ingest its
outputs, and compare the observations with pre-recorded decision criteria.

A negative or inconclusive result is a valid pilot outcome when its provenance
and prospective evaluation are complete.

## Bounded scope

The pilot contains:

- one research question;
- one primary hypothesis and at least one competing explanation or falsifying
  observation;
- one bounded parameter region;
- one identified software baseline;
- one prospective protocol revision;
- one dry-run or synthetic failure fixture;
- at most one effect-eligible real execution occurrence per run revision;
- one immutable observation generation; and
- one reviewed, scope-limited research disposition.

The exact scientific question and unpublished inputs remain in private or
application-owned records rather than this public definition.

## Exclusions

The pilot does not include:

- an unbounded parameter sweep;
- autonomous choice of the research agenda;
- claims of novelty based on retrieval absence;
- automatic software modification;
- automatic manuscript editing;
- automatic retry after ambiguous completion;
- scientific acceptance based on workflow success;
- CPN authority;
- artifact publication; or
- release or deployment.

## Participating owners

| Owner | Pilot responsibility |
|---|---|
| `projectkoios` | Pilot definition and cross-repository architecture |
| `projectkoios-research` | Question, hypothesis, scientific review, evaluation meaning, and disposition |
| `ksdft2effmass` | Application code, project-specific protocol, calculations, and public results when authorized |
| `projectkoios-ingestion` | Input, output, observation, and derivation processing |
| `projectkoios-search` | Literature and prior-calculation evidence retrieval |
| `projectkoios-references` | Bibliographic identity, acquisition, and rights evidence |
| `projectkoios-workflow` | Effect-free planning, workflow state, and runtime semantics |
| Software owner | Software baseline and any separately authorized code change |
| Deployment owner | Private composition, authority, worker capability, storage, and reconciliation |

Reusable conformance fixtures remain with component owners. Project-specific
scientific artifacts remain with the application or private store.

## Input classes

### Private or application-owned inputs

- bounded research question;
- literature evidence snapshot;
- prior computational evidence;
- hypothesis and competing alternatives;
- code and environment identities;
- parameter and input manifests;
- prospective protocol and decision criteria;
- execution authority references;
- raw and derived outputs; and
- scientific review decisions.

### Public inputs

- use-case and architecture records;
- component contract identifiers;
- synthetic workflow, crash, ambiguity, and reconciliation fixtures;
- public software baselines when applicable; and
- public conformance commands.

Unpublished inputs and outputs are never copied into this definition.

## Required readiness evidence

Before a real execution is requested, the pilot owner records:

1. executable deployment-adapter ownership;
2. actual lifecycle state of required workflow and runtime contracts;
3. exact operation identity, schemas, and bounds;
4. worker capability and environment evidence;
5. artifact-store write and receipt behavior;
6. idempotency and ambiguity-reconciliation policy;
7. source, input, code, and dependency identities;
8. reviewed prospective protocol and stop conditions;
9. fresh attempt-bound authority requirements;
10. privacy review; and
11. synthetic crash and reconciliation evidence.

If these are incomplete, the pilot remains planning-only or uses synthetic
fixtures. Documentation completion does not authorize a real computation.

## Procedure

### Phase 0: Freeze the pilot revision

1. Record component and contract revisions.
2. Identify the research-question record without copying private content.
3. Freeze metric definitions, evaluation criteria, and artifact routing.
4. Record the distinction between exploratory and confirmatory work.
5. Record readiness blockers and stop conditions.

### Phase 1: Establish the evidence snapshot

1. Retrieve literature evidence with exact source locators.
2. Retrieve prior calculations with exact code, input, environment, output,
   convergence, and warning references.
3. Keep literature and computational evidence in separate roles.
4. Record unavailable sources, missing provenance, convention conflicts, and
   insufficient evidence.
5. Identify the immutable evidence snapshot motivating the hypothesis.

Retrieval absence is not evidence of novelty.

### Phase 2: Review the hypothesis

1. Record a primary prospective hypothesis.
2. Record at least one alternative explanation or observation that would
   challenge the primary hypothesis.
3. State the applicable physical and numerical regime.
4. State assumptions, units, coordinate systems, and source conventions.
5. Link every literature-dependent premise to reference evidence.
6. Mark model-generated hypotheses `AUTOMATED_UNREVIEWED` until reviewed.
7. Record a human disposition permitting protocol development without
   declaring the hypothesis correct.

### Phase 3: Author the prospective protocol

The project-specific protocol records:

- input and software-baseline identities;
- model and approximation choices;
- parameter values, ranges, and units;
- control or reference calculations;
- numerical resolution and convergence checks;
- resource and time bounds;
- expected output artifact kinds;
- failure and ambiguity behavior;
- stopping conditions;
- evaluation metrics;
- predicted observations; and
- decision criteria for supported, challenged, inconclusive, and invalid
  outcomes.

Any adaptive step must identify in advance the evidence that permits it and the
bounds that remain applicable.

### Phase 4: Seal and review

1. Review the protocol for confounding, circularity, underdetermination,
   convention mismatch, inadequate controls, and insufficient bounds.
2. Resolve or explicitly retain review findings.
3. Create an immutable prospective-package identity containing references to
   the question, evidence snapshot, hypothesis, protocol, and review.
4. Append an event showing that this exact package revision preceded execution.
5. Treat any later protocol change as a new revision.

### Phase 5: Validate planning without effects

1. Produce the workflow plan deterministically.
2. Verify operation and subject binding.
3. Verify parameter, resource, and artifact bounds.
4. Verify that workflow state contains compact references rather than private
   payloads.
5. Run synthetic success, failure, timeout, and ambiguous-completion fixtures.
6. Confirm that ambiguity enters query-only reconciliation and never triggers
   automatic retry.

### Phase 6: Authorize one bounded attempt

1. Runtime policy verifies authority authenticity, expiry, revocation,
   applicability, scope, and worker capability.
2. Reserve at most one effect-eligible occurrence for the run revision.
3. Issue fresh dispatch authority bound to one attempt.
4. Record append-only dispatch evidence.

Planning success does not grant this authority.

### Phase 7: Execute and capture

1. The worker receives only admitted inputs and capabilities.
2. Runtime history records progress, completion, failure, cancellation, and
   reconciliation events.
3. The worker emits raw outputs and artifact-store receipts.
4. The source evidence and sealed prospective package remain unchanged.
5. Timeout, lease expiry, or worker disappearance does not prove non-application.

### Phase 8: Ingest observations

1. Verify raw output identities and receipts.
2. Preserve failed, partial, null, and unexpected outputs.
3. Emit an immutable observation generation.
4. Link every observation to exact inputs, software, environment, protocol,
   occurrence, and attempt.
5. Emit derived tables, plots, or metrics as separate artifacts with derivation
   evidence.
6. Do not label a derived explanation as an observation.

### Phase 9: Evaluate prospectively

1. Apply the metrics and decision criteria from the sealed protocol.
2. Record missing data, convergence failures, exclusions, deviations, and
   ambiguity.
3. Compare the predicted and observed quantities without changing the original
   criteria.
4. Label any pattern noticed only after execution as post-observation.
5. Record a human disposition limited to the tested scope.

### Phase 10: Replay and continue

1. Replay workflow history and artifact derivations.
2. Verify deterministic identities where required.
3. Reproduce the evaluation from immutable observations and criteria.
4. Create a new prospective revision for any follow-up study.
5. Route later manuscript, software, release, or publication work through its
   own authority.

## Metrics

Protocol-specific scientific metrics remain in the application-owned
prospective record. The pilot also records infrastructure metrics:

- evidence-locator resolution;
- prospective-package completeness;
- plan determinism;
- bounds-validation coverage;
- runtime-event replay differences;
- artifact-receipt resolution;
- input-to-output provenance completeness;
- raw-to-derived lineage completeness;
- pre-recorded-criteria coverage;
- protocol-deviation count;
- post-observation hypothesis labeling; and
- ambiguity-reconciliation behavior.

Metric definitions and thresholds are frozen before the evaluated execution.

## Acceptance evidence

The pilot is technically demonstrated when reviewed evidence shows:

1. the prospective package predates and identifies the execution attempt;
2. literature, prior calculations, hypothesis, protocol, and observations
   retain distinct roles;
3. planning performs no external effect;
4. exact operation, subject, parameter, resource, and artifact bounds are
   enforced;
5. dispatch authority is fresh and attempt-bound;
6. runtime history and artifact receipts replay according to the applicable
   contract;
7. every output resolves to exact inputs, code, environment, protocol,
   occurrence, and attempt;
8. raw observations remain separate from derived analysis and interpretation;
9. failed, null, negative, and surprising outcomes remain visible;
10. evaluation uses the pre-recorded metrics and decision criteria;
11. deviations and post-observation hypotheses are explicit;
12. ambiguous effects enter reconciliation instead of automatic retry;
13. private payloads remain outside Git and public logs; and
14. technical completion does not trigger scientific, manuscript, software,
    release, or publication authority.

Scientific success is not required. An inconclusive or hypothesis-challenging
result may satisfy the pilot.

## Stop conditions

Stop planning or execution and preserve evidence if:

- the prospective package is not immutable before dispatch;
- code, environment, input, or protocol identity changes unexpectedly;
- operation or resource bounds cannot be enforced;
- required worker capability or authority evidence is absent;
- private payloads would enter workflow state or public logs;
- artifact receipts cannot be verified;
- an effect has ambiguous completion;
- convergence or validity gates fail; or
- a request attempts to infer scientific acceptance from runtime success.

An ambiguous effect is reconciled before any new attempt is considered.

## Artifact routing

| Artifact | Location |
|---|---|
| Pilot definition | This file |
| Reusable workflow and ingestion fixtures | Owning component repositories |
| Research identity and relationship | `projectkoios-research` |
| Project-specific prospective protocol | `ksdft2effmass`, when separately authorized and suitable for version control |
| Unpublished hypothesis, inputs, outputs, and review payloads | Configuration-resolved private store |
| Run manifest, runtime history, receipts, metrics, and decisions | `state/runs/<run-id>/` |
| Public project result | `ksdft2effmass`, only after separate review and authorization |
| Mutable coordination | Parent and owner issues |
| Sanitized pilot completion summary | Appropriate owner record without private payloads |
