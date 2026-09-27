# `ExampleClass` mathematics

## Model

For finite dimensionless real input \(x\), the output \(y\) is

<a id="eq-example-linear"></a>
```math
\begin{equation}
y = 2x
\tag{EQ-EXAMPLE-LINEAR}
\end{equation}
```

| Symbol | Meaning | Unit | Domain |
| --- | --- | --- | --- |
| \(x\) | input | dimensionless | finite real numbers |
| \(y\) | output | dimensionless | finite real numbers |

## Assumptions and validity

The fixed coefficient is valid only for this illustrative model. No extrapolation
to measured physical systems is claimed.

## Evidence

- **Implementation conformance — supported:** the mapped method implements the
  equation directly.
- **Numerical verification — supported:** exact comparison against `2 * x` on
  CPython for finite fixture inputs, tolerance `0.0`.
- **Scientific validation — not evaluated:** no reference dataset or physical
  model is claimed by this illustrative calculation.
- **Human acceptance — not evaluated:** no accepting authority has approved the
  model for operational use.

## Navigation

- [Implementation](../index.md)
- [Class contract](../../index.md)
- [Research references](../references/index.md)
- [Testing detail](../testing/index.md)
