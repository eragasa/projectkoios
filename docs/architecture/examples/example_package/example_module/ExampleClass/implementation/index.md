# `ExampleClass` implementation

## Current implementation

`calculate` validates finiteness, multiplies the input by `COEFFICIENT`, and
returns the resulting float. It performs no I/O.

## Data flow

1. Receive `x`.
2. Reject a non-finite value.
3. Compute `COEFFICIENT * x`.
4. Return the result.

## Navigation

- [Mathematics](mathematics/index.md)
- [References](references/index.md)
- [Testing](testing/index.md)
- [Class contract](../index.md)

## Local mapping

- Code: `src/python/example_package/example_module.py::ExampleClass.calculate`
- Test: `tests/test__ExampleClass.py::test__example_class__calculates`

## Evidence boundary

The implementation test establishes code conformance only. Numerical,
scientific, and human evidence retain independent statements.
