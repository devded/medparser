# Design — MedParser

A locked design system for MedParser following the Hallmark anti-AI-slop design skill and the Cobalt-01 (API Product) pattern.

## Genre
modern-minimal

## Theme
- `--color-paper`:        oklch(98.5% 0.004 250)   /* Cool engineered near-white */
- `--color-paper-2`:      oklch(96% 0.006 250)     /* Elevated surface */
- `--color-paper-3`:      oklch(93.5% 0.008 250)   /* Interactive / hover surface */
- `--color-rule`:         oklch(90% 0.008 250)     /* 1px hairline rule */
- `--color-rule-2`:       oklch(82% 0.012 250)     /* Active / strong border */
- `--color-ink`:          oklch(24% 0.02 258)      /* Charcoal ink */
- `--color-ink-2`:        oklch(45% 0.018 257)     /* Secondary body */
- `--color-muted`:        oklch(62% 0.014 257)     /* Subtle annotations */
- `--color-accent`:       oklch(58% 0.20 256)      /* Electric cobalt signal (<5% viewport) */
- `--color-accent-ink`:   oklch(98.5% 0.004 250)   /* Contrast text on cobalt */
- `--color-focus`:        oklch(58% 0.20 256)      /* Focus ring */

/* Dark Graphite Band Tokens */
- `--color-graphite`:      oklch(20% 0.016 260)    /* Dark section base */
- `--color-graphite-card`: oklch(24% 0.018 260)    /* Dark section card */
- `--color-graphite-rule`: oklch(34% 0.016 260)    /* Dark section border */
- `--color-graphite-ink`:  oklch(95% 0.006 250)    /* Light text on dark */
- `--color-graphite-muted`:oklch(68% 0.012 250)    /* Muted text on dark */

## Typography
- Display: Space Grotesk, weights 500, 600, 700 (Roman only; no italic headers)
- Body:    Inter, weights 400, 500, 600
- Mono:    JetBrains Mono, weights 400, 500 (UPPERCASE for small meta badges/labels with tracking 0.06em, and code blocks)

## Macrostructure Family
- Marketing & Docs Hub: `01-bento-grid` (Bento Grid + Asymmetric SaaS / API Product layout with Dark Graphite Interactive Workbench)

## Navigation Archetype
- `N3` (Bordered nav bar with wordmark, version tag, navigation links, working ⌘K command palette, and primary CTA)

## Footer Archetype
- `Ft2` (Minimalist two-part technical footer with uptime status, API endpoints, repository links, and copyright)

## Motion & Microinteractions
- Easings: `cubic-bezier(0.16, 1, 0.3, 1)`
- Reveal pattern: One-shot fade & 8px rise via `IntersectionObserver`
- Hero type-in: One-shot code typewriter effect on initial page load
- Reduced motion: Fully visible, instantaneous transitions with `@media (prefers-reduced-motion: reduce)`
- 8-State compliance: default, hover, focus-visible, active, disabled, loading, error, success
