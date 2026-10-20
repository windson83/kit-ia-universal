# FrontMD Stack Selection Matrix

This reference prevents dependency sprawl. Choose the least complex option that meets the interaction and design requirements.

## 1. Framework

| Situation | Preferred approach |
|---|---|
| Existing healthy Next.js app | Keep Next.js; respect current routing/rendering model |
| Existing healthy Vite React app | Keep Vite; do not migrate for aesthetics |
| New marketing/full-stack React product needing SSR/SEO | Consider Next.js |
| New internal SPA with separate backend | Consider Vite React |
| Non-React project | Preserve its framework unless migration is explicitly in scope |

FrontMD is React-optimized, but design principles are framework-agnostic.

## 2. Styling

### Tailwind CSS

Use when:

- project already uses it
- rapid design-system iteration matters
- semantic CSS variables/tokens are enforced
- component code is owned locally

Avoid turning Tailwind into arbitrary utility soup. Establish tokens and component variants.

### CSS Modules / vanilla CSS

Use when:

- already established in the codebase
- component scoping is more valuable than utility composition
- the design includes bespoke layout/animation where direct CSS is clearer

Do not introduce Tailwind solely because FrontMD mentions it.

## 3. Primitive/component base

### shadcn/ui

Best fit when:

- you want component source in-repo
- deep visual customization matters
- a design system will evolve with the product
- AI agents need to inspect/modify component internals

For new projects, select one component base deliberately.

### Base UI

Choose when:

- building a fresh general-purpose React system
- accessible headless behavior is needed
- you want styling ownership
- shadcn's current Base UI path covers required components

### React Aria

Choose when:

- enterprise accessibility is central
- complex selection, keyboard, internationalization, or multiple interaction modalities matter
- building reusable design-system components

### Radix Primitives

Choose when:

- already used in the repository
- migration cost outweighs benefits
- a required primitive/integration is mature in the existing Radix ecosystem

### Rule

Do not use Base UI Select, Radix Select, and React Aria Select in the same design system without a documented migration reason.

## 4. Enhanced component sources

### Animate UI

Good for:

- animated accordions/tabs/menus
- interaction polish
- components that should remain source-owned

Use when animation adds state clarity. Remove unnecessary animation.

### Aceternity UI

Good for:

- high-impact landing page moments
- hero interactions
- distinctive backgrounds/visual modules
- a limited number of signature components

Risk:

- overuse quickly becomes spectacle and hurts uniqueness
- WebGL/canvas/continuous effects can create performance/accessibility cost

Policy: generally limit to one or a few signature moments per experience.

### Kibo UI

Good for:

- richer functional components compatible with a shadcn-oriented stack
- file dropzones, advanced inputs, higher-level app UI, AI UI primitives

### 21st.dev

Use as:

- discovery catalogue
- visual inspiration
- source for candidate components

Before adopting a component, inspect:

- dependencies
- accessibility
- responsiveness
- visual consistency
- maintenance quality
- whether it duplicates existing code

## 5. Data display

### TanStack Table

Use for data-heavy screens needing combinations of:

- sorting
- filtering
- selection
- pagination
- column visibility
- large data
- custom cell rendering

Because it is headless, preserve complete visual ownership.

Use native/simple `<table>` for small static tabular data. Do not add TanStack Table for a three-row table.

## 6. Motion

### CSS

First choice for:

- hover
- focus
- color
- opacity
- small transform
- simple keyframes

### Motion for React

Use for:

- enter/exit presence
- layout animation
- gestures
- shared-layout transitions
- complex state-driven motion
- scroll-linked animation

### GSAP

Consider only when:

- complex timeline choreography is a core requirement
- SVG/scroll/specialized animation exceeds the current stack

Do not add GSAP and Motion together by default.

## 7. Icons

### Lucide

Neutral, interface-oriented, consistent stroke system. Good default for admin/enterprise/product UI.

### Phosphor

Wider stylistic range and weights. Useful when the brand calls for more personality.

Rule: one icon family for ordinary UI controls.

## 8. Forms

Prefer the project's existing form architecture.

For complex React forms, a common robust combination is:

- React Hook Form for field state and performance
- Zod or the project's schema validator for typed validation

But native controlled inputs are sufficient for small forms.

## 9. Charts

Do not choose a chart library first. Choose the analytical question first.

Use the project's existing chart library if competent.

Rules:

- labels and units are explicit
- legend is useful, not ornamental
- color encodes meaning consistently
- chart has accessible textual context
- avoid 3D charts
- avoid decorative charts with no decision value

## 10. Theming

Prefer semantic CSS variables.

For light/dark modes:

- tokens must be authored for each mode
- don't simply invert colors
- verify border/surface hierarchy in both modes
- charts and data colors need mode-aware contrast

## 11. Component-source policy

Priority order:

1. existing component that can be adapted cleanly
2. existing primitive + custom styling
3. shadcn/open-code component
4. audited third-party source component
5. new bespoke component
6. new runtime dependency only when needed

This ordering keeps the UI coherent and the dependency graph under control.
