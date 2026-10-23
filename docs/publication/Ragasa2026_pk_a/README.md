# Ragasa2026_pk_a publication source

## Purpose and status

This directory contains the bounded LaTeX source for the Draft preprint
**“Project Koios: An audit-first, LLM-assisted workflow for verifiable
computational physics.”** It adapts the reviewed technical methodology and
experience report into an article-shaped source; it is not a second evidence
ledger or a publication-status system.

The canonical reviewed source basis is Project Koios commit
`45da16e6428c3c431359da4f80f46de7ebf71081`:

- `docs/reports/project-koios-audit-first-methodology.md` — reviewed narrative;
- `docs/reports/project-koios-audit-first-methodology-evidence.json` — bounded
  machine-readable claim/evidence ledger; and
- `docs/reports/project-koios-audit-first-methodology-plan.md` — evidence and
  release plan.

The manuscript remains a Draft preprint source. It is not peer reviewed,
submitted, accepted, released, or assigned a DOI. The provisional author name
is Eugene Joseph M. Ragasa; affiliation, correspondence, contributor roles, and
final authorship metadata require explicit human confirmation before submission
or release.

## Files

- `Ragasa2026_pk_a.tex` — canonical manuscript source;
- `Ragasa2026_pk_a.pdf` — retained rendered Draft;
- `references.bib` — only references cited by the manuscript;
- `figures/audit-first-workflow.tex` — claim-admission workflow figure source;
- `figures/evidence-authority-separation.tex` — evidence/authority separation
  figure source;
- `Makefile` — local build entry; and
- `.gitignore` — publication-local auxiliary-output exclusion.

## Build

A TeX Live installation with `latexmk`, `pdflatex`, BibTeX, and TikZ is
sufficient. From this directory run:

```bash
make
```

The build writes auxiliary and intermediate files under `.build/`, then copies
the retained rendered Draft to:

```text
Ragasa2026_pk_a.pdf
```

Remove both intermediate output and the rendered PDF with `make clean`; recreate
them with `make`. The build must not install dependencies or fetch network
resources. `.build/` is ignored locally, while the PDF is intentionally retained
beside the source. Retention does not authorize release or publication.

## Render record

- Build command: `make clean && make`
- Renderer: pdfTeX `3.141592653-2.6-1.40.27` (TeX Live 2025)
- Driver: latexmk `4.86a`
- Bibliography processor: BibTeX `0.99d` (TeX Live 2025)
- Deterministic build epoch: `SOURCE_DATE_EPOCH=1792674722`, `TZ=UTC`,
  `FORCE_SOURCE_DATE=1`
- PDF pages: 9 (Ghostscript `10.04.0` page-count inspection)
- PDF size: 350,385 bytes
- PDF SHA-256:
  `f904717b1fae76e6b1720030896e441bc57def276b937d1d9320e2224bf9dd8c`
- Clean-build comparison: two consecutive clean builds produced the same PDF
  SHA-256 and byte count.

Publication inputs remain local and uncommitted in this first pass. Their
SHA-256 identities are:

```text
b5113d142bedbc851f40e691d1e75f90101e8f3df0d6b8f525a375271887f1aa  Ragasa2026_pk_a.tex
b2193fc4d3ecc57e59fedef5a63ec52b20533dc4f4a9721d59d132e3675693da  references.bib
ac4fb7b2279f3aaf54bd1fab64c5bd7502a270bb580b1d32c3264750c66d78d6  Makefile
b284382198a77bfcbcc107f4920fc799e419ea78a5b93c3a775eba7868706a6f  figures/audit-first-workflow.tex
2eb9b912d9eca525865b1a743752f11d9f8bdf13b4f25fbba9dfa46a0a8f3100  figures/evidence-authority-separation.tex
```

The scientific and methodological source identity remains the reviewed report
and ledger at commit `45da16e6428c3c431359da4f80f46de7ebf71081`.

## Evidence and nonclaims

The JSON ledger at the canonical reviewed commit remains the supporting evidence
record. The article summarizes selected claims for readability and does not
replace, flatten, or extend that ledger.

This source does not establish:

- peer review, submission, publication acceptance, or release;
- experimental or material validation;
- a productivity, quality, cost, or time-to-result benefit from LLM assistance;
- universal LLM compliance with prompts, policy, or scientific norms;
- that source-level test definitions are retained executed results;
- that a Lean theorem proves runtime behavior, source fidelity, or physical
  applicability; or
- authorization for a push, pull request, merge, tag, release, deposit, DOI,
  arXiv submission, or publication.

Any future public artifact requires separate authorship, rights, privacy,
technical, editorial, and release decisions. Repository licenses and linked
notice files do not by themselves clear every manuscript or deposit input.
