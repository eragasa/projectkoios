# `ExampleClass` references

## Worked API provenance

The local input check is informed by Python's documented finiteness predicate.
The locally chosen \(y=2x\) equation is illustrative original work and is not
derived from this or any other research source.

| Claim | Source | Version | Locator | License | Role | Basis | Deviation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `CLAIM-FINITE-INPUT-CHECK` | Python `math.isfinite` documentation | Python 3.14 documentation | `https://docs.python.org/3.14/library/math.html#math.isfinite` | PSF License Version 2 | API basis | documents the predicate as true exactly when neither infinite nor NaN | the example method raises `ValueError` instead of returning a Boolean |

## Interpretation

The exact API anchor is the locator. The row supports only the finiteness-check
behavior; it provides no scientific validation for the local equation.

## Navigation

- [Implementation](../index.md)
- [Class contract](../../index.md)
- [Mathematics](../mathematics/index.md)
