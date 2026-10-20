# Anti-AI Aesthetic Review

Use this document as a critique pass, not as a ban list. Any visual pattern can be correct if it follows from the product brief.

## Why generated frontends often look generated

They optimize for local attractiveness rather than product-specific coherence. The model recognizes popular fragments and repeats them: rounded cards, gradient headlines, bento grids, glow, pills, icon circles, and generous spacing. Individually these can be good. Repeated without context, they become a fingerprint.

## Review 1 — Product specificity

Ask:

- Could this exact screen be relabeled for another SaaS product without changing the layout?
- Do typography, density, imagery and navigation reflect the actual domain?
- Does the page use real information structures from the product?
- Is there a signature idea connected to the subject matter?

If the answer is mostly no, redesign before polishing effects.

## Review 2 — Card addiction

Flag when:

- every section is a card
- cards have identical radius/padding/shadow regardless of hierarchy
- cards are nested inside cards
- whitespace/dividers would communicate grouping better

Correction options:

- remove container chrome
- use alignment
- use a shared background plane
- use rule/divider structure
- change density
- promote important content out of cards

## Review 3 — Gradient and glow addiction

Flag when gradients appear on:

- headline
- logo mark
- primary button
- icon badges
- background glow
- card borders

all in the same viewport.

Keep one or two intentional roles. Remove the rest.

## Review 4 — Repetition disguised as consistency

Consistency is repeated rules; monotony is repeated composition.

Flag:

- every section centered
- every block has the same 3-column grid
- every card has icon/title/body/button
- every heading has eyebrow/headline/subtitle
- every interaction uses scale-on-hover

Introduce controlled variation based on content type.

## Review 5 — Typography tells

Flag:

- default system/Inter typography with no reason
- all-caps labels everywhere
- random monospace metadata
- colored single word in every headline
- huge headline with vague generic copy
- line lengths that are too long
- too many font weights

Correction:

- establish real typographic roles
- use content-specific headline treatment
- choose type based on brand personality
- reduce decorative labels

## Review 6 — Fake technicality

Flag decorative elements that imply technology without conveying information:

- arbitrary grid backgrounds
- meaningless terminal snippets
- random code brackets
- scanning lines
- animated particles
- faux system labels

Use these only when technology itself is part of the product narrative.

## Review 7 — Unnecessary glassmorphism

Glass requires a meaningful layered background. A translucent panel over a flat background is usually just lower contrast.

If glass is used:

- verify readability
- reduce blur cost
- supply a non-transparency fallback where needed
- use it sparingly

## Review 8 — Motion sameness

Flag:

- every section fades up on scroll
- every card lifts on hover
- every button scales
- infinite marquee with no content reason
- delayed entrances slow task completion

Prefer motion tied to state changes or one signature narrative moment.

## Review 9 — Dashboard decoration

Flag:

- KPIs with no timeframe/comparison
- donut charts for simple single values
- tiny charts that cannot be read
- gradients inside data series without meaning
- excessive dashboard cards

Every visualized metric should answer a real operational question.

## Review 10 — Navigation cosplay

Flag:

- sidebars on apps with three destinations
- dock navigation copied from macOS without task rationale
- icon-only primary navigation for non-expert users
- command palettes replacing ordinary discoverable navigation

Choose navigation from information architecture and user frequency.

## Review 11 — Content authenticity

Generated filler can ruin an otherwise strong design.

Avoid presenting as real:

- invented customer logos
- fake testimonials
- fake performance statistics
- fake press quotes

Use clearly marked demo content or realistic domain placeholders.

## Review 12 — Final visual test

At desktop and mobile, view the screen at 100% and answer:

- Where does the eye go first?
- Is that correct?
- Is anything visually loud without being important?
- Is anything important visually weak?
- Is the page too symmetrical?
- Are there more than 2–3 decorative visual languages competing?
- Does the mobile hierarchy preserve the same intent?

Make at least one correction from the critique pass on substantial new work. A critique that changes nothing should be rare.
