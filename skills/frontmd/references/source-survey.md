# FrontMD Market & Source Survey

Research snapshot: 2026-09-18.

This file records the official/current sources that informed FrontMD. It is not a version lock. Before installation, re-check current documentation and peer compatibility.

## Agent Skill format

- Open Agent Skills specification: https://openagentskills.dev/docs/specification
- Agent Skills conventions use a `SKILL.md` with YAML frontmatter plus optional `scripts/`, `references/`, and `assets/` directories.

## Anthropic frontend-design skill

- Source: https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md
- Relevant idea: an AI frontend skill should explicitly avoid templated/generic aesthetics and force intentional visual direction, typography, layout and critique.
- FrontMD extends this into stack governance, component sourcing, responsive rules, accessibility, performance, testing and a validation gate.

## Lovable

- Designer/stack page: https://lovable.dev/pt-br/designers
- Lovable publicly describes its application stack around React, Tailwind and Supabase.
- Implication: strong perceived design quality cannot be reproduced merely by naming React/Tailwind. Art direction and component composition matter more.

## shadcn/ui

- Docs: https://ui.shadcn.com/docs
- Tailwind v4 / React 19: https://ui.shadcn.com/docs/tailwind-v4
- Skills: https://ui.shadcn.com/docs/skills
- 2026 React Aria base: https://ui.shadcn.com/docs/changelog/2026-07-react-aria
- Core idea: open-code component distribution, deep customization, AI-readable source.
- 2026 state: Base UI, Radix, and React Aria are supported component bases; Base UI is the current default in shadcn's July 2026 announcement.

## Base UI

- Docs: https://base-ui.com/react/overview/quick-start
- Accessibility: https://base-ui.com/react/overview/accessibility
- Headless React components with accessibility behavior and full styling ownership.

## Radix Primitives

- Docs: https://www.radix-ui.com/primitives/docs/overview/introduction
- Mature low-level accessible primitives for design systems and apps.

## React Aria

- Docs: https://react-spectrum.adobe.com/react-aria/
- Unstyled components/hooks emphasizing accessibility, internationalization, devices, input modalities and behavior.

## Tailwind CSS

- Site: https://tailwindcss.com/
- v4.1 article: https://tailwindcss.com/blog/tailwindcss-v4-1
- Useful for fast tokenized styling, but FrontMD requires semantic design tokens to prevent arbitrary utility accumulation.

## Motion for React

- Docs: https://motion.dev/docs/react
- Production animation library for React using browser-native mechanisms plus JS capabilities for springs/gestures/layout.
- FrontMD preference: CSS first for simple transitions, Motion for meaningful interactive/stateful animation.

## Animate UI

- Site: https://animate-ui.com/
- Docs: https://animate-ui.com/docs
- Open component distribution using Tailwind and Motion, inspired by shadcn-style source ownership.

## Aceternity UI

- Site: https://ui.aceternity.com/
- Components: https://ui.aceternity.com/components
- Provides React/Tailwind/Motion visual components, including navbars, sidebars, hero systems and high-impact effects.
- FrontMD policy: use as accent/signature material, not a full default design language.

## Kibo UI

- Docs: https://www.kibo-ui.com/docs
- Higher-level composable components intended to extend shadcn-oriented stacks with richer functionality.

## 21st.dev

- Site: https://21st.dev/
- Large community component discovery catalogue.
- FrontMD policy: source candidates, then audit dependencies, accessibility, responsiveness and style coherence before adoption.

## TanStack Table

- Docs: https://tanstack.com/table/latest/docs/overview
- Current docs in September 2026 identify v9 as latest and emphasize a headless model with full markup/style control.
- Strong fit for data-heavy app screens where custom design and sophisticated table state are both needed.

## Storybook

- Testing overview: https://storybook.js.org/docs/writing-tests
- Visual testing: https://storybook.js.org/docs/writing-tests/visual-testing
- Interaction testing: https://storybook.js.org/docs/writing-tests/interaction-testing
- Accessibility testing: https://storybook.js.org/docs/writing-tests/accessibility-testing
- Useful for isolated component states, visual diffs, interactions and accessibility checks.

## Playwright

- Accessibility: https://playwright.dev/docs/accessibility-testing
- Visual comparisons: https://playwright.dev/docs/test-snapshots
- Supports end-to-end behavior, axe integration and screenshot comparisons.

## WCAG 2.2

- Standard: https://www.w3.org/TR/WCAG22/
- FrontMD targets AA behavior for general production work unless the project specifies another target.

## Core Web Vitals

- Web Vitals: https://web.dev/articles/vitals
- At research time, common 'good' field thresholds: LCP <= 2.5s, INP <= 200ms, CLS <= 0.1 at the 75th percentile.
- Re-check current guidance for formal targets.
