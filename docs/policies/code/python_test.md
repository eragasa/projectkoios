<!-- GENERATED FILE. DO NOT EDIT. -->

# Project Koios Python test policy

> **GENERATED MARKDOWN PROJECTION.**
> [`docs/policies/code/python_test.json`](python_test.json) is authoritative.
> Regenerate this file from that source; do not edit it independently.

- Policy ID: `projectkoios.code.python-test`
- Policy version: `0.1.0`
- Status: **Draft**
- Source SHA-256: `701d8b8529612e9a6821851877155459eb0fdbe5f72284dbb12ed62ced65c03d`

## Purpose

Define Project Koios requirements for proportionate Python tests, maintained evidence, ownership, independent oracles, fixtures, and honest acceptance claims.

## Scope

- New or materially changed Python tests in Project Koios owner repositories.
- Test-owned fixtures, schemas, golden bytes, structured declaration records, ownership records, and parameter cases.
- Software verification and separately authorized numerical verification, scientific validation, or uncertainty-quantification tests.

## Exclusions

- Automatic repository-wide rewrites of conforming existing tests.
- Scientific, numerical, uncertainty-quantification, publication, release, or human-acceptance claims inferred from routine software-verification evidence.
- Production behavior added solely to make test construction convenient.
- Weakening expectations, tolerances, or coverage merely to obtain a pass.

## Precedence

1. Accepted contracts, scientific specifications, and architecture decisions.
2. The owning repository's AGENTS.md, pyproject.toml, and maintained commands.
3. The Project Koios Python code policy.
4. This Project Koios Python test policy.
5. Adapted predecessor conventions recorded under source_provenance.

## Python code-policy requirements

Source: [`docs/policies/code/python.json`](python.json)

- Every named variable has an explicit type annotation where Python syntax permits one.
- Every public and private method has explicit annotations and keyword-only parameters after self or cls except where a protocol requires another signature.
- Every method call spells each argument name where the callable supports keyword arguments.
- Small helper behavior belongs to its cohesive owner; a test-only module helper is acceptable when clearer than an artificial class.
- The test package initializer exposes only a deliberate stable API when a public test-support API is required.

## Adaptation provenance

- Source repository: https://github.com/eragasa/ksdft2effmass
- Source revision: `7bd913151f7e61ed2bdba593df920be36573b502`
- Source license: `Apache-2.0`

Project Koios retains the predecessor's evidence-class separation, routine and claim-bearing profiles, stable evidence identifiers, module metadata, cohesive Test ownership, semantic parameter identities, independent-oracle requirements, exact acceptance, deterministic structural audit, and stop boundaries. It adapts helper placement, test-name spelling, repository paths, command names, and migration timing to Project Koios authority.

### Pinned predecessor inputs

#### `AGENTS.md`

- Source: [AGENTS.md](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/AGENTS.md)
- SHA-256: `72146e726e4251437a14e9ac0cf8c16db2750e8daa471f1a0fe03499697d3a9a`
- Byte count: `35349`
- Use: Testing ownership, Test-class structure, helper placement, resources, negative typing tests, evidence limitations, and stop boundaries.

#### `.pi/skills/develop-python-test-evidence/SKILL.md`

- Source: [.pi/skills/develop-python-test-evidence/SKILL.md](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/.pi/skills/develop-python-test-evidence/SKILL.md)
- SHA-256: `110c3ef295deaa4188a9358638fcb808b9b7e618437fbdb4b87836a7035779fc`
- Byte count: `5430`
- Use: Evidence classes, ownership selection, naming, oracle quality, deterministic validation boundary, and stop conditions.

#### `.pi/skills/develop-python-test-evidence/references/test-evidence-conventions.md`

- Source: [.pi/skills/develop-python-test-evidence/references/test-evidence-conventions.md](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/.pi/skills/develop-python-test-evidence/references/test-evidence-conventions.md)
- SHA-256: `86ec2f4c392b0c91c1338708ecdcf7fe13c4ab02db62576327ad954abcc59fc8`
- Byte count: `11387`
- Use: Detailed conventions for ownership, helpers, naming, parameterization, layering, exact and approximate acceptance, and evidence claims.

#### `harness/pi/evidence/python-test-evidence-profile-matrix-v1.json`

- Source: [harness/pi/evidence/python-test-evidence-profile-matrix-v1.json](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/harness/pi/evidence/python-test-evidence-profile-matrix-v1.json)
- SHA-256: `085b4380cab81308b1e25672e039c838a872236533641ac415a1bec1253332d6`
- Byte count: `1873`
- Use: Predecessor routine and claim-bearing evidence-field profiles; adapted rather than copied as universal requirements.

#### `python/pyproject.toml`

- Source: [python/pyproject.toml](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/python/pyproject.toml)
- SHA-256: `30f9fd960bb02b475ff620805f3e5d2d7325c57cf110b51a7e2e414d979b01f0`
- Byte count: `2744`
- Use: Pytest strictness, evidence markers, coverage, Ruff, MyPy, and Python 3.14 configuration reference.

#### `harness/pi/docs/evidence-grammar.md`

- Source: [harness/pi/docs/evidence-grammar.md](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/harness/pi/docs/evidence-grammar.md)
- SHA-256: `1db352ccd4f8298a8286eb394907d0d319ca9a5ed95bc04de56c434f15b37c03`
- Byte count: `8453`
- Use: Authority flow, ownership grammar, evidence classes, validator boundaries, and maintained conformance ownership.

#### `python/src/ksdft2effmass/harness/pi/conformance/python/validation.py`

- Source: [python/src/ksdft2effmass/harness/pi/conformance/python/validation.py](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/python/src/ksdft2effmass/harness/pi/conformance/python/validation.py)
- SHA-256: `40be6479238a0ee95a341eb5bc020241c084d1ac41a377dcc076250aa23836e4`
- Byte count: `26617`
- Use: Reusable explicit-input PythonConformanceValidator orchestration, immutable result model, deterministic diagnostics, and claim boundary.

#### `python/src/ksdft2effmass/harness/pi/conformance/python/strict.py`

- Source: [python/src/ksdft2effmass/harness/pi/conformance/python/strict.py](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/python/src/ksdft2effmass/harness/pi/conformance/python/strict.py)
- SHA-256: `468e1ad59972afe22b63fa5a6f9f52e2d577931ef10dd693ac49a3cfe9f6d8f7`
- Byte count: `26529`
- Use: Reusable strict coding-standards adapter, Test-owner checks, helper ownership, typing checks, and resource placement.

#### `python/src/ksdft2effmass/harness/pi/local/evidence_repository_conformance.py`

- Source: [python/src/ksdft2effmass/harness/pi/local/evidence_repository_conformance.py](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/python/src/ksdft2effmass/harness/pi/local/evidence_repository_conformance.py)
- SHA-256: `61dcd86e0555b18c70b388b0831a6381c6249437fdca1cb61ed7391a167525b7`
- Byte count: `3958`
- Use: Repository-local adapter pattern that resolves source authority and invokes the explicit-input validator without making generated inventories authoritative.

#### `python/src/ksdft2effmass/harness/cli/validate_evidence_repository_conformance.py`

- Source: [python/src/ksdft2effmass/harness/cli/validate_evidence_repository_conformance.py](https://github.com/eragasa/ksdft2effmass/blob/7bd913151f7e61ed2bdba593df920be36573b502/python/src/ksdft2effmass/harness/cli/validate_evidence_repository_conformance.py)
- SHA-256: `687b49029f1d24af5263554608e79626647ea2c2165be3e9a684db13092c4fa5`
- Byte count: `3044`
- Use: Thin deterministic JSON CLI and bounded INVALID_INPUT, INTERNAL_ERROR, PASS, and FAIL command outcomes.

## Evidence classes

### software_verification

**Establishes:** The implemented public software contract behaves as specified under the tested conditions.

**Does not establish:** Numerical correctness, scientific adequacy, uncertainty quantification, publication authority, release readiness, or human acceptance.

### numerical_verification

**Establishes:** A numerical implementation agrees with an independently derived mathematical oracle under an explicit criterion.

**Does not establish:** Physical-model adequacy, scientific validation, uncertainty quantification, or human acceptance.

### scientific_validation

**Establishes:** A declared use is adequate against trusted physical, experimental, or scientific reference evidence under a separately authorized protocol.

**Does not establish:** Adequacy outside the declared use or protocol, publication authority, or general human acceptance.

### uncertainty_quantification

**Establishes:** Declared uncertainty sources are characterized or propagated under an explicit uncertainty model or protocol.

**Does not establish:** Scientific adequacy outside that uncertainty model or automatic acceptance of a result.

## Test profiles

### routine

**When:** Maintained software-verification tests whose claims remain bounded to ordinary software behavior and do not carry a numerical, scientific-validation, or uncertainty-quantification claim.

- A static pytest marker links each explicitly admitted test function to one structured declaration record.
- The declaration owns evidence identity, requirement, acceptance, claim boundary, limitations, and provenance metadata without duplicating it in decorators or docstrings.
- Method, oracle, interpretation, and limitations are optional when they add useful information and the represented claim remains routine software verification.
- Evidence identifiers remain stable through authorized renames and migrations.
- Routine evidence remains software verification and cannot be relabeled as a numerical, scientific-validation, uncertainty-quantification, publication, release, or human-acceptance result.

### claim_bearing

**When:** Maintained software or scientific tests that support an explicit numerical-verification, scientific-validation, uncertainty-quantification, or elevated software-contract claim.

- A static pytest marker links each explicitly admitted test function to one structured declaration record.
- The declaration owns evidence identity, requirement, method, oracle, acceptance, interpretation, claim boundary, limitations, and provenance metadata without duplicating it in decorators or docstrings.
- External references require immutable content identity or explicit unresolved status.
- Evidence identifiers remain stable through authorized renames and migrations.
- Deterministic structural validation supplements but does not replace semantic review of the oracle, acceptance criterion, interpretation, limitations, or provenance.

## Module ownership

### class_owned

One public class is the sole primary system under test.

File pattern: `test__ClassName.py or a cohesive test__ClassName__facet.py split.`

### artifact_owned

A schema, fixture family, wire contract, package API, dependency rule, command, or cross-object agreement is primary.

File pattern: `A concise test__artifact_name.py using repository vocabulary.`

### Ownership rules

- Choose exactly one primary owner before naming the module.
- Module-level test functions are the default.
- An optional cohesive Test... wrapper may provide a collection namespace when it improves readability; it is not mandatory evidence metadata or production architecture.
- A Test wrapper has no initializer, mutable instance state, or inheritance-based reuse.
- Do not duplicate assertions across facet modules or use a facet as a dumping ground for collaborators.

## Naming

### Module patterns

- Class-owned: test__ClassName.py.
- Cohesive class-owned split: test__ClassName__facet.py.
- Artifact-owned: test__artifact_name.py.

- Class pattern: Optional Test followed by the class or artifact owner name when a wrapper improves readability.
- Method pattern: `test__surface__facet__behavior, using explicit public behavior and avoiding general, behavior, misc, or opaque numeric names.`
- Special methods: Name equality, hashing, representation, calls, lookup, and other special methods as method facets rather than properties.
- Compatibility: Existing repository tests need not be renamed unless materially changed or separately authorized for migration.

## Test owner rules

- Ordinary lightweight tests remain unmarked and outside formal maintained-evidence admission.
- Each test method establishes one named behavior with relevant assertions.
- Cases are independent and do not rely on execution order or mutable self state.
- A module-level function or optional Test wrapper supplies structural pytest identity; evidence metadata remains in the linked declaration record.
- A test class must not become mandatory ceremony, a production object, or a service container.
- Test methods and private helper methods satisfy the Python code policy's explicit typing, keyword-only parameter, and keyword-spelled call requirements.

## Helper rules

- Test-only setup, assertion, and data builders are small helpers owned by the cohesive module or optional Test wrapper; module helpers are acceptable when clearer than an artificial class.
- Helpers own no independent evidence identifier or pass claim.
- Helpers use visible semantic names, do not hide requirements or tolerances, and do not reproduce the production algorithm.
- Do not create a production DataObjectAction solely to construct test data.

## Fixture rules

- Prefer direct immutable values or maintained immutable resource records.
- Use pytest fixtures only for genuine lifecycle management or materially shared setup.
- Keep conftest.py fixtures narrow and broad or stateful autouse behavior prohibited unless explicitly justified.
- Maintained inputs, ownership records, and compact fixtures live beneath the applicable tests resources directory.
- Runtime scratch uses pytest's isolated temporary path and does not become maintained input.

## Parameterization rules

- Use pytest.param with explicit semantic IDs for meaningful partitions.
- Semantic IDs describe partitions, not ordinals, raw values, paths, generated representations, or opaque abbreviations.
- One parameterized test remains one evidence owner only when every case shares the same requirement, method shape, oracle, acceptance rule, and failure interpretation.
- Split independently meaningful cases when their oracle, acceptance, or interpretation differs.
- Do not replace independently meaningful assertions with broad loops that obscure failing partitions.

## Oracle rules

- Use public contracts, fixed schemas, exact language semantics, independently derived mathematics, higher-precision or independently implemented methods, or approved trusted references.
- Do not use private behavior, production constants as the sole expectation, a reproduction of the production algorithm, or reviewer agreement as the primary oracle.
- Do not mock the system under test; replace only external boundaries when isolation is required.
- Golden bytes or text are valid only when exact representation is itself the contract and the golden source is independently maintained.

## Acceptance rules

- Use exact equality for exact state, canonical bytes, ordering, enums, identities, and exact mathematical zeros.
- Approximate acceptance states the represented quantity, units, dtype or precision, scale, independent expected result, criterion type, threshold and boundary, zero or subnormal handling, and nonfinite behavior where applicable.
- Keep test forward-error bounds distinct from production tolerances and scientific acceptance criteria.
- For package exports, compare the exact expected inventory or directly assert required and prohibited names; do not add a redundant numeric export-count assertion.
- Round-trip success establishes only the round-trip representation contract.

## Layering rules

- Keep schema validation, runtime construction or deserialization, canonical serialization, fixture orchestration, and projection drift checks distinct.
- Use integration tests only for genuine cross-surface contracts and public boundaries.
- A schema pass establishes wire shape, while runtime tests establish semantic and cross-field invariants.
- Evidence, contract, and regression intent remain orthogonal; regression and contract are not evidence classes, and API is a contract surface.
- A passing software test cannot be promoted to numerical verification, scientific validation, uncertainty quantification, or human acceptance.

## Negative-test rules

- Cover malformed syntax, wrong semantic types, Boolean-versus-integer lookalikes, unsupported versions, unknown fields, duplicate members, missing fields, representation limits, and prohibited nonfinite values where applicable.
- Negative runtime-type cases use explicit closed unions and the narrowest call-site type-checker suppression.
- Do not use Any, cast to Any, file-wide suppressions, widened production signatures, skips, or xfail merely to make a negative case possible.

## Stop conditions

- Stop when authority, evidence class, primary owner, public or mathematical requirement, independent oracle, acceptance rule, or separately required scientific protocol is missing or conflicting.
- Do not change expected values, weaken tolerances, add skips, remove tests, renumber evidence identifiers, or alter production behavior merely to obtain a pass.
- Report whether the implementation, fixture, method, contract, reference, or environment is inconsistent instead of repairing evidence silently.

## Minimum validation

```bash
ruff check .
mypy src/python tools tests
pytest
```

### Validation rules

- Run the cheapest affected tests first and broader owner-repository checks afterward.
- Use strict marker and configuration handling when the owner repository declares evidence markers.
- Evidence-bearing tests use static koios_evidence, koios_contract, and koios_regression pytest markers linked to records conforming to projectkoios.arch.python-test-declaration@0.1.0; decorators and docstrings do not duplicate declaration metadata.
- Each intent marker accepts exactly one nonempty literal declaration_id keyword, all intent markers on a test use the same identity, and their set exactly matches the declaration intents.
- Declarations are discovered beneath the explicit tests/declarations root; marker and declaration identities must agree, and every admitted declaration resolves to exactly one collected test function.
- Adapt the pinned PythonConformanceValidator explicit-input architecture and repository adapter rather than implementing an unrelated parallel auditor.
- A deterministic structural validator may establish naming, ownership, metadata, identifier, parameterization, typing, and resource-placement shape only; it cannot establish semantic correctness, oracle independence, tolerance adequacy, scientific validity, or human acceptance.
- Generated Markdown is checked byte-for-byte against the deterministic projection of this JSON source.

## Deferred decisions

- Acceptance of the Draft projectkoios.arch.python-test-declaration contract and schema.
- Extraction of the pinned PythonConformanceValidator mechanics into the appropriate Project Koios owner repository, with Project Koios naming and helper-policy adaptations.
- Migration of unchanged legacy tests into Test owner classes.
- Cross-repository enforcement beyond each owner's maintained commands.
