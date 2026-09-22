# Public Project Koios records

`project-catalog.json` is the product-owned source for project summaries explicitly
approved for public presentation. `course-catalog.json` is the public-safe inventory of
identified course identities and their material-review status. The browser does not
infer either catalog from private repositories, tasks, notes, workflows, or runtime
state.

The `projectkoios-api` public-project catalog contract validates the document before
serving it. A configured missing, malformed, duplicate, or contract-invalid catalog
prevents API startup. The web interface consumes only that API projection.

A project record is an editorial overview. Capability statuses must distinguish
`available`, `in-development`, and `planned` work. Limitations remain visible. A record
does not grant release, publication, scientific-validation, or architecture authority
to an independent repository.

A course record publishes identity and migration status only. `inventory-only` means
that a source collection is known but has not reached a public-material review gate.
`review-candidate` means default-deny sanitization has produced a candidate for manual
review; it does not authorize publication. No course materials are currently marked
`published`.

Changes to this directory require human review in the `projectkoios` repository. The
initial catalog contains Project Koios itself; independent scientific applications
retain their own public claims and release lifecycles.
