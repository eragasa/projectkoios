# Project Koios application architecture

## Purpose

A Project Koios application is the workflow/colored-Petri-net-enabled
composition layer that stitches reusable capabilities into a scientific
operation. Application architecture keeps scientific policy and cross-capability
composition out of reusable simulation and workflow packages.

## Ownership

The `projectkoios-applications` repository owns the
`projectkoios.applications` namespace and these application-scoped concerns:

- cross-capability composition;
- scientific policy, recipes, and configuration;
- workflow definitions and facades;
- colored-Petri-net (CPN) composition;
- runners and application replay;
- campaigns; and
- application evidence and outcomes.

Application capabilities are packages under this shared owner rather than
repositories by default. `pw_dft_scf` is
`projectkoios.applications.pw_dft_scf`; it is not a standalone application or
repository. Additional application capabilities share
`projectkoios-applications` unless a materially independent ownership boundary
is documented in current architecture.

The incubated source path mirrors the intended package as
`projectkoios.frankensteins.applications.pw_dft_scf`. A reviewed transfer to the
application owner removes only the `frankensteins` segment. Incubation does not
make transfer automatic; the current disposition of the remaining overlay is
recorded in the [Frankenstein architecture](architecture.frankenstein.md).

## Reusable capability boundaries

| Owner | Responsibility |
|---|---|
| `projectkoios-simulations` | Neutral simulation abstractions and provider integrations, without application recipes, campaigns, or scientific outcome policy. |
| `projectkoios-workflow` | Generic workflow runtime, state, engine, replay primitives, and CPN contracts, without application scientific semantics. |
| `projectkoios-applications` | Composition and policy that specialize reusable capabilities into applications. |

A simulation integration owns neutral interaction with its provider. An
application owns the selection and composition of those integrations, the
scientific recipe applied to them, and the interpretation of their results in
an application workflow.

The workflow owner supplies engine-neutral state and runtime behavior, generic
engine contracts, CPN contracts, and reusable replay mechanics. An application
supplies its workflow definitions and facade, composes its CPN model, and owns
application-level execution and replay policy. Application definitions do not
become generic workflow contracts merely because the workflow runtime executes
them.

## Dependency direction

Dependencies point from applications to reusable components:

```text
projectkoios.applications
    -> projectkoios.simulations and provider integrations
    -> projectkoios.workflow
    -> other reusable capabilities
```

Reusable components must not import `projectkoios.applications` or an
application capability package. Behavior needed by a reusable component must be
expressed through a neutral contract owned outside the application layer.

Application evidence may refer to provider artifacts and generic workflow
records without taking ownership of the reusable implementations that produced
or tracked them. Provider artifacts, workflow state, and application outcomes
remain distinguishable evidence types.

## Scientific authority

A successful provider call, completed workflow, CPN firing, replay match, or
application run does not by itself establish scientific acceptance. Application
policy identifies required checks and evidence, while an explicit human or
separately declared domain authority accepts scientific claims. Independently
governed projects such as `ksdft2effmass` and `dacp2transport` retain their own
scientific, migration, release, and source authority.
