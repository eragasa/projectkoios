# Public Project Koios records

`project-catalog.json` is the product-owned source for project summaries explicitly
approved for public presentation. The browser does not infer this content from private
repositories, tasks, notes, workflows, or runtime state.

The `projectkoios-api` public-project catalog contract validates the document before
serving it. A configured missing, malformed, duplicate, or contract-invalid catalog
prevents API startup. The web interface consumes only that API projection.

A project record is an editorial overview. Capability statuses must distinguish
`available`, `in-development`, and `planned` work. Limitations remain visible. A record
does not grant release, publication, scientific-validation, or architecture authority
to an independent repository.

Changes to this directory require human review in the `projectkoios` repository. The
initial catalog contains Project Koios itself; independent scientific applications
retain their own public claims and release lifecycles.
