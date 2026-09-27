# Python test declaration contract

## Contract metadata

| Field | Value |
|---|---|
| Contract ID | `projectkoios.arch.python-test-declaration` |
| Target version | `0.1.0` |
| Status | `Draft` |
| Semantic owner | `ARCH` — Project Koios accepted policy domain |
| Current owner repository | `projectkoios` |
| Acceptance authority | Project Koios human architecture authority |
| Schema identity | `https://projectkoios.com/schemas/arch/python-test-declaration/0.1.0.schema.json` |
| Accepted baseline | None |
| Predecessor | None |
| Supersedes | None |

The schema URL is currently an unpublished identity. Validators resolve it through the pinned mothership catalog without implicit network access.

## Purpose

A Python test declaration records the maintained claim associated with an explicitly admitted test. It keeps evidence classification, contract intent, regression intent, requirements, acceptance, claim boundaries, limitations, and provenance outside executable test bodies.

Ordinary lightweight tests require no declaration. A declaration does not make a test scientifically valid, accepted, authorized, published, released, or suitable for another purpose.

## Authority boundaries

The declaration owns structured metadata for one admitted test subject. It does not own:

- executable setup, operations, or assertions;
- the referenced software, scientific, wire, or baseline contract;
- pytest collection or execution state;
- workflow attempts or authorization;
- human acceptance records;
- baseline replacement decisions; or
- generated inventories and Markdown projections.

Decorators may link a test function to a declaration and state admission intent. They MUST NOT duplicate declaration metadata or convert a declaration into execution authority.

## Static marker linkage

Admitted tests use one or more of these orthogonal static markers:

```python
@pytest.mark.koios_evidence(declaration_id="projectkoios.test.example")
@pytest.mark.koios_contract(declaration_id="projectkoios.test.example")
@pytest.mark.koios_regression(declaration_id="projectkoios.test.example")
def test__represented_behavior() -> None:
    ...
```

Each marker accepts exactly one keyword argument. `declaration_id` is a nonempty string literal; positional arguments, computed values, extra keywords, and `**kwargs` are invalid. All Koios intent markers on one test function identify the same declaration. The marker set must exactly equal the nonempty evidence, contract, and regression intents in that declaration.

Declarations are discovered recursively as regular non-symlinked `*.json` files beneath the owner repository's explicit `tests/declarations/` root. Discovery never imports or executes test modules. Every declaration resolves to exactly one collected module-level test function or method of a top-level `Test...` wrapper. Ordinary tests have no Koios intent marker and require no declaration.

## Subject

Every declaration identifies:

- whether the test is class-owned or artifact-owned;
- its repository-relative test file;
- the source module;
- the represented symbol kind; and
- the represented symbol name.

Module-level test functions remain the default. An optional `Test...` wrapper does not change the declaration subject or become production architecture.

## Orthogonal intents

Evidence, contract, and regression intents are independent:

- evidence classifies what a body of maintained evidence establishes;
- contract identifies provider or consumer obligations at a declared surface; and
- regression identifies a protected dimension and immutable baseline reference.

At least one intent is required. Evidence is not a synonym for contract or regression. Regression is not an evidence class, and API is a contract surface rather than an evidence class.

## Requirement and references

Every declaration contains one structured requirement with a stable identifier, statement, preconditions, and authoritative-reference identifiers.

References are closed records. Repository paths are relative and traversal-free. Resolved references require exact SHA-256 and byte-count identity. Unresolved references carry no invented content identity. URL-shaped identifiers do not authorize network retrieval.

## Method and oracle

Routine declarations may omit method and oracle records when the executable test and exact contract make them unnecessary. Claim-bearing evidence requires:

- setup, operation, and observed outputs;
- a closed oracle kind;
- an independence rationale;
- interpretation; and
- at least one explicit limitation.

An oracle reference or reviewer agreement is not by itself proof of oracle independence.

## Acceptance

Version `0.1.0` supports only closed acceptance kinds:

- exact;
- schema;
- set membership;
- tolerance; and
- performance.

There is no unrestricted custom predicate. Tolerance acceptance requires quantity, units, dtype, scale, criterion, both tolerance values, boundary behavior, zero handling, and nonfinite behavior. Performance acceptance requires an environment reference, warm-up count, sample count, statistic, a percentile value when that statistic is selected, direction, threshold, units, and noise policy.

Duration regression requires the benchmark lane and performance acceptance.

## Claim boundary and limitations

Every declaration states nonempty `establishes` and `does_not_establish` collections. These fields bound the represented claim; they do not authorize promotion into another evidence class.

Limitations have separate identifiers, statements, and consequences. Claim-bearing evidence requires at least one limitation. Routine declarations may have none when the claim boundary is sufficient.

## Validation boundary

Draft 2020-12 schema validation establishes closed wire shape and represented conditional requirements only. A semantic validator remains responsible for:

- unique declaration, evidence, regression, requirement, and limitation identities across the admitted repository scope;
- unique reference identities within each declaration;
- reference-ID closure within each declaration;
- marker/declaration agreement;
- test-function placement;
- baseline and contract identity resolution;
- schema-catalog identity verification; and
- provenance and privacy policy.

Contract identities may recur because multiple tests can provide or consume the same versioned contract. Their version, surface, role, and authoritative references remain explicit in each declaration.

Neither schema nor semantic validation establishes oracle quality, tolerance adequacy, scientific validity, human acceptance, or authorization.

## Compatibility

This is a Draft `0.1.0` contract with no accepted baseline. Consumers MUST NOT claim compatibility until the schema, semantic rules, marker linkage, and conformance vectors receive separate review and human acceptance.
