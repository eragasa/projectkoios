# Atomic Notes in Project Koios

Atomic notes are small, reusable knowledge objects. Each atomic note should capture one stable concept, definition, theorem, model, operator, equation, quantity, method, algorithm, example, or exercise.

An atomic note is not a lecture. A lecture is a pedagogical sequence. An atomic note is a reusable unit of knowledge.

The purpose of atomic notes in Project Koios is to support a technical workflow where physics, mathematics, computation, and implementation remain connected.

A good atomic note should answer:
- What is the object?
- What does it mean?
- What is its mathematical form?
- What is its physical interpretation?
- How is it represented computationally?
- What other notes depend on it?

## Core rule

One atomic note equals one reusable concept.

A lecture may contain many atomic notes.  
A textbook section may develop many atomic notes.  
An exercise may apply several atomic notes.  
A computational notebook may implement several atomic notes.

The distinction is:

```text
atomic note      → one concept
lecture          → one teaching sequence
textbook section → one developed exposition
exercise note    → one problem and solution
notebook         → one executable investigation
```

## Common atomic-note spine

All atomic notes should share a minimal common structure.

```md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Core idea

## Definition / Statement

## Interpretation

## Minimal example

## Representations

## Common confusions

## Links
```

This spine should remain stable across mathematics, physics, materials science, and computation.

However, the detailed structure should depend on the epistemic role of the note.

## Template families

Project Koios should use functional templates rather than discipline-specific templates.

Instead of:

```text
math.atomic.md
physics.atomic.md
chemistry.atomic.md
materials.atomic.md
```

use:

```text
atomic.definition.md
atomic.theorem.md
atomic.model.md
atomic.operator.md
atomic.equation.md
atomic.quantity.md
atomic.method.md
atomic.algorithm.md
atomic.example.md
atomic.exercise.md
```

The note type should follow the role of the object, not the academic department.

For example:

|Object|Template|
|---|---|
|vector|definition|
|basis|definition|
|coordinate system|definition|
|Bloch theorem|theorem|
|divergence theorem|theorem|
|free electron model|model|
|Drude model|model|
|Hamiltonian operator|operator|
|Laplacian operator|operator|
|Schrödinger equation|equation|
|diffusion equation|equation|
|entropy|quantity|
|chemical potential|quantity|
|density of states|quantity|
|finite difference method|method|
|FFT|algorithm|
|particle in a box calculation|example|
|vector-space proof problem|exercise|

## Template: Definition Note

Use for concepts such as vector, basis, coordinate system, Hilbert space, phase space, ensemble, entropy, chemical potential, and unit vector.

```md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
note_kind: definition
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Core idea

One sentence stating the concept.

## Definition

State the definition precisely.

$$

$$

where

- $ $ =
- $ $ =
- $ $ =

$\blacksquare$

## Interpretation

Explain what the definition means physically, geometrically, mathematically, or computationally.

## Minimal example

Give the smallest nontrivial example.

$$

$$

## Non-examples / common confusions

- 
- 
- 

## Links

### Prerequisites

- [[ ]]

### Used by

- [[ ]]

### Related

- [[ ]]
```

## Template: Theorem / Proposition Note

Use for results such as Bloch theorem, divergence theorem, spectral theorem, equipartition theorem, Noether theorem, or a convergence result.

```md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
note_kind: theorem
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Core idea

One sentence stating what the theorem gives you.

## Statement

State the theorem precisely.

$$

$$

## Assumptions

- 
- 
- 

## Meaning

Explain what the theorem says in ordinary technical language.

## Proof sketch

Only include the essential steps.

1. 
2. 
3. 

## Minimal example

Show the theorem acting on a concrete object.

$$

$$

## Used by

- [[ ]]

## Related

- [[ ]]
```

## Template: Physical Model Note

Use for models such as the free electron model, Drude model, harmonic oscillator, particle in a box, ideal gas, regular solution model, and tight-binding model.

````md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
note_kind: model
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Core idea

State what physical system is being idealized.

## State space

Define the state variables or admissible states.

$$

$$

where

- $ $ =
- $ $ =

## Assumptions

- 
- 
- 

## Governing equation / operator

$$

$$

## Boundary conditions / constraints

$$

$$

## Observables

- 
- 
- 

## Minimal computational representation

```python

````

## Limits of the model

## Links

### Prerequisites

- [[ ]]
    

### Used by

- [[ ]]
    

### Related

- [[ ]]
    

````

## Template: Operator Note

Use for derivative operators, Laplacians, Hamiltonians, momentum operators, projection operators, translation operators, and finite-difference matrices.

```md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
note_kind: operator
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Core idea

State what transformation the operator performs.

## Definition

$$
\hat{A}: \mathcal{V} \to \mathcal{W}
$$

where

- $\hat{A}$ =
- $\mathcal{V}$ =
- $\mathcal{W}$ =

## Domain and codomain

- Domain:
- Codomain:
- Required smoothness / admissible states:

## Action on a state

$$
\hat{A} f =
$$

## Matrix representation

Given a basis $\{\phi_i\}$,

$$
A_{ij}
=
\langle \phi_i | \hat{A} | \phi_j \rangle
$$

## Numerical discretization

$$

$$

## Boundary conditions

Explain whether the operator depends on boundary conditions.

## Common confusions

- Operator versus matrix representation.
- Continuous operator versus discrete operator.
- Physical observable versus generator.
- Abstract operator versus implementation object.

## Links

### Prerequisites

- [[ ]]

### Used by

- [[ ]]

### Related

- [[ ]]
````

## Template: Equation Note

Use for equations such as the Schrödinger equation, diffusion equation, heat equation, Clausius-Clapeyron equation, ideal gas law, and continuity equation.

```md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
note_kind: equation
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Core idea

State what balance law, constraint, constitutive relation, or dynamical law this equation represents.

## Equation

$$

$$

## Symbols

- $ $ =
- $ $ =
- $ $ =

## Meaning

Explain what the equation says physically or mathematically.

## Assumptions

- 
- 
- 

## Derived from

- [[ ]]

## Solves for

- 
- 

## Limiting cases

- 
- 

## Computational form

$$

$$

## Links

### Prerequisites

- [[ ]]

### Used by

- [[ ]]

### Related

- [[ ]]
```

## Template: Quantity Note

Use for quantities such as entropy, free energy, chemical potential, density of states, effective mass, conductivity, mobility, heat capacity, and work function.

```md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
note_kind: quantity
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Core idea

State what the quantity measures.

## Definition

$$

$$

where

- $ $ =
- $ $ =

## Units

$$

$$

## Physical interpretation

Explain what a large value, small value, zero value, or sign change means.

## How it is measured or computed

## Related quantities

- [[ ]]
- [[ ]]

## Common confusions

- 
- 
- 

## Links

### Prerequisites

- [[ ]]

### Used by

- [[ ]]

### Related

- [[ ]]
```

## Template: Computational Method Note

Use for finite difference methods, finite element methods, eigenvalue solvers, FFTs, Monte Carlo methods, molecular dynamics, and numerical integration schemes.

````md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
note_kind: method
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Core idea

State what problem this method solves.

## Continuous problem

$$

$$

## Discretized state

$$
\mathbf{u}
=
\begin{bmatrix}
u_1 & u_2 & \cdots & u_N
\end{bmatrix}^{\mathsf T}
$$

## Discrete operator / update rule

$$

$$

## Boundary conditions

State how boundary conditions enter the numerical representation.

## Algorithm

1. 
2. 
3. 

## Minimal code

```python

````

## Numerical issues

- stability
    
- convergence
    
- conditioning
    
- grid resolution
    
- boundary artifacts
    

## Links

### Prerequisites

- [[ ]]
    

### Used by

- [[ ]]
    

### Related

- [[ ]]
    

````

## Template: Algorithm Note

Use for procedures with a definite input-output structure, such as FFT, Lanczos iteration, QR decomposition, bisection, Newton iteration, Metropolis sampling, or relaxation schemes.

```md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
note_kind: algorithm
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Core idea

State what the algorithm computes.

## Input

- 
- 

## Output

- 
- 

## Mathematical problem

$$

$$

## Algorithm

1. 
2. 
3. 

## Minimal implementation

```python

````

## Complexity

- Time:
    
- Memory:
    

## Numerical issues

## Links

### Prerequisites

- [[ ]]
    

### Used by

- [[ ]]
    

### Related

- [[ ]]
    

````

## Template: Example Note

Use for short worked examples that instantiate a definition, theorem, model, equation, or method.

```md
---
title:
aliases: []
tags: []
status: draft
type: atomic-note
note_kind: example
domain:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Purpose

State what this example demonstrates.

## Given

- 
- 
- 

## Relevant notes

- [[ ]]
- [[ ]]

## Setup

$$

$$

## Calculation

$$

$$

## Result

$$

$$

## Interpretation

Explain what the result means.

## Extensions

- 
- 
- 
````

## Template: Exercise Note

Use for exercises, homework problems, derivation prompts, proof prompts, and computational tasks.

```md
---
title:
aliases: []
tags: []
status: draft
type: exercise-note
note_kind: exercise
domain:
difficulty:
created:
updated:
---

# {{title}}

back to: [[ ]]

## Problem

State the problem clearly.

## Given

- 
- 
- 

## Find

- 
- 

## Relevant notes

- [[ ]]
- [[ ]]

## Solution outline

1. 
2. 
3. 

## Full solution

$$

$$

## Final result

$$

$$

## Checks

- Units:
- Limiting case:
- Sign convention:
- Numerical check:

## Related exercises

- [[ ]]
```

## Recommended note taxonomy

Use `type` for the broad object class and `note_kind` for the functional role.

Examples:

```yaml
type: atomic-note
note_kind: definition
```

```yaml
type: atomic-note
note_kind: model
```

```yaml
type: atomic-note
note_kind: operator
```

```yaml
type: exercise-note
note_kind: exercise
```

Useful `note_kind` values:

```text
definition
theorem
model
operator
equation
quantity
method
algorithm
example
exercise
```

Useful `domain` values:

```text
math.linear-algebra
math.calculus
math.differential-equations
physics.mechanics
physics.quantum
physics.statistical-mechanics
physics.electromagnetism
materials.thermodynamics
materials.phase-diagrams
materials.kinetics
computation.numerics
computation.software
```

## Naming convention

Use stable, dotted names when the note belongs to the knowledge system.

Examples:

```text
math.linearalgebra.vector.md
math.linearalgebra.basis.md
math.linearalgebra.displacement.md
math.linearalgebra.coordinatesystem.md

physics.quantum.hamiltonian.md
physics.quantum.schrodinger-equation.time-independent.md
physics.quantum.particle-in-a-box.1d.md

physics.solidstate.bloch-theorem.md
physics.solidstate.density-of-states.md
physics.solidstate.free-electron-model.md

materials.thermodynamics.chemical-potential.md
materials.thermodynamics.regular-solution-model.md
materials.phase-diagrams.lever-rule.md

computation.numerics.finite-difference-method.md
computation.numerics.laplacian.1d.dirichlet.md
```

## Lecture versus atomic note

A lecture should contain a sequence.

Example:

```text
point
→ coordinate choice
→ displacement
→ vector
→ vector space
→ basis
→ components
→ magnitude and direction
```

That is a lecture arc.

The corresponding atomic notes would be:

```text
point
coordinate
displacement
vector
vector space
basis
coordinate representation
magnitude
direction
```

The lecture links these concepts together.  
The atomic notes define them individually.

## Design principle

The template should follow the epistemic role of the note, not the academic department.

The same operator template can describe:

```text
Laplacian operator
Hamiltonian operator
translation operator
finite-difference Laplacian matrix
stress tensor as a linear map
```

The same model template can describe:

```text
ideal gas model
free electron model
regular solution model
Drude model
particle in a box
tight-binding model
```

The same quantity template can describe:

```text
entropy
chemical potential
density of states
effective mass
mobility
heat capacity
```

This keeps Project Koios coherent across physics, materials science, computation, and pedagogy.

## Practical rule

When creating a new note, first ask:

```text
What kind of knowledge object is this?
```

Then choose the template:

```text
Is it a concept?       → definition
Is it a result?        → theorem
Is it an idealization? → model
Is it a mapping?       → operator
Is it a relation?      → equation
Is it measured?        → quantity
Is it a procedure?     → method or algorithm
Is it a demonstration? → example
Is it a task?          → exercise
```

Only after that assign the domain.

This prevents the knowledge base from becoming a pile of department-specific notes and instead makes it a reusable technical system.