# `LineChunker` mathematics

## Definitions and domain

Let:

- \(N \in \mathbb{Z}_{\ge 0}\) be the number of lines;
- \(C \in \mathbb{Z}_{>0}\) be `lines_per_chunk`;
- \(O \in \mathbb{Z}\) be `overlap_lines`, with \(0 \le O < C\); and
- \(S = C-O\) be the step, so \(S \ge 1\).

For \(N>0\), let the terminal zero-based chunk index be

<a id="eq-line-chunk-terminal"></a>
```math
\begin{equation}
K = \left\lceil \frac{\max(N-C, 0)}{S} \right\rceil .
\tag{EQ-LINE-CHUNK-TERMINAL}
\end{equation}
```

A chunk is emitted exactly for integer indexes \(0 \le k \le K\). Its one-based
inclusive interval is

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

For \(N=0\), no chunk is emitted. For \(N>0\), the first interval starts at
line 1, every interval contains at most \(C\) lines, and consecutive intervals
share \(O\) lines. The definition of \(K\) selects the first index whose window
reaches line \(N\); no later mathematical window is emitted. Because \(S\ge1\),
starts strictly increase and finite input terminates at \(k=K\).

These equations describe the local implementation; they are not
research-derived and make no scientific model claim.

## Navigation

- [Implementation](../index.md)
- [Class contract](../../index.md)
- [Testing](../testing/index.md)
