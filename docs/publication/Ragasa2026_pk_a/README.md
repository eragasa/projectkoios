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
- PDF pages: 12 (Ghostscript `10.04.0` page-count inspection)
- PDF size: 372,406 bytes
- PDF SHA-256:
  `e8ea37979706a72caed7c34ce475c9e3e655d60c50a68dc5773a8ba19f2fa8e1`
- Clean-build comparison: two consecutive clean builds produced the same PDF
  SHA-256 and byte count.

The preserved first-pass package is commit
`6db177ce8af369039fbaccd25f9dcde53033e2e7`. This related-work revision
supersedes the publication files from that checkpoint. Its publication-input
SHA-256 identities are:

```text
8e3264d7d61778267bf448529623e5bfbe30081b2de146af5626cc9ffc793462  Ragasa2026_pk_a.tex
bd83b273d0681f09afdfe7f825f9811edf5e33f838dc6b05d71d170be0bc511d  references.bib
ac4fb7b2279f3aaf54bd1fab64c5bd7502a270bb580b1d32c3264750c66d78d6  Makefile
b284382198a77bfcbcc107f4920fc799e419ea78a5b93c3a775eba7868706a6f  figures/audit-first-workflow.tex
2eb9b912d9eca525865b1a743752f11d9f8bdf13b4f25fbba9dfa46a0a8f3100  figures/evidence-authority-separation.tex
```

The scientific and methodological source identity remains the reviewed report
and ledger at commit `45da16e6428c3c431359da4f80f46de7ebf71081`.

## Related-work metadata provenance

The related-work revision admits 12 author/editor-authorized entries after a
References verification dated 2026-10-23. The received canonical 12-entry
BibTeX block was 5,745 bytes with SHA-256
`5d6fbff3c70c292139d5c6795ad5b437059178c594e1d6d8a2faf01595b2b4c1`.
The merged bibliography preserves the verified identities and ten DOI values.
For plainnat/BibTeX rendering, it adds an editor-labelled sort key to the
PROV-DM record, repeats the two accepted access dates in rendered note text, and
repeats the NIST DOI in rendered note text because the style otherwise drops
those fields. The canonical parrot glyph in the Bender et al. title remains in
`references.bib`; the pdfTeX source explicitly renders that unsupported glyph as
`[parrot]`. These render accommodations are not identity changes.

The external sources contextualize established practice; they are not evidence
that a Project Koios case implemented a cited practice. The 2026-10-23 metadata,
correction, retraction, and errata checks are point-in-time checks and must be
repeated immediately before any separately authorized submission.

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
