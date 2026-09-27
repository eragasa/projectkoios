# Module `example_package.example_module`

## Current responsibility

The module defines the coefficient and `ExampleClass` calculation contract.

## Public contract

`COEFFICIENT` is `2.0`. `ExampleClass.calculate(x)` returns the modeled output
for an input in the documented validity domain.

## Navigation

- [Class `ExampleClass`](ExampleClass/index.md)
- [Parent package](../index.md)

## Local mapping

- Code: `src/python/example_package/example_module.py`
- Test: `tests/test__ExampleClass.py::test__example_class__calculates`

## Evidence

Implementation conformance: the mapped test checks the constant and method
result using an exact fixture.
