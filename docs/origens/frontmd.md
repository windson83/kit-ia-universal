# Fonte histórica — não é instrução operacional

Origem: `frontmd-skill-v1.0.0.zip!/frontmd/SKILL.md`

---
name: frontmd
description: Design and implement distinctive, production-grade React frontends that avoid generic AI-generated aesthetics. Use when creating, redesigning, auditing, or polishing web interfaces, dashboards, SaaS apps, landing pages, portals, admin panels, navigation systems, forms, or design systems where visual quality, responsive UX, accessibility, performance, and maintainable component architecture matter.
license: MIT
compatibility: Works with Claude Code, Codex, Cursor, and other Agent Skills-compatible coding agents. Optimized for React + TypeScript; supports Next.js, Vite, Tailwind CSS and existing component systems. Requires web/package access only when checking current library versions or installing dependencies.
metadata:
  author: Elder Windson / OpenAI-assisted
  version: "1.0.0"
  updated: "2026-09-18"
---

# FrontMD — Frontend Design Director

FrontMD is a design-and-implementation skill for building interfaces that feel intentionally art-directed rather than assembled from AI defaults.

The goal is not to maximize the number of UI libraries. The goal is to choose a coherent visual system, use the smallest reliable component stack, and deliver a frontend that is distinctive, accessible, responsive, performant, and maintainable.

## Prime directive

Every screen must look like it belongs to this product, this audience, and this use case.

Never produce a generic "AI SaaS" visual language merely because it is easy to generate. Do not default to identical rounded cards, decorative gradients, floating glass panels, purple/blue glow, excessive pills, random bento grids, repetitive icon badges, or the same hero composition for unrelated products.

A beautiful frontend is not a collection of effects. It is a hierarchy of decisions.

## Mandatory operating mode

For every frontend task, work through these stages in order:

1. Reconnaissance
2. Product and visual brief
3. Stack decision
4. Design tokens and layout grammar
5. Component architecture
6. Implementation
7. Responsive and interaction pass
8. Accessibility and performance pass
9. Visual critique
10. Validation gate

Do not skip directly to JSX unless the user explicitly asks for a tiny isolated component.

---

# 1. Reconnaissance before changing code

Inspect the project before installing or replacing anything.

Read, when available:

- `package.json`
- the lockfile (`pnpm-lock.yaml`, `bun.lock`, `package-lock.json`, or `yarn.lock`)
- framework config
- Tailwind/global CSS configuration
- existing theme/tokens
- `components/`, `ui/`, `layouts/`, and navigation code
- current icon library
- existing form/table/chart/motion dependencies
- routes and primary user flows
- screenshots or reference designs supplied by the user

Determine:

- framework and versions
- package manager already used by the repository
- rendering model: SPA, SSR, RSC, hybrid
- current primitive/component base
- whether a design system already exists
- which components are reusable versus duplicated
- accessibility and responsive debt
- whether the task is an incremental redesign or a new visual language

### Never do these during reconnaissance

- Do not migrate Next.js to Vite or Vite to Next.js just for preference.
- Do not replace an established primitive library without a concrete benefit.
- Do not install multiple libraries that solve the same base problem.
- Do not add animation packages before determining whether CSS is sufficient.
- Do not erase a valid brand system to impose FrontMD defaults.

---

# 2. Build a compact design brief

Before coding a substantial interface, establish the following internally and make the decisions visible in the implementation:

- **Product:** what is being built?
- **Audience:** who uses it and in what environment?
- **Primary job:** what is the most important action or information?
- **Trust level:** consumer, enterprise, government, health, finance, internal tool, etc.
- **Information density:** low, medium, high.
- **Brand personality:** e.g. precise, institutional, editorial, energetic, calm, technical, premium.
- **Signature idea:** one memorable visual or interaction decision that belongs to this project.
- **Restraint rule:** what visual device will deliberately *not* be overused?

If the brief is incomplete, infer conservative defaults from the domain and existing product, then proceed. Do not block work with unnecessary questions.

## Design direction rules

Choose a specific direction rather than combining fashionable effects.

Examples of legitimate directions:

- editorial/information-led
- precision enterprise
- calm institutional
- industrial/technical
- high-density operations console
- expressive consumer
- premium minimal
- warm human service
- data-first analytical

The chosen direction must drive typography, spacing, color, shape, borders, motion, and imagery.

---

# 3. Stack decision — use a hierarchy, not a pile

Read `references/stack-selection.md` before introducing new UI dependencies.

## Preferred React stack for new work

Use this as a decision tree, not a mandatory bundle:

### Foundation

- React + TypeScript
- Existing framework if healthy
- Tailwind CSS v4 when Tailwind is already present or suitable for the project
- CSS custom properties for semantic design tokens
- OKLCH for new color systems when browser support requirements allow it

### Component distribution

Prefer **shadcn/ui** when the project benefits from owning the component source and customizing it deeply.

For a new shadcn-based project, choose exactly one base:

- **Base UI** — preferred default for a fresh general-purpose product when its components cover the required interactions.
- **React Aria** — prefer when accessibility, internationalization, interaction modalities, complex selection, or enterprise-grade behavior are especially important.
- **Radix Primitives** — prefer when the repository already depends on Radix, when compatibility is important, or when a required primitive is best supported there.

Do not casually mix Base UI, React Aria, and Radix implementations of the same component family.

### Functional headless engines

Use specialized headless libraries when behavior is complex and visual ownership matters:

- TanStack Table for serious tables/data grids
- TanStack Query for server-state workflows where already appropriate
- TanStack Virtual for large virtualized lists/tables
- React Hook Form + schema validation for large forms when the project already follows that pattern

### Elevated visual components

Use these selectively, never as the whole design language:

- Animate UI — tasteful motion-enhanced primitives and components
- Aceternity UI — signature marketing/hero/visual moments
- Kibo UI — higher-level functional components compatible with shadcn-style stacks
- 21st.dev — component discovery and inspiration; review quality and dependencies before adopting code

Treat third-party visual blocks as raw material. Restyle them to the product tokens and remove visual gimmicks that do not serve the product.

### Motion

- CSS transitions/animations for simple hover, focus, opacity, color, and small transforms
- Motion for React for stateful, layout, gesture, scroll, presence, and orchestrated animation
- Introduce GSAP only when the brief truly requires timeline-heavy or specialized animation beyond the existing stack

### Icons

Use one icon family per product surface unless the brand system explicitly supports more.

Prefer:

- Lucide for neutral interface systems
- Phosphor when a softer or more expressive icon personality is appropriate

Never decorate every heading with an icon.

---

# 4. Freshness protocol for libraries

FrontMD must remain useful after its creation date.

Before installing a package:

1. Inspect what the repo already uses.
2. Use the repo's existing package manager.
3. Check the package's current official documentation and peer dependency compatibility when network access exists.
4. Prefer stable releases over experimental/canary versions unless the user requested otherwise.
5. Avoid hardcoding a historical version merely because it appears in this skill.
6. Verify React/framework compatibility before install.
7. Prefer source-owned/open-code components where long-term customization matters.
8. Record why each new dependency is needed.

Dependency test: if the design can be implemented cleanly with the existing stack, do not add a package.

---

# 5. Create a real token system before styling screens

For substantial work, define semantic tokens before one-off utilities spread through the UI.

Minimum token categories:

- canvas/background
- surface levels
- foreground/text levels
- border/subtle border
- primary/action
- accent/signature
- destructive/warning/success/info
- focus ring
- spacing rhythm
- container widths
- radius scale
- shadow/elevation scale
- typography scale
- motion durations/easings

Prefer semantic names such as `--surface-raised` and `--text-muted`, not component-specific names like `--card-gray`.

## Typography

Typography must carry product personality.

- Choose fonts intentionally from available/local/licensed sources.
- Do not automatically choose Inter just because it is common.
- Use one family well or a deliberate pair.
- Define a coherent type scale.
- Keep body measure readable; long prose should generally stay below roughly 75–80 characters per line.
- Use weight, width, size, spacing, and line-height intentionally.
- Avoid all-caps eyebrow labels above every section.
- Avoid coloring one random word in every headline as a default design trick.

## Spacing

Use a small spacing rhythm and break it only deliberately.

Do not give every component the same padding. Density should reflect importance and task frequency.

## Radius and elevation

Do not apply one large rounded radius to every surface.

Use shape hierarchically:

- controls
- cards/surfaces
- modal/sheet
- media
- decorative elements

Shadows must communicate elevation or interaction, not decorate every container.

---

# 6. Layout grammar

Every page should have an identifiable composition rule.

Decide:

- main container logic
- column/grid system
- density
- vertical rhythm
- section boundaries
- sticky regions
- navigation shell
- breakpoint behavior

## Avoid the generated-template layout

Do not automatically build:

`navbar → centered hero → 3 feature cards → bento grid → testimonials → pricing → FAQ → CTA`

Use that only if the content and product genuinely require it.

For application screens, avoid wrapping every logical group in a bordered card. Use whitespace, alignment, typography, table structure, dividers, background layers, and hierarchy before creating another card.

---

# 7. Navigation and menu quality

Navigation is a product architecture decision, not a decorative component.

## Choose the shell by information architecture

Use a **top navigation** when:

- destinations are few
- hierarchy is shallow
- content width benefits from full viewport

Use a **sidebar** when:

- the app has many stable destinations
- users switch contexts frequently
- nested sections matter
- admin/operations workflows dominate

Use **hybrid navigation** only when top-level context and deep local navigation both genuinely exist.

For mobile, choose intentionally among:

- compact top bar + sheet/drawer
- bottom navigation for a small set of frequent destinations
- context-specific tabs

### Menu standards

Menus must support:

- visible active state
- keyboard navigation
- focus management
- responsive collapse behavior
- tooltips only when collapsed labels become ambiguous
- sensible grouping
- readable labels instead of unexplained icons
- accessible hit targets
- no layout jump when opening/closing

Do not build a flashy animated navigation if it reduces scan speed for frequent operational use.

---

# 8. Component rules

Build components around reusable behavior and visual grammar, not arbitrary fragments.

Each reusable component should consider:

- default state
- hover
- focus-visible
- active/pressed
- disabled
- loading
- error
- empty
- long content
- narrow viewport
- dark/light theme if supported
- reduced motion

## Buttons

Button hierarchy must be obvious without relying only on color.

Do not create five competing primary buttons in one viewport.

## Forms

- labels remain visible
- placeholder is not a label
- validation is specific and located near the field
- preserve user input on recoverable failures
- group related fields
- use appropriate input types/autocomplete
- show pending/success/error states
- keep destructive actions visually and spatially distinct

## Tables and data-heavy screens

Use semantic table patterns when data is tabular.

For advanced tables, prefer a headless engine and own the visual markup.

Support as needed:

- sorting
- filtering
- pagination or virtualization
- column visibility
- bulk selection
- sticky headers
- density controls
- responsive fallback
- empty/loading/error states

Do not turn every desktop table into unrelated cards on mobile without considering which columns/actions matter.

## Dialogs, sheets, popovers

Use the right layer:

- popover for lightweight contextual interaction
- dialog for focused modal task
- sheet/drawer for secondary workflows or mobile navigation

Never use modal dialogs for information that belongs directly in page flow.

---

# 9. Motion system

Motion must explain change, reinforce hierarchy, or add a deliberate signature moment.

Use three motion tiers:

- **Tier 1 — feedback:** 100–180ms for hover/focus/press feedback
- **Tier 2 — state transition:** 180–320ms for menus, tabs, drawers, accordions
- **Tier 3 — signature:** longer only for one deliberate hero/reveal/visual narrative

Values are guidelines; adapt to the product.

Rules:

- Prefer transform/opacity for smooth animation.
- Respect `prefers-reduced-motion`.
- Avoid animating every card on scroll.
- Avoid identical fade-up entrance animations for every section.
- Avoid perpetual motion behind dense content.
- Interaction-triggered motion is usually more useful than decorative autonomous motion.
- Test motion on touch and low-power devices.

---

# 10. Anti-AI aesthetic filter

Before finalizing, actively search for these tells and remove them unless justified by the brief:

- generic purple/blue gradient as default brand
- glow behind every hero
- glassmorphism without product rationale
- every section inside a rounded rectangle
- identical cards with icon + title + paragraph
- bento grid used only because it is fashionable
- excessive pill-shaped controls and badges
- huge radius everywhere
- all-caps eyebrow labels repeated above headings
- random monospace labels to imply "tech"
- arrow glyph appended to every CTA
- one colored/italicized word in every headline
- meaningless decorative grid/noise/dots
- multiple animation styles competing on one page
- hero copy that sounds like generic startup filler
- fake metrics or placeholder testimonials presented as real
- oversized empty whitespace that harms operational density
- dashboard charts added without a decision-making purpose

A page can use any of these devices. It simply must earn them.

Read `references/anti-ai-aesthetic.md` for the full critique checklist.

---

# 11. Responsive design is not shrinking desktop

Validate at minimum around these viewport classes:

- 360–390px phone
- 768px tablet
- 1024px small desktop/tablet landscape
- 1280–1440px desktop
- wide desktop when relevant

For each major screen ask:

- What disappears?
- What moves?
- What changes order?
- What becomes scrollable?
- What becomes a sheet/menu?
- Which actions remain immediately accessible?
- Does the information hierarchy still make sense?

Use modern CSS layout capabilities where appropriate, including Grid, Flexbox, `minmax()`, `clamp()`, container queries, logical properties, and intrinsic sizing.

Prevent horizontal overflow unless the interaction explicitly calls for it.

---

# 12. Accessibility gate

Target WCAG 2.2 AA behavior for production work unless the project specifies a stricter target.

Mandatory checks:

- semantic HTML first
- keyboard-only operability
- visible focus
- logical focus order
- accessible labels/names
- contrast
- status/error announcements where needed
- no color-only meaning
- adequate target sizing
- escape/close behavior for overlays
- focus restoration after modal interactions
- reduced-motion support
- drag interactions have an alternative where required

Automated axe checks are useful but not sufficient. Perform manual keyboard and visual checks too.

---

# 13. Performance gate

Visual quality does not justify a slow product.

Prefer:

- framework-native image optimization when available
- correct image dimensions/aspect ratios
- font subset/preload strategy where appropriate
- lazy loading for below-the-fold heavy media
- minimal client-only boundaries
- tree-shakable imports
- no giant animation dependency for one hover effect
- virtualization for very large lists/tables
- code splitting when justified

Use current Core Web Vitals as field targets when measurable. At the time this skill was authored, the commonly referenced "good" thresholds are LCP <= 2.5s, INP <= 200ms, and CLS <= 0.1 at the 75th percentile; verify current guidance when making performance commitments.

---

# 14. Implementation quality

- TypeScript types should describe component contracts.
- Keep data/business logic separate from visual primitives where practical.
- Prefer composition over giant boolean-prop components.
- Avoid premature abstraction, but remove obvious duplication.
- Keep styling colocated enough to be maintainable.
- Use semantic tokens rather than scattering raw color values.
- Preserve existing project conventions unless they are the problem being fixed.
- Do not silently break route behavior, auth, forms, analytics, or API integration during a visual refactor.

---

# 15. Visual critique pass

After implementation, inspect the rendered result rather than trusting the source code.

Ask:

1. Can the product/domain be guessed from the screen without reading the logo?
2. Is there one clear visual hierarchy?
3. Does the design feel specific rather than trendy-by-default?
4. Are repeated components actually consistent?
5. Is there too much chrome?
6. Is spacing intentional or merely generous?
7. Does the typography have a point of view?
8. Is the primary action obvious?
9. Is every decorative effect doing useful work?
10. Does mobile feel designed, not collapsed?

When browser tooling is available, capture screenshots at multiple breakpoints and correct issues found visually.

---

# 16. Validation gate — do not call the frontend finished before this

For substantial work, run or approximate the following checks according to the repository tooling.

## Build and static checks

- install succeeds
- typecheck succeeds
- lint succeeds
- production build succeeds

## Component/UI checks

Use Storybook when the project has or benefits from a component system:

- important states represented as stories
- interaction tests for stateful components
- accessibility addon/checks
- visual regression for critical components

## End-to-end and visual checks

Use Playwright when available:

- core flows work
- keyboard flow works
- critical overlays/menus/forms work
- axe scan for automatically detectable accessibility issues
- screenshots or visual comparisons for critical pages

## Responsive checks

Verify critical screens at phone, tablet, and desktop sizes.

## Performance checks

Use Lighthouse/Lighthouse CI or the project's established tooling where practical.

Read `references/validation.md` for an executable validation sequence.

---

# 17. FrontMD quality score

Before finishing a major UI task, score the implementation from 0–10 in each category:

1. Product specificity
2. Visual hierarchy
3. Typography
4. Color/token coherence
5. Layout/composition
6. Interaction/motion quality
7. Responsive behavior
8. Accessibility
9. Performance
10. Maintainability/consistency

A major task should not be considered FrontMD-ready if:

- any category is below 7, or
- the total is below 85/100, or
- accessibility/build checks fail, or
- obvious generic AI-template tells remain.

Do not game the score. Fix the weak category and re-review.

---

# 18. Output behavior for coding agents

When asked to implement:

- make the code changes, do not only describe them
- summarize the chosen direction and new dependencies briefly
- mention any intentional deviation from the existing design system
- report validation actually performed
- do not claim tests passed unless they were run

When asked to audit only:

- identify issues by severity and user impact
- distinguish aesthetic preference from usability/accessibility defects
- propose a staged correction plan
- do not rewrite the entire stack when targeted corrections will solve the problem

When working from a reference image/site:

- reproduce the *design logic* and quality level, not copyrighted brand assets or exact proprietary composition unless the user owns/provides them
- preserve the target product's identity rather than cloning another product blindly

---

# 19. Reference files

Use these supporting documents as needed:

- `references/stack-selection.md` — stack and library decision matrix
- `references/anti-ai-aesthetic.md` — visual anti-patterns and critique process
- `references/validation.md` — QA and visual validation sequence
- `references/source-survey.md` — market/official-source survey used to build FrontMD

For structural validation of this skill package, run:

`python scripts/validate_skill.py`
