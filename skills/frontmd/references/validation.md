# FrontMD Validation Sequence

Run what applies to the repository. Never claim a check passed if it was not executed.

## Phase A — Structural checks

1. Install dependencies with the repository's package manager.
2. Run typecheck.
3. Run lint.
4. Run unit/component tests.
5. Run production build.

Stop and fix regressions before visual sign-off.

## Phase B — Browser review

Open each critical route and inspect:

- loading
- default
- empty
- error
- populated
- long-content states

Where auth prevents test access, use project-approved fixtures or test accounts; do not weaken production auth just to take a screenshot.

## Phase C — Responsive viewport matrix

Recommended baseline:

| Class | Example viewport |
|---|---:|
| Small phone | 360×800 |
| Modern phone | 390×844 |
| Tablet portrait | 768×1024 |
| Small desktop | 1024×768 |
| Desktop | 1440×900 |

Also test product-specific breakpoints and orientation changes where relevant.

Look for:

- horizontal overflow
- clipped menus
- unreadable tables
- misplaced fixed/sticky elements
- layout shift from async content
- touch targets too small
- bad line wrapping
- hidden primary actions

## Phase D — Keyboard test

Without mouse:

- reach all actionable elements
- open/close menus
- open/close dialogs/sheets
- traverse form controls
- submit/cancel forms
- see focus at all times
- ensure focus is not trapped except intentionally in modal contexts
- ensure focus returns to the logical trigger after modal close

## Phase E — Automated accessibility

When Playwright exists or can be added appropriately, run `@axe-core/playwright` checks on critical routes and interactive states.

Important: axe catches only a subset of accessibility failures. Keep the manual keyboard/visual pass.

## Phase F — Visual regression

Preferred options:

- Storybook visual tests / Chromatic for reusable components
- Playwright `toHaveScreenshot()` for key pages/flows

Keep screenshot baselines in a stable environment.

Critical visual targets often include:

- navigation expanded/collapsed
- major dashboard
- primary form
- modal/sheet
- table with data
- empty state
- mobile navigation

## Phase G — Interaction tests

For Storybook or Playwright, test at least the important behavior:

- menu open/close
- tabs
- dropdown/select
- dialog focus
- form validation
- destructive confirmation
- loading and retry
- table filters/sorting if critical

## Phase H — Motion/reduced motion

Check:

- animations do not block interaction
- no large layout jank
- `prefers-reduced-motion` results in a usable experience
- hover-only interactions have touch equivalents
- autoplay effects are restrained

## Phase I — Performance

Where practical:

- run Lighthouse or Lighthouse CI
- inspect bundle changes after introducing UI packages
- inspect large images and fonts
- ensure below-the-fold visual effects are not eagerly expensive

Field targets should use current Web Vitals guidance. Verify current thresholds for formal performance commitments.

## Phase J — FrontMD quality score

Score 0–10:

- Product specificity
- Hierarchy
- Typography
- Color/tokens
- Layout
- Interaction/motion
- Responsive behavior
- Accessibility
- Performance
- Maintainability

Rules:

- no individual score < 7
- total target >= 85/100
- build/typecheck and critical interaction regressions must be resolved
- accessibility failures with material impact must be resolved

## Reporting template

Use a concise completion report:

- Design direction: ...
- Stack changes: ...
- Key components changed: ...
- Validation run: ...
- Remaining known limitations: ...
