# `LineChunker` mathematics

## Definitions and domain

Let:

- \(N \in \mathbb{Z}_{\ge 0}\) be the number of lines;
- \(C \in \mathbb{Z}_{>0}\) be `lines_per_chunk`;
- \(O \in \mathbb{Z}\) be `overlap_lines`, with \(0 \le O < C\); and
- \(S = C-O\) be the step, so \(S \ge 1\).

For zero-based chunk index \(k \in \mathbb{Z}_{\ge 0}\), a chunk exists when
\(kS < N\). Its one-based inclusive interval is

<a id="eq-line-chunk-start"></a>
```math
\begin{equation}
\operatorname{start}(k) = kS + 1
\tag{EQ-LINE-CHUNK-START}
\end{equation}
```

<a id="eq-line-chunk-end"></a>
```math
\begin{equation}
\operatorname{end}(k) = \min(kS + C, N)
\tag{EQ-LINE-CHUNK-END}
\end{equation}
```

## Consequences

For \(N=0\), no chunk index satisfies the existence condition. For \(N>0\), the
first interval starts at line 1, every interval contains at most \(C\) lines,
and consecutive intervals share \(O\) lines. Because \(S\ge1\), starts strictly
increase and finite input terminates. Emission stops at the first interval with
\(\operatorname{end}(k)=N\).

These equations describe the local implementation; they are not
research-derived and make no scientific model claim.

## Navigation

- [Implementation](../index.md)
- [Class contract](../../index.md)
- [Testing](../testing/index.md)
