# `ExampleClass` testing

## Strategy

Tests keep distinct questions distinct. A passing implementation test is not
reported as scientific validation or human acceptance.

| Evidence kind | Current result |
| --- | --- |
| Implementation conformance | Supported: contract fixtures exercise calculation and rejection behavior. |
| Numerical verification | Supported: exact comparator `2 * x`, tolerance `0.0`, CPython, finite fixture domain. |
| Scientific validation | Not evaluated: no scientific dataset or physical claim is in scope. |
| Human acceptance | Not evaluated: no accepting authority has approved operational use. |

## Local mapping

- `tests/test__ExampleClass.py::test__example_class__calculates`
- `tests/test__ExampleClass.py::test__example_class__rejects_non_finite`

## Limitations

The fixtures do not establish behavior outside finite real inputs and do not
establish scientific fitness.

## Navigation

- [Implementation](../index.md)
- [Class contract](../../index.md)
- [Mathematics](../mathematics/index.md)
