# Class `example_package.example_module.ExampleClass`

## Current contract

`ExampleClass.calculate(x)` accepts a finite dimensionless real value and returns
`2x`. It raises `ValueError` for a non-finite input.

## Invariants

- The coefficient is fixed for the lifetime of an instance.
- The method has no external side effects.
- Results are supported only for finite real inputs.

## Navigation

- [Implementation](implementation/index.md)
- [Parent module](../index.md)

## Local mapping

- Code: `src/python/example_package/example_module.py::ExampleClass`
- Test: `tests/test__ExampleClass.py::test__example_class__calculates`

## Evidence

Implementation conformance: the mapped contract test covers a finite input and
the non-finite rejection path. Numerical and scientific evidence are recorded
separately in the implementation detail.
