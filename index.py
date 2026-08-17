HOME_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MedParser — Medical Report AI Extractor API</title>
  <meta name="description" content="High-precision medical report parsing and lab biomarker extraction API using Google Gemini AI and FastAPI.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    /* Hallmark · pre-emit critique: P5 H5 E5 S5 R5 V5 */
    /* Hallmark · macrostructure: 01-bento-grid · theme: cobalt · genre: modern-minimal · nav: N3 · footer: Ft2 · slop: pass (42–45) · contrast: pass (40–41) */

    :root {
      /* Hallmark Cobalt Theme Tokens (OKLCH) */
      --color-paper: oklch(98.5% 0.004 250);
      --color-paper-2: oklch(96% 0.006 250);
      --color-paper-3: oklch(93.5% 0.008 250);
      --color-rule: oklch(90% 0.008 250);
      --color-rule-2: oklch(82% 0.012 250);
      --color-ink: oklch(24% 0.02 258);
      --color-ink-2: oklch(45% 0.018 257);
      --color-muted: oklch(62% 0.014 257);
      --color-accent: oklch(58% 0.20 256);
      --color-accent-hover: oklch(52% 0.21 256);
      --color-accent-ink: oklch(98.5% 0.004 250);
      --color-focus: oklch(58% 0.20 256);

      /* Dark Graphite Band Tokens */
      --color-graphite: oklch(20% 0.016 260);
      --color-graphite-card: oklch(24% 0.018 260);
      --color-graphite-rule: oklch(34% 0.016 260);
      --color-graphite-rule-2: oklch(42% 0.018 260);
      --color-graphite-ink: oklch(95% 0.006 250);
      --color-graphite-ink-2: oklch(82% 0.010 250);
      --color-graphite-muted: oklch(66% 0.012 250);

      /* Semantic Status Indicators */
      --color-success: oklch(68% 0.18 145);
      --color-warning: oklch(75% 0.16 75);
      --color-danger: oklch(60% 0.22 25);
      --color-danger-bg: oklch(96% 0.04 25);

      /* Typography Tokens */
      --font-display: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-body: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      /* Spacing Scale (4-pt grid) */
      --space-3xs: 0.25rem;
      --space-2xs: 0.5rem;
      --space-xs: 0.75rem;
      --space-sm: 1rem;
      --space-md: 1.5rem;
      --space-lg: 2rem;
      --space-xl: 3rem;
      --space-2xl: 4.5rem;
      --space-3xl: 6rem;

      /* Radii - tight technical corners */
      --radius-sm: 4px;
      --radius-md: 6px;
      --radius-lg: 10px;

      /* Motion */
      --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
      --dur-fast: 150ms;
      --dur-med: 240ms;
    }

    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html, body {
      overflow-x: clip;
      background-color: var(--color-paper);
      color: var(--color-ink-2);
      font-family: var(--font-body);
      font-size: 15px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    h1, h2, h3, h4, h5, h6 {
      font-family: var(--font-display);
      color: var(--color-ink);
      font-style: normal;
      font-weight: 600;
      line-height: 1.15;
      letter-spacing: -0.025em;
    }

    p {
      color: var(--color-ink-2);
      font-size: 1rem;
      line-height: 1.65;
    }

    a {
      color: var(--color-ink);
      text-decoration: none;
      transition: color var(--dur-fast) var(--ease-out);
    }
    a:hover {
      color: var(--color-accent);
    }

    /* Container */
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 var(--space-md);
    }

    /* Navigation (N3 Archetype) */
    .nav-bar {
      position: sticky;
      top: 0;
      z-index: 100;
      background: color-mix(in srgb, var(--color-paper) 88%, transparent);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--color-rule);
    }
    .nav-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0.85rem var(--space-md);
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: var(--space-sm);
    }
    .brand {
      display: flex;
      align-items: center;
      gap: var(--space-xs);
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.15rem;
      color: var(--color-ink);
      letter-spacing: -0.03em;
    }
    .brand-tag {
      font-family: var(--font-mono);
      font-size: 0.7rem;
      font-weight: 500;
      color: var(--color-accent);
      background: var(--color-paper-2);
      border: 1px solid var(--color-rule);
      padding: 0.15rem 0.45rem;
      border-radius: var(--radius-sm);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: var(--space-md);
      list-style: none;
    }
    .nav-link {
      font-size: 0.9rem;
      font-weight: 500;
      color: var(--color-ink-2);
      position: relative;
      padding: 0.2rem 0;
    }
    .nav-link:hover {
      color: var(--color-ink);
    }
    .nav-right {
      display: flex;
      align-items: center;
      gap: var(--space-xs);
    }
    .cmd-trigger {
      display: inline-flex;
      align-items: center;
      gap: var(--space-xs);
      background: var(--color-paper-2);
      border: 1px solid var(--color-rule);
      border-radius: var(--radius-md);
      padding: 0.4rem 0.75rem;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--color-muted);
      cursor: pointer;
      transition: border-color var(--dur-fast), background var(--dur-fast);
    }
    .cmd-trigger:hover {
      border-color: var(--color-rule-2);
      background: var(--color-paper-3);
      color: var(--color-ink);
    }
    .cmd-trigger kbd {
      background: var(--color-paper);
      border: 1px solid var(--color-rule-2);
      border-radius: 3px;
      padding: 0.1rem 0.35rem;
      font-size: 0.7rem;
      font-weight: 600;
      color: var(--color-ink-2);
    }

    /* Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.45rem;
      font-family: var(--font-body);
      font-size: 0.88rem;
      font-weight: 500;
      line-height: 1;
      padding: 0.65rem 1.15rem;
      border-radius: var(--radius-md);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all var(--dur-fast) var(--ease-out);
      white-space: nowrap;
      text-decoration: none;
    }
    .btn:focus-visible {
      outline: 2px solid var(--color-focus);
      outline-offset: 2px;
    }
    .btn--primary {
      background: var(--color-accent);
      color: var(--color-accent-ink);
      border-color: var(--color-accent);
    }
    .btn--primary:hover {
      background: var(--color-accent-hover);
      border-color: var(--color-accent-hover);
      color: var(--color-accent-ink);
    }
    .btn--primary:active {
      transform: translateY(1px);
    }
    .btn--secondary {
      background: var(--color-paper-2);
      color: var(--color-ink);
      border-color: var(--color-rule);
    }
    .btn--secondary:hover {
      background: var(--color-paper-3);
      border-color: var(--color-rule-2);
      color: var(--color-ink);
    }
    .btn--secondary:active {
      transform: translateY(1px);
    }
    .btn--ghost {
      background: transparent;
      color: var(--color-ink-2);
      border-color: transparent;
    }
    .btn--ghost:hover {
      background: var(--color-paper-2);
      color: var(--color-ink);
    }
    .btn--graphite {
      background: var(--color-accent);
      color: var(--color-accent-ink);
      border-color: var(--color-accent);
      font-weight: 600;
    }
    .btn--graphite:hover {
      background: var(--color-accent-hover);
      color: var(--color-accent-ink);
    }
    .btn:disabled, .btn[aria-disabled="true"] {
      opacity: 0.55;
      cursor: not-allowed;
      pointer-events: none;
    }

    /* Eyebrows & Machine Readouts */
    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 500;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--color-accent);
      margin-bottom: var(--space-xs);
    }
    .eyebrow::before {
      content: "";
      display: inline-block;
      width: 6px;
      height: 6px;
      background: var(--color-accent);
      border-radius: 1px;
    }
    .eyebrow--dark {
      color: var(--color-accent);
    }

    /* Hero Section (Asymmetric Cobalt-01 Pattern) */
    .hero-section {
      padding: var(--space-2xl) 0 var(--space-2xl);
      border-bottom: 1px solid var(--color-rule);
    }
    .hero-grid {
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: var(--space-xl);
      align-items: center;
    }
    .hero-content {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }
    .hero-title {
      font-size: clamp(2.2rem, 4vw, 3.1rem);
      line-height: 1.08;
      letter-spacing: -0.035em;
      color: var(--color-ink);
      margin-bottom: var(--space-sm);
    }
    .hero-lede {
      font-size: 1.08rem;
      color: var(--color-ink-2);
      line-height: 1.6;
      max-width: 54ch;
      margin-bottom: var(--space-lg);
    }
    .hero-actions {
      display: flex;
      align-items: center;
      gap: var(--space-xs);
      flex-wrap: wrap;
      margin-bottom: var(--space-lg);
    }
    .hero-specs {
      display: flex;
      align-items: center;
      gap: var(--space-sm);
      flex-wrap: wrap;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--color-muted);
      padding-top: var(--space-xs);
      border-top: 1px solid var(--color-rule);
      width: 100%;
    }
    .spec-item {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }
    .spec-item strong {
      color: var(--color-ink);
      font-weight: 500;
    }

    /* Code Card Specimen Hero */
    .code-card {
      background: var(--color-graphite);
      border: 1px solid var(--color-graphite-rule);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 4px 20px -2px oklch(20% 0.016 260 / 0.15);
      display: flex;
      flex-direction: column;
    }
    .code-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.65rem 0.9rem;
      background: color-mix(in srgb, var(--color-graphite-card) 60%, transparent);
      border-bottom: 1px solid var(--color-graphite-rule);
      font-family: var(--font-mono);
      font-size: 0.78rem;
    }
    .code-endpoint {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--color-graphite-ink);
    }
    .method-badge {
      background: var(--color-accent);
      color: var(--color-accent-ink);
      padding: 0.15rem 0.45rem;
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 0.7rem;
      letter-spacing: 0.04em;
    }
    .code-status {
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.74rem;
      color: var(--color-success);
    }
    .code-status::before {
      content: "";
      display: inline-block;
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--color-success);
    }
    .code-nav {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--color-graphite-rule);
      background: var(--color-graphite);
      padding: 0 0.5rem;
    }
    .code-tabs {
      display: flex;
      gap: 0.2rem;
    }
    .code-tab {
      background: transparent;
      border: none;
      border-bottom: 2px solid transparent;
      padding: 0.55rem 0.75rem;
      font-family: var(--font-mono);
      font-size: 0.76rem;
      color: var(--color-graphite-muted);
      cursor: pointer;
      transition: all var(--dur-fast);
    }
    .code-tab:hover {
      color: var(--color-graphite-ink);
    }
    .code-tab.is-active {
      color: var(--color-accent);
      border-bottom-color: var(--color-accent);
      font-weight: 500;
    }
    .copy-btn {
      background: transparent;
      border: 1px solid var(--color-graphite-rule);
      border-radius: var(--radius-sm);
      padding: 0.25rem 0.55rem;
      color: var(--color-graphite-muted);
      font-family: var(--font-mono);
      font-size: 0.72rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all var(--dur-fast);
    }
    .copy-btn:hover {
      background: var(--color-graphite-card);
      border-color: var(--color-graphite-rule-2);
      color: var(--color-graphite-ink);
    }
    .code-body {
      padding: 1rem 1.1rem;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      line-height: 1.6;
      color: var(--color-graphite-ink);
      overflow-x: auto;
      max-height: 380px;
    }
    .code-panel {
      display: none;
    }
    .code-panel.is-active {
      display: block;
    }
    pre {
      margin: 0;
      font-family: inherit;
    }
    /* Syntax Tokens */
    .tok-kw { color: var(--color-accent); font-weight: 500; }
    .tok-fn { color: oklch(75% 0.16 210); }
    .tok-str { color: oklch(85% 0.10 145); }
    .tok-key { color: oklch(88% 0.05 250); font-weight: 500; }
    .tok-num { color: oklch(78% 0.14 80); }
    .tok-cmt { color: var(--color-graphite-muted); font-style: normal; }
    .tok-flg { color: var(--color-warning); font-weight: 600; }

    /* Bento Grid Macrostructure 01 */
    .section {
      padding: var(--space-2xl) 0;
      border-bottom: 1px solid var(--color-rule);
    }
    .section-header {
      margin-bottom: var(--space-xl);
      max-width: 680px;
    }
    .section-title {
      font-size: clamp(1.75rem, 3vw, 2.3rem);
      margin-bottom: var(--space-xs);
    }
    .section-desc {
      font-size: 1.02rem;
      color: var(--color-ink-2);
    }

    .bento-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: var(--space-sm);
    }
    .bento-cell {
      background: var(--color-paper-2);
      border: 1px solid var(--color-rule);
      border-radius: var(--radius-lg);
      padding: var(--space-md);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: border-color var(--dur-fast) var(--ease-out), background-color var(--dur-fast);
    }
    .bento-cell:hover {
      border-color: var(--color-rule-2);
      background: color-mix(in srgb, var(--color-paper-2) 90%, var(--color-paper-3));
    }
    .span-2x1 {
      grid-column: span 2;
    }
    .span-1x1 {
      grid-column: span 1;
    }
    .bento-header {
      margin-bottom: var(--space-sm);
    }
    .bento-num {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--color-accent);
      font-weight: 600;
      margin-bottom: var(--space-2xs);
    }
    .bento-title {
      font-size: 1.2rem;
      font-weight: 600;
      margin-bottom: 0.4rem;
      color: var(--color-ink);
    }
    .bento-desc {
      font-size: 0.92rem;
      color: var(--color-ink-2);
      line-height: 1.55;
    }
    .bento-preview {
      margin-top: var(--space-md);
      background: var(--color-paper);
      border: 1px solid var(--color-rule);
      border-radius: var(--radius-md);
      padding: 0.75rem;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--color-ink);
      overflow-x: auto;
    }
    .bento-pill-group {
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
      margin-top: var(--space-md);
    }
    .bento-pill {
      font-family: var(--font-mono);
      font-size: 0.74rem;
      padding: 0.2rem 0.55rem;
      border-radius: var(--radius-sm);
      background: var(--color-paper);
      border: 1px solid var(--color-rule);
      color: var(--color-ink-2);
    }

    /* Interactive Studio Workbench (Light Engineered Surface) */
    .studio-section {
      background: var(--color-paper-2);
      color: var(--color-ink-2);
      padding: var(--space-3xl) 0;
      border-top: 1px solid var(--color-rule);
      border-bottom: 1px solid var(--color-rule);
    }
    .studio-section h2, .studio-section h3, .studio-section h4 {
      color: var(--color-ink);
    }
    .studio-section p {
      color: var(--color-ink-2);
    }
    .workbench-grid {
      display: grid;
      grid-template-columns: 1fr 1.25fr;
      gap: var(--space-lg);
      margin-top: var(--space-xl);
      align-items: start;
    }

    /* Workbench Form Panel */
    .form-panel {
      background: var(--color-paper);
      border: 1px solid var(--color-rule);
      border-radius: var(--radius-lg);
      padding: var(--space-lg);
      box-shadow: 0 4px 16px -4px oklch(24% 0.02 258 / 0.04);
    }
    .form-group {
      margin-bottom: var(--space-md);
    }
    .form-label {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 0.76rem;
      font-weight: 500;
      color: var(--color-ink);
      margin-bottom: 0.4rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .form-label-hint {
      font-size: 0.7rem;
      color: var(--color-muted);
      text-transform: none;
      letter-spacing: normal;
    }
    .input-wrapper {
      position: relative;
      display: flex;
      align-items: center;
    }
    .text-input, .select-input {
      width: 100%;
      height: 42px;
      background: var(--color-paper-2);
      border: 1px solid var(--color-rule);
      border-radius: var(--radius-md);
      padding: 0 0.85rem;
      font-family: var(--font-body);
      font-size: 0.88rem;
      color: var(--color-ink);
      transition: border-color var(--dur-fast);
      outline: 2px solid transparent;
      outline-offset: 1px;
    }
    .text-input:focus, .select-input:focus {
      border-color: var(--color-accent);
      outline: 2px solid var(--color-focus);
    }
    .text-input::placeholder {
      color: var(--color-muted);
    }
    .toggle-pass {
      position: absolute;
      right: 0.6rem;
      background: transparent;
      border: none;
      color: var(--color-muted);
      font-family: var(--font-mono);
      font-size: 0.72rem;
      cursor: pointer;
      padding: 0.2rem 0.4rem;
    }
    .toggle-pass:hover {
      color: var(--color-ink);
    }

    /* File Dropzone */
    .dropzone {
      border: 1px dashed var(--color-rule-2);
      border-radius: var(--radius-md);
      padding: var(--space-md) var(--space-sm);
      text-align: center;
      background: var(--color-paper-2);
      cursor: pointer;
      transition: all var(--dur-fast);
    }
    .dropzone:hover, .dropzone.is-dragover {
      border-color: var(--color-accent);
      background: color-mix(in srgb, var(--color-paper-2) 90%, var(--color-accent) 10%);
    }
    .dropzone-icon {
      font-size: 1.5rem;
      margin-bottom: 0.35rem;
    }
    .dropzone-title {
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--color-ink);
      margin-bottom: 0.2rem;
    }
    .dropzone-desc {
      font-size: 0.76rem;
      color: var(--color-muted);
      font-family: var(--font-mono);
    }
    .file-input-hidden {
      display: none;
    }
    .file-selected-badge {
      display: none;
      margin-top: 0.6rem;
      padding: 0.35rem 0.65rem;
      background: var(--color-paper-2);
      border: 1px solid var(--color-accent);
      border-radius: var(--radius-sm);
      font-family: var(--font-mono);
      font-size: 0.74rem;
      color: var(--color-ink);
      text-align: left;
    }

    .sample-btn {
      background: var(--color-paper-2);
      border: 1px dashed var(--color-rule-2);
      border-radius: var(--radius-md);
      color: var(--color-ink-2);
      font-family: var(--font-mono);
      font-size: 0.76rem;
      padding: 0.45rem 0.8rem;
      cursor: pointer;
      width: 100%;
      text-align: center;
      margin-top: var(--space-xs);
      transition: all var(--dur-fast);
    }
    .sample-btn:hover {
      background: var(--color-paper-3);
      border-color: var(--color-ink);
      color: var(--color-ink);
    }

    /* Workbench Result Panel */
    .result-panel {
      background: var(--color-paper);
      border: 1px solid var(--color-rule);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      min-height: 480px;
      box-shadow: 0 4px 16px -4px oklch(24% 0.02 258 / 0.04);
    }
    .result-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.65rem 1rem;
      border-bottom: 1px solid var(--color-rule);
      background: var(--color-paper-2);
      font-family: var(--font-mono);
      font-size: 0.76rem;
    }
    .result-tabs {
      display: flex;
      gap: 0.3rem;
    }
    .result-tab {
      background: transparent;
      border: none;
      border-bottom: 2px solid transparent;
      padding: 0.4rem 0.65rem;
      font-family: var(--font-mono);
      font-size: 0.76rem;
      color: var(--color-muted);
      cursor: pointer;
      transition: all var(--dur-fast);
    }
    .result-tab:hover {
      color: var(--color-ink);
    }
    .result-tab.is-active {
      color: var(--color-accent);
      border-bottom-color: var(--color-accent);
      font-weight: 500;
    }
    .result-meta {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--color-muted);
    }
    .result-meta .copy-btn {
      border: 1px solid var(--color-rule-2);
      color: var(--color-ink-2);
    }
    .result-meta .copy-btn:hover {
      background: var(--color-paper-3);
      border-color: var(--color-ink);
      color: var(--color-ink);
    }
    .result-body {
      padding: 1.1rem;
      flex-grow: 1;
      overflow-y: auto;
      max-height: 520px;
    }
    .result-view {
      display: none;
    }
    .result-view.is-active {
      display: block;
    }

    /* Visual Report View */
    .report-card {
      background: var(--color-paper-2);
      border: 1px solid var(--color-rule);
      border-radius: var(--radius-md);
      padding: 1rem;
      margin-bottom: var(--space-md);
    }
    .report-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: var(--space-xs);
      font-size: 0.82rem;
    }
    .meta-row {
      display: flex;
      flex-direction: column;
    }
    .meta-lbl {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      color: var(--color-muted);
      text-transform: uppercase;
    }
    .meta-val {
      color: var(--color-ink);
      font-weight: 500;
    }
    .clinical-summary-box {
      margin-top: 0.8rem;
      padding-top: 0.8rem;
      border-top: 1px solid var(--color-rule);
      font-size: 0.85rem;
      line-height: 1.5;
      color: var(--color-ink-2);
    }
    .clinical-summary-box strong {
      color: var(--color-ink);
      font-family: var(--font-mono);
      font-size: 0.75rem;
      text-transform: uppercase;
      display: block;
      margin-bottom: 0.25rem;
    }

    /* Lab Test Table */
    .test-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.8rem;
      text-align: left;
    }
    .test-table th {
      font-family: var(--font-mono);
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--color-muted);
      padding: 0.5rem 0.65rem;
      border-bottom: 1px solid var(--color-rule-2);
    }
    .test-table td {
      padding: 0.55rem 0.65rem;
      border-bottom: 1px solid var(--color-rule);
      color: var(--color-ink);
    }
    .test-table tr:hover td {
      background: var(--color-paper-2);
    }
    .badge-abnormal {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.65rem;
      font-weight: 600;
      color: oklch(48% 0.22 25);
      background: oklch(96% 0.04 25);
      border: 1px solid oklch(75% 0.15 25);
      padding: 0.1rem 0.35rem;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }
    .badge-normal {
      display: inline-block;
      font-family: var(--font-mono);
      font-size: 0.65rem;
      font-weight: 500;
      color: oklch(44% 0.16 145);
      background: oklch(96% 0.04 145);
      border: 1px solid oklch(75% 0.12 145);
      padding: 0.1rem 0.35rem;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
    }

    #jsonPreformatted, #headersTelemetryPre {
      display: block;
      background: var(--color-graphite);
      border: 1px solid var(--color-graphite-rule);
      border-radius: var(--radius-md);
      padding: 1rem;
      color: var(--color-graphite-ink);
      font-family: var(--font-mono);
      font-size: 0.78rem;
      line-height: 1.55;
      overflow-x: auto;
    }

    /* API Specification Table */
    .spec-table-wrapper {
      border: 1px solid var(--color-rule);
      border-radius: var(--radius-lg);
      overflow: hidden;
      background: var(--color-paper-2);
      margin-top: var(--space-lg);
    }
    .spec-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }
    .spec-table th {
      background: var(--color-paper-3);
      padding: 0.75rem 1rem;
      font-family: var(--font-mono);
      font-size: 0.74rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--color-ink);
      text-align: left;
      border-bottom: 1px solid var(--color-rule-2);
    }
    .spec-table td {
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--color-rule);
      color: var(--color-ink-2);
    }
    .spec-table tr:last-child td {
      border-bottom: none;
    }
    .spec-table code {
      font-family: var(--font-mono);
      font-size: 0.8em;
      background: var(--color-paper);
      border: 1px solid var(--color-rule-2);
      padding: 0.15rem 0.35rem;
      border-radius: 3px;
      color: var(--color-ink);
    }

    /* Command Palette Modal (⌘K) */
    .cmd-overlay {
      position: fixed;
      inset: 0;
      background: oklch(15% 0.01 260 / 0.65);
      backdrop-filter: blur(6px);
      z-index: 1000;
      display: flex;
      align-items: flex-start;
      justify-content: center;
      padding-top: 15vh;
      opacity: 0;
      visibility: hidden;
      transition: opacity var(--dur-fast), visibility var(--dur-fast);
    }
    .cmd-overlay.is-open {
      opacity: 1;
      visibility: visible;
    }
    .cmd-dialog {
      width: 100%;
      max-width: 580px;
      background: var(--color-paper);
      border: 1px solid var(--color-rule-2);
      border-radius: var(--radius-lg);
      box-shadow: 0 20px 40px -10px oklch(15% 0.02 260 / 0.25);
      overflow: hidden;
      transform: translateY(-8px) scale(0.98);
      transition: transform var(--dur-fast) var(--ease-out);
    }
    .cmd-overlay.is-open .cmd-dialog {
      transform: translateY(0) scale(1);
    }
    .cmd-search-box {
      display: flex;
      align-items: center;
      padding: 0.85rem 1.1rem;
      border-bottom: 1px solid var(--color-rule);
      gap: 0.65rem;
    }
    .cmd-search-input {
      width: 100%;
      border: none;
      background: transparent;
      font-family: var(--font-body);
      font-size: 0.95rem;
      color: var(--color-ink);
      outline: none;
    }
    .cmd-list {
      max-height: 320px;
      overflow-y: auto;
      padding: 0.5rem;
      list-style: none;
    }
    .cmd-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.6rem 0.85rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      color: var(--color-ink-2);
      cursor: pointer;
      transition: background var(--dur-fast), color var(--dur-fast);
    }
    .cmd-item:hover, .cmd-item.is-selected {
      background: var(--color-paper-3);
      color: var(--color-ink);
    }
    .cmd-item-action {
      font-family: var(--font-mono);
      font-size: 0.72rem;
      color: var(--color-muted);
    }

    /* Reveal Animation */
    .reveal {
      opacity: 0;
      transform: translateY(8px);
      transition: opacity 0.5s var(--ease-out), transform 0.5s var(--ease-out);
    }
    .reveal.is-in {
      opacity: 1;
      transform: none;
    }

    /* Footer (Ft2 Archetype) */
    .footer {
      background: var(--color-paper);
      border-top: 1px solid var(--color-rule);
      padding: var(--space-xl) 0 var(--space-lg);
    }
    .footer-content {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: var(--space-md);
      flex-wrap: wrap;
    }
    .footer-left {
      display: flex;
      flex-direction: column;
      gap: 0.3rem;
    }
    .footer-brand {
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1rem;
      color: var(--color-ink);
      letter-spacing: -0.02em;
    }
    .footer-sub {
      font-size: 0.8rem;
      color: var(--color-muted);
    }
    .footer-status {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      color: var(--color-success);
      background: var(--color-paper-2);
      border: 1px solid var(--color-rule);
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-sm);
    }
    .status-dot {
      width: 6px;
      height: 6px;
      background: var(--color-success);
      border-radius: 50%;
    }
    .footer-links {
      display: flex;
      gap: var(--space-md);
      list-style: none;
      font-size: 0.82rem;
    }

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {
      .reveal {
        opacity: 1 !important;
        transform: none !important;
        transition: none !important;
      }
      .cmd-overlay, .cmd-dialog {
        transition: none !important;
      }
    }

    /* Responsive */
    @media (max-width: 900px) {
      .hero-grid {
        grid-template-columns: 1fr;
        gap: var(--space-lg);
      }
      .bento-grid {
        grid-template-columns: 1fr;
      }
      .span-2x1 {
        grid-column: span 1;
      }
      .workbench-grid {
        grid-template-columns: 1fr;
      }
      .nav-links {
        display: none;
      }
    }
    @media (max-width: 640px) {
      .hero-title {
        font-size: 2rem;
      }
      .footer-content {
        flex-direction: column;
        align-items: flex-start;
      }
    }
  </style>
</head>
<body>

  <!-- Navigation (N3 Archetype) -->
  <header class="nav-bar">
    <div class="nav-container">
      <a href="/" class="brand" aria-label="MedParser Home">
        MedParser
        <span class="brand-tag">REST API v1.0</span>
      </a>

      <nav aria-label="Main Navigation">
        <ul class="nav-links">
          <li><a href="#capabilities" class="nav-link">Capabilities</a></li>
          <li><a href="#quickstart" class="nav-link">Quickstart</a></li>
          <li><a href="#studio" class="nav-link">Live Studio</a></li>
          <li><a href="#spec" class="nav-link">API Reference</a></li>
          <li><a href="/docs" class="nav-link" target="_blank">Swagger UI ↗</a></li>
        </ul>
      </nav>

      <div class="nav-right">
        <button class="cmd-trigger" id="cmdTriggerBtn" aria-label="Open Command Palette">
          Search
          <kbd>⌘K</kbd>
        </button>
        <a href="#studio" class="btn btn--primary">Try Live</a>
      </div>
    </div>
  </header>

  <main>
    <!-- Hero Section (Asymmetric Cobalt-01 Pattern) -->
    <section class="hero-section" id="quickstart">
      <div class="container hero-grid">
        
        <div class="hero-content reveal">
          <div class="eyebrow">REST API · GEMINI MULTIMODAL OCR</div>
          <h1 class="hero-title">Medical report parsing, structured in milliseconds.</h1>
          <p class="hero-lede">
            Extract patient demographics, lab biomarkers, reference ranges, and abnormal flags directly into typed Pydantic JSON schemas. Zero server-side API key retention with pure header-based authentication.
          </p>
          <div class="hero-actions">
            <a href="#studio" class="btn btn--primary">Open Interactive Studio ↓</a>
            <button class="btn btn--secondary" id="heroCopyCurlBtn">Copy cURL Snippet</button>
            <a href="/docs" class="btn btn--ghost" target="_blank">Swagger OpenAPI Spec ↗</a>
          </div>
          <div class="hero-specs">
            <div class="spec-item">Endpoint: <strong>POST /extract</strong></div>
            <div class="spec-item">Max Payload: <strong>15MB Multipart</strong></div>
            <div class="spec-item">Format: <strong>PDF / PNG / JPEG / WEBP / HEIC</strong></div>
          </div>
        </div>

        <div class="code-card reveal" style="transition-delay: 100ms;">
          <div class="code-header">
            <div class="code-endpoint">
              <span class="method-badge">POST</span>
              <span>/extract</span>
            </div>
            <div class="code-status">200 OK · 148ms</div>
          </div>
          <div class="code-nav">
            <div class="code-tabs">
              <button class="code-tab is-active" data-target="panel-curl">cURL</button>
              <button class="code-tab" data-target="panel-python">Python</button>
              <button class="code-tab" data-target="panel-ts">TypeScript</button>
              <button class="code-tab" data-target="panel-schema">JSON Schema</button>
            </div>
            <button class="copy-btn" id="heroCodeCopyBtn">Copy</button>
          </div>

          <div class="code-body">
            <!-- cURL Panel -->
            <div class="code-panel is-active" id="panel-curl">
<pre><code><span class="tok-fn">curl</span> -X POST <span class="tok-str">"https://your-domain.com/extract"</span> \
  -H <span class="tok-str">"accept: application/json"</span> \
  -H <span class="tok-key">"X-Gemini-Api-Key: $GEMINI_API_KEY"</span> \
  -H <span class="tok-key">"X-Gemini-Model: gemini-3.7-flash"</span> \
  -F <span class="tok-str">"file=@medical_lab_report.pdf"</span></code></pre>
            </div>

            <!-- Python Panel -->
            <div class="code-panel" id="panel-python">
<pre><code><span class="tok-kw">import</span> requests

url = <span class="tok-str">"https://your-domain.com/extract"</span>
headers = {
    <span class="tok-key">"X-Gemini-Api-Key"</span>: <span class="tok-str">"AIzaSy..."</span>,
    <span class="tok-key">"X-Gemini-Model"</span>: <span class="tok-str">"gemini-3.7-flash"</span>
}
files = {<span class="tok-key">"file"</span>: open(<span class="tok-str">"report.pdf"</span>, <span class="tok-str">"rb"</span>)}

response = requests.post(url, headers=headers, files=files)
data = response.json()
print(<span class="tok-str">f"Extracted {len(data['data']['tests'])} lab tests"</span>)</code></pre>
            </div>

            <!-- TypeScript Panel -->
            <div class="code-panel" id="panel-ts">
<pre><code><span class="tok-kw">const</span> formData = <span class="tok-kw">new</span> FormData();
formData.append(<span class="tok-str">"file"</span>, fileBlob, <span class="tok-str">"report.pdf"</span>);

<span class="tok-kw">const</span> res = <span class="tok-kw">await</span> fetch(<span class="tok-str">"/extract"</span>, {
  method: <span class="tok-str">"POST"</span>,
  headers: {
    <span class="tok-key">"X-Gemini-Api-Key"</span>: process.env.GEMINI_API_KEY,
    <span class="tok-key">"X-Gemini-Model"</span>: <span class="tok-str">"gemini-3.7-flash"</span>
  },
  body: formData
});
<span class="tok-kw">const</span> result = <span class="tok-kw">await</span> res.json();</code></pre>
            </div>

            <!-- JSON Schema Panel -->
            <div class="code-panel" id="panel-schema">
<pre><code>{
  <span class="tok-key">"success"</span>: <span class="tok-kw">true</span>,
  <span class="tok-key">"model_used"</span>: <span class="tok-str">"gemini-3.7-flash"</span>,
  <span class="tok-key">"data"</span>: {
    <span class="tok-key">"patient_name"</span>: <span class="tok-str">"Eleanor Vance"</span>,
    <span class="tok-key">"patient_id"</span>: <span class="tok-str">"MRN-884920"</span>,
    <span class="tok-key">"date"</span>: <span class="tok-str">"2026-08-14"</span>,
    <span class="tok-key">"tests"</span>: [
      {
        <span class="tok-key">"name"</span>: <span class="tok-str">"Hemoglobin A1c"</span>,
        <span class="tok-key">"value"</span>: <span class="tok-str">"6.8"</span>,
        <span class="tok-key">"unit"</span>: <span class="tok-str">"%"</span>,
        <span class="tok-key">"reference_range"</span>: <span class="tok-str">"4.0 - 5.6"</span>,
        <span class="tok-key">"is_abnormal"</span>: <span class="tok-flg">true</span>,
        <span class="tok-key">"category"</span>: <span class="tok-str">"Endocrine"</span>
      }
    ]
  }
}</code></pre>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- Bento Grid Section (Macrostructure 01) -->
    <section class="section" id="capabilities">
      <div class="container">
        <div class="section-header reveal">
          <div class="eyebrow">01 · ARCHITECTURE & CAPABILITIES</div>
          <h2 class="section-title">Engineered for clinical document workflows.</h2>
          <p class="section-desc">Modular extraction pipeline with zero storage footprint and strict type fidelity.</p>
        </div>

        <div class="bento-grid">
          <!-- Bento 1: Strict Schemas -->
          <article class="bento-cell span-2x1 reveal">
            <div class="bento-header">
              <div class="bento-num">01.01</div>
              <h3 class="bento-title">Schema-Enforced Structured Extraction</h3>
              <p class="bento-desc">
                Converts unstructured clinical scans into fully typed Pydantic data models. Captures patient demographics, ordering physician, lab metadata, categorized biomarker panels, and clinical synthesis.
              </p>
            </div>
            <div class="bento-preview">
              <code>MedicalReport(patient_name, patient_id, date, lab_name, tests: List[Test])</code>
            </div>
          </article>

          <!-- Bento 2: Zero Retention Header Auth -->
          <article class="bento-cell span-1x1 reveal" style="transition-delay: 50ms;">
            <div class="bento-header">
              <div class="bento-num">01.02</div>
              <h3 class="bento-title">Zero Key Retention</h3>
              <p class="bento-desc">
                Credentials are authenticated exclusively via client-supplied <code>X-Gemini-Api-Key</code> request headers. The server operates completely statelessly.
              </p>
            </div>
            <div class="bento-pill-group">
              <span class="bento-pill">No DB Storage</span>
              <span class="bento-pill">Stateless</span>
              <span class="bento-pill">Header Auth</span>
            </div>
          </article>

          <!-- Bento 3: Multimodal Document Support -->
          <article class="bento-cell span-1x1 reveal" style="transition-delay: 100ms;">
            <div class="bento-header">
              <div class="bento-num">01.03</div>
              <h3 class="bento-title">Multimodal Ingestion</h3>
              <p class="bento-desc">
                Native parsing for PDFs and raster formats up to 15MB. Automatically decodes multi-page records and photographic captures.
              </p>
            </div>
            <div class="bento-pill-group">
              <span class="bento-pill">.PDF</span>
              <span class="bento-pill">.PNG</span>
              <span class="bento-pill">.JPEG</span>
              <span class="bento-pill">.WEBP</span>
              <span class="bento-pill">.HEIC</span>
            </div>
          </article>

          <!-- Bento 4: Abnormal Flags -->
          <article class="bento-cell span-1x1 reveal" style="transition-delay: 150ms;">
            <div class="bento-header">
              <div class="bento-num">01.04</div>
              <h3 class="bento-title">Abnormal Result Flagging</h3>
              <p class="bento-desc">
                Per-biomarker evaluation against documented lab reference intervals. Sets <code>is_abnormal: true</code> for immediate diagnostic triaging.
              </p>
            </div>
            <div class="bento-pill-group">
              <span class="bento-pill">Reference Intervals</span>
              <span class="bento-pill">Boolean Flags</span>
            </div>
          </article>

          <!-- Bento 5: Gemini 3.7 / 3.6 / 2.5 Flash Engine -->
          <article class="bento-cell span-1x1 reveal" style="transition-delay: 200ms;">
            <div class="bento-header">
              <div class="bento-num">01.05</div>
              <h3 class="bento-title">Gemini Flash Models</h3>
              <p class="bento-desc">
                Configurable model routing supporting <code>gemini-3.7-flash</code>, <code>gemini-3.6-flash</code>, <code>gemini-2.5-flash</code>, and <code>gemini-2.5-pro</code> with exponential retry backoff.
              </p>
            </div>
            <div class="bento-pill-group">
              <span class="bento-pill">3.7 Flash</span>
              <span class="bento-pill">3.6 Flash</span>
              <span class="bento-pill">2.5 Flash</span>
              <span class="bento-pill">2.5 Pro</span>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Interactive Studio Workbench -->
    <section class="studio-section" id="studio">
      <div class="container">
        <div class="section-header reveal">
          <div class="eyebrow">02 · INTERACTIVE WORKBENCH</div>
          <h2>Live Document Extraction Studio.</h2>
          <p>Test the API directly in your browser. Credentials stay on the client and are sent via HTTP headers.</p>
        </div>

        <div class="workbench-grid">
          <!-- Request Form Panel -->
          <div class="form-panel reveal">
            <form id="liveExtractForm">
              
              <div class="form-group">
                <label class="form-label" for="apiKeyInput">
                  <span>Gemini API Key</span>
                  <span class="form-label-hint">Header: X-Gemini-Api-Key</span>
                </label>
                <div class="input-wrapper">
                  <input type="password" id="apiKeyInput" class="text-input" placeholder="AIzaSy..." autocomplete="off" required>
                  <button type="button" class="toggle-pass" id="toggleApiKeyBtn">Show</button>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label" for="modelSelect">
                  <span>Gemini Model</span>
                  <span class="form-label-hint">Header: X-Gemini-Model</span>
                </label>
                <select id="modelSelect" class="select-input">
                  <option value="gemini-3.7-flash" selected>gemini-3.7-flash (Latest & Recommended)</option>
                  <option value="gemini-3.6-flash">gemini-3.6-flash</option>
                  <option value="gemini-2.5-flash">gemini-2.5-flash</option>
                  <option value="gemini-2.5-pro">gemini-2.5-pro (Deep reasoning)</option>
                </select>
              </div>

              <div class="form-group">
                <label class="form-label">
                  <span>Medical Report Document</span>
                  <span class="form-label-hint">Max 15MB</span>
                </label>
                <div class="dropzone" id="fileDropzone">
                  <div class="dropzone-icon">📄</div>
                  <div class="dropzone-title">Click to upload or drag & drop</div>
                  <div class="dropzone-desc">PDF, PNG, JPG, WEBP, or HEIC</div>
                  <input type="file" id="fileInput" class="file-input-hidden" accept=".pdf,.png,.jpg,.jpeg,.webp,.heic,.heif">
                </div>
                <div class="file-selected-badge" id="fileSelectedBadge">
                  Selected: <span id="fileNameDisplay">None</span>
                </div>
                <button type="button" class="sample-btn" id="loadSampleDocBtn">Load Synthetic Lab Panel Sample</button>
              </div>

              <button type="submit" class="btn btn--primary" id="executeBtn" style="width: 100%; height: 42px;">
                Execute Extraction (POST /extract)
              </button>
            </form>
          </div>

          <!-- Result Inspector Panel -->
          <div class="result-panel reveal" style="transition-delay: 100ms;">
            <div class="result-header">
              <div class="result-tabs">
                <button class="result-tab is-active" data-view="view-visual">Visual Report</button>
                <button class="result-tab" data-view="view-json">JSON Output</button>
                <button class="result-tab" data-view="view-headers">Headers & Telemetry</button>
              </div>
              <div class="result-meta">
                <span id="responseStatusBadge">Ready</span>
                <span id="responseLatency">—</span>
                <button class="copy-btn" id="copyResultBtn">Copy JSON</button>
              </div>
            </div>

            <div class="result-body">
              <!-- Visual View -->
              <div class="result-view is-active" id="view-visual">
                <div id="visualEmptyState" style="text-align: center; padding: 4rem 1rem; color: var(--color-muted);">
                  <div style="font-size: 2rem; margin-bottom: 0.5rem; opacity: 0.6;">🧪</div>
                  <div style="font-family: var(--font-mono); font-size: 0.85rem;">Provide your Gemini key and submit a medical document to view structured extraction.</div>
                </div>

                <div id="visualContent" style="display: none;">
                  <div class="report-card">
                    <div class="report-meta-grid">
                      <div class="meta-row">
                        <span class="meta-lbl">Patient Name</span>
                        <span class="meta-val" id="resPatientName">—</span>
                      </div>
                      <div class="meta-row">
                        <span class="meta-lbl">Patient ID / MRN</span>
                        <span class="meta-val" id="resPatientId">—</span>
                      </div>
                      <div class="meta-row">
                        <span class="meta-lbl">Report Date</span>
                        <span class="meta-val" id="resDate">—</span>
                      </div>
                      <div class="meta-row">
                        <span class="meta-lbl">Ordering Physician</span>
                        <span class="meta-val" id="resDoctor">—</span>
                      </div>
                    </div>
                    <div class="clinical-summary-box">
                      <strong>Clinical Summary</strong>
                      <div id="resSummary">—</div>
                    </div>
                  </div>

                  <table class="test-table">
                    <thead>
                      <tr>
                        <th>Test / Biomarker</th>
                        <th>Result</th>
                        <th>Ref Range</th>
                        <th>Category</th>
                        <th>Status</th>
                      </tr>
                    </thead>
                    <tbody id="resTableBody">
                      <!-- Dynamically rendered -->
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- Raw JSON View -->
              <div class="result-view" id="view-json">
                <pre><code id="jsonPreformatted" style="color: var(--color-graphite-ink); font-family: var(--font-mono); font-size: 0.78rem;">// Ready for extraction output</code></pre>
              </div>

              <!-- Headers & Telemetry View -->
              <div class="result-view" id="view-headers">
                <pre><code id="headersTelemetryPre" style="color: var(--color-graphite-ink); font-family: var(--font-mono); font-size: 0.78rem;">// Request and response telemetry will appear here after execution</code></pre>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- API Reference Specification Section -->
    <section class="section" id="spec">
      <div class="container">
        <div class="section-header reveal">
          <div class="eyebrow">03 · API CONTRACT & SPECIFICATION</div>
          <h2 class="section-title">Endpoint Reference.</h2>
          <p class="section-desc">Strict REST contracts and status code definitions.</p>
        </div>

        <div class="spec-table-wrapper reveal">
          <table class="spec-table">
            <thead>
              <tr>
                <th>Method & Path</th>
                <th>Required Headers</th>
                <th>Payload</th>
                <th>Response Codes</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><code>POST /extract</code></td>
                <td>
                  <code>X-Gemini-Api-Key: string</code><br>
                  <code>X-Gemini-Model: string</code>
                </td>
                <td>Multipart <code>file</code> (PDF/Image ≤ 15MB)</td>
                <td>
                  <strong>200 OK</strong> · Structured JSON<br>
                  <strong>400</strong> · Invalid file / missing header<br>
                  <strong>401</strong> · Unauthorized key<br>
                  <strong>413</strong> · File size &gt; 15MB<br>
                  <strong>429</strong> · Gemini rate limit<br>
                  <strong>502</strong> · Upstream error
                </td>
              </tr>
              <tr>
                <td><code>GET /health</code></td>
                <td>None</td>
                <td>None</td>
                <td><strong>200 OK</strong> · Service health status</td>
              </tr>
              <tr>
                <td><code>GET /docs</code></td>
                <td>None</td>
                <td>None</td>
                <td><strong>200 OK</strong> · Interactive Swagger UI</td>
              </tr>
              <tr>
                <td><code>GET /redoc</code></td>
                <td>None</td>
                <td>None</td>
                <td><strong>200 OK</strong> · OpenAPI ReDoc Specification</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </main>

  <!-- Command Palette Modal (⌘K) -->
  <div class="cmd-overlay" id="cmdOverlay" role="dialog" aria-modal="true" aria-label="Command Palette">
    <div class="cmd-dialog">
      <div class="cmd-search-box">
        <span style="font-family: var(--font-mono); color: var(--color-muted);">⌘</span>
        <input type="text" class="cmd-search-input" id="cmdInput" placeholder="Type a command or jump to section..." autocomplete="off">
      </div>
      <ul class="cmd-list" id="cmdList">
        <li class="cmd-item is-selected" data-action="goto" data-target="#studio">
          <span>Jump to Interactive Studio</span>
          <span class="cmd-item-action">Section</span>
        </li>
        <li class="cmd-item" data-action="goto" data-target="#capabilities">
          <span>View Capabilities & Bento Grid</span>
          <span class="cmd-item-action">Section</span>
        </li>
        <li class="cmd-item" data-action="goto" data-target="#spec">
          <span>View API Specification</span>
          <span class="cmd-item-action">Section</span>
        </li>
        <li class="cmd-item" data-action="copy-curl">
          <span>Copy cURL Request Command</span>
          <span class="cmd-item-action">Clipboard</span>
        </li>
        <li class="cmd-item" data-action="load-sample">
          <span>Load Synthetic Medical Lab Sample</span>
          <span class="cmd-item-action">Action</span>
        </li>
        <li class="cmd-item" data-action="open-url" data-target="/docs">
          <span>Open Swagger Documentation</span>
          <span class="cmd-item-action">URL ↗</span>
        </li>
        <li class="cmd-item" data-action="open-url" data-target="/health">
          <span>Check Health Status Endpoint</span>
          <span class="cmd-item-action">URL ↗</span>
        </li>
      </ul>
    </div>
  </div>

  <!-- Footer (Ft2 Archetype) -->
  <footer class="footer">
    <div class="container footer-content">
      <div class="footer-left">
        <div class="footer-brand">MedParser API</div>
        <div class="footer-sub">Stateless clinical report extraction with Google Gemini AI.</div>
      </div>
      <div class="footer-status">
        <span class="status-dot"></span>
        <span>All Systems Operational</span>
      </div>
      <ul class="footer-links">
        <li><a href="/docs" target="_blank">Swagger UI</a></li>
        <li><a href="/health" target="_blank">Health Status</a></li>
        <li><a href="https://github.com/devded/medparser" target="_blank">GitHub</a></li>
      </ul>
    </div>
  </footer>

  <script>
    // 1. Reveal Animations with IntersectionObserver
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // 2. Hero Code Tabs Switcher
    const codeTabs = document.querySelectorAll('.code-tab');
    const codePanels = document.querySelectorAll('.code-panel');

    codeTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const target = tab.getAttribute('data-target');
        codeTabs.forEach(t => t.classList.remove('is-active'));
        codePanels.forEach(p => p.classList.remove('is-active'));
        tab.classList.add('is-active');
        document.getElementById(target)?.classList.add('is-active');
      });
    });

    // 3. Hero Code Copy Button
    const heroCodeCopyBtn = document.getElementById('heroCodeCopyBtn');
    heroCodeCopyBtn?.addEventListener('click', () => {
      const activePanel = document.querySelector('.code-panel.is-active');
      if (activePanel) {
        navigator.clipboard.writeText(activePanel.innerText.trim());
        const origText = heroCodeCopyBtn.innerText;
        heroCodeCopyBtn.innerText = 'Copied!';
        setTimeout(() => { heroCodeCopyBtn.innerText = origText; }, 2000);
      }
    });

    const heroCopyCurlBtn = document.getElementById('heroCopyCurlBtn');
    heroCopyCurlBtn?.addEventListener('click', () => {
      const curlSnippet = `curl -X POST "https://your-domain.com/extract" \\\\
  -H "accept: application/json" \\\\
  -H "X-Gemini-Api-Key: $GEMINI_API_KEY" \\\\
  -H "X-Gemini-Model: gemini-3.7-flash" \\\\
  -F "file=@medical_lab_report.pdf"`;
      navigator.clipboard.writeText(curlSnippet);
      const origText = heroCopyCurlBtn.innerText;
      heroCopyCurlBtn.innerText = '✓ Copied cURL';
      setTimeout(() => { heroCopyCurlBtn.innerText = origText; }, 2000);
    });

    // 4. Command Palette (⌘K)
    const cmdOverlay = document.getElementById('cmdOverlay');
    const cmdTriggerBtn = document.getElementById('cmdTriggerBtn');
    const cmdInput = document.getElementById('cmdInput');
    const cmdList = document.getElementById('cmdList');
    const cmdItems = Array.from(cmdList.querySelectorAll('.cmd-item'));

    function openCmd() {
      cmdOverlay.classList.add('is-open');
      cmdInput.value = '';
      filterCmd('');
      setTimeout(() => cmdInput.focus(), 50);
    }
    function closeCmd() {
      cmdOverlay.classList.remove('is-open');
    }

    cmdTriggerBtn?.addEventListener('click', openCmd);
    window.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (cmdOverlay.classList.contains('is-open')) closeCmd();
        else openCmd();
      } else if (e.key === 'Escape' && cmdOverlay.classList.contains('is-open')) {
        closeCmd();
      }
    });

    cmdOverlay.addEventListener('click', (e) => {
      if (e.target === cmdOverlay) closeCmd();
    });

    function filterCmd(query) {
      const q = query.toLowerCase().trim();
      let firstVisible = null;
      cmdItems.forEach(item => {
        const text = item.innerText.toLowerCase();
        const matches = text.includes(q);
        item.style.display = matches ? 'flex' : 'none';
        item.classList.remove('is-selected');
        if (matches && !firstVisible) firstVisible = item;
      });
      if (firstVisible) firstVisible.classList.add('is-selected');
    }

    cmdInput?.addEventListener('input', (e) => filterCmd(e.target.value));

    cmdInput?.addEventListener('keydown', (e) => {
      const visibleItems = cmdItems.filter(item => item.style.display !== 'none');
      const currentIndex = visibleItems.findIndex(item => item.classList.contains('is-selected'));

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        const nextIndex = (currentIndex + 1) % visibleItems.length;
        visibleItems.forEach(i => i.classList.remove('is-selected'));
        visibleItems[nextIndex]?.classList.add('is-selected');
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        const prevIndex = (currentIndex - 1 + visibleItems.length) % visibleItems.length;
        visibleItems.forEach(i => i.classList.remove('is-selected'));
        visibleItems[prevIndex]?.classList.add('is-selected');
      } else if (e.key === 'Enter') {
        e.preventDefault();
        const selected = visibleItems[currentIndex] || visibleItems[0];
        if (selected) executeCmdItem(selected);
      }
    });

    cmdList?.addEventListener('click', (e) => {
      const item = e.target.closest('.cmd-item');
      if (item) executeCmdItem(item);
    });

    function executeCmdItem(item) {
      const action = item.getAttribute('data-action');
      const target = item.getAttribute('data-target');
      closeCmd();

      if (action === 'goto' && target) {
        document.querySelector(target)?.scrollIntoView({ behavior: 'smooth' });
      } else if (action === 'open-url' && target) {
        window.open(target, '_blank');
      } else if (action === 'copy-curl') {
        heroCopyCurlBtn.click();
      } else if (action === 'load-sample') {
        document.getElementById('loadSampleDocBtn')?.click();
      }
    }

    // 5. Workbench API Key Toggle
    const toggleApiKeyBtn = document.getElementById('toggleApiKeyBtn');
    const apiKeyInput = document.getElementById('apiKeyInput');
    toggleApiKeyBtn?.addEventListener('click', () => {
      const isPass = apiKeyInput.type === 'password';
      apiKeyInput.type = isPass ? 'text' : 'password';
      toggleApiKeyBtn.innerText = isPass ? 'Hide' : 'Show';
    });

    // 6. Workbench File Dropzone
    const dropzone = document.getElementById('fileDropzone');
    const fileInput = document.getElementById('fileInput');
    const fileSelectedBadge = document.getElementById('fileSelectedBadge');
    const fileNameDisplay = document.getElementById('fileNameDisplay');
    let loadedFileBlob = null;

    dropzone?.addEventListener('click', () => fileInput.click());
    fileInput?.addEventListener('change', (e) => {
      if (fileInput.files.length > 0) {
        setFile(fileInput.files[0]);
      }
    });

    dropzone?.addEventListener('dragover', (e) => {
      e.preventDefault();
      dropzone.classList.add('is-dragover');
    });
    dropzone?.addEventListener('dragleave', () => dropzone.classList.remove('is-dragover'));
    dropzone?.addEventListener('drop', (e) => {
      e.preventDefault();
      dropzone.classList.remove('is-dragover');
      if (e.dataTransfer.files.length > 0) {
        setFile(e.dataTransfer.files[0]);
      }
    });

    function setFile(file) {
      loadedFileBlob = file;
      fileNameDisplay.innerText = `${file.name} (${(file.size / 1024).toFixed(1)} KB)`;
      fileSelectedBadge.style.display = 'block';
    }

    // 7. Load Synthetic Sample
    const loadSampleDocBtn = document.getElementById('loadSampleDocBtn');
    loadSampleDocBtn?.addEventListener('click', () => {
      const sampleText = `COMPREHENSIVE METABOLIC & LIPID PANEL
Patient: Vance, Eleanor (ID: MRN-884920)
Date of Service: 2026-08-14
Ordering Physician: Dr. Marcus Reed, MD
Laboratory: Apex Diagnostics Center

TESTS:
Glucose, Fasting: 118 mg/dL [Reference: 70 - 99 mg/dL] (HIGH)
Hemoglobin A1c: 6.8 % [Reference: 4.0 - 5.6 %] (HIGH)
Total Cholesterol: 215 mg/dL [Reference: 125 - 200 mg/dL] (HIGH)
HDL Cholesterol: 48 mg/dL [Reference: > 40 mg/dL] (NORMAL)
LDL Cholesterol: 142 mg/dL [Reference: < 100 mg/dL] (HIGH)
Triglycerides: 165 mg/dL [Reference: < 150 mg/dL] (HIGH)
Creatinine: 0.9 mg/dL [Reference: 0.6 - 1.2 mg/dL] (NORMAL)
eGFR: > 90 mL/min/1.73m2 [Reference: > 60 mL/min/1.73m2] (NORMAL)
TSH: 2.15 uIU/mL [Reference: 0.40 - 4.50 uIU/mL] (NORMAL)`;

      const blob = new Blob([sampleText], { type: 'text/plain' });
      const sampleFile = new File([blob], 'sample_synthetic_lab_panel.txt', { type: 'text/plain' });
      setFile(sampleFile);
      document.querySelector('#studio')?.scrollIntoView({ behavior: 'smooth' });
    });

    // 8. Result Tabs (Visual vs JSON vs Headers)
    const resultTabs = document.querySelectorAll('.result-tab');
    const resultViews = document.querySelectorAll('.result-view');

    resultTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const viewId = tab.getAttribute('data-view');
        resultTabs.forEach(t => t.classList.remove('is-active'));
        resultViews.forEach(v => v.classList.remove('is-active'));
        tab.classList.add('is-active');
        document.getElementById(viewId)?.classList.add('is-active');
      });
    });

    // 9. Form Submission & Real-time Live Extraction
    const liveExtractForm = document.getElementById('liveExtractForm');
    const executeBtn = document.getElementById('executeBtn');
    const responseStatusBadge = document.getElementById('responseStatusBadge');
    const responseLatency = document.getElementById('responseLatency');
    const jsonPreformatted = document.getElementById('jsonPreformatted');
    const headersTelemetryPre = document.getElementById('headersTelemetryPre');
    const copyResultBtn = document.getElementById('copyResultBtn');

    let currentResponseJson = null;

    liveExtractForm?.addEventListener('submit', async (e) => {
      e.preventDefault();
      const apiKey = apiKeyInput.value.trim();
      const model = document.getElementById('modelSelect').value;

      if (!apiKey) {
        alert('Please enter your Gemini API Key.');
        apiKeyInput.focus();
        return;
      }
      if (!loadedFileBlob) {
        alert('Please select or upload a medical document file.');
        return;
      }

      executeBtn.disabled = true;
      executeBtn.innerText = 'Extracting data with Gemini...';
      responseStatusBadge.innerText = 'Processing...';
      responseStatusBadge.style.color = 'var(--color-accent)';
      const startTime = performance.now();

      const formData = new FormData();
      formData.append('file', loadedFileBlob);

      try {
        const res = await fetch('/extract', {
          method: 'POST',
          headers: {
            'X-Gemini-Api-Key': apiKey,
            'X-Gemini-Model': model
          },
          body: formData
        });

        const elapsedMs = Math.round(performance.now() - startTime);
        responseLatency.innerText = `${elapsedMs}ms`;

        const data = await res.json();
        currentResponseJson = data;

        if (res.ok && data.success) {
          responseStatusBadge.innerText = '200 OK';
          responseStatusBadge.style.color = 'var(--color-success)';
          renderVisualReport(data.data);
          jsonPreformatted.innerText = JSON.stringify(data, null, 2);
        } else {
          responseStatusBadge.innerText = `${res.status} Error`;
          responseStatusBadge.style.color = 'var(--color-danger)';
          jsonPreformatted.innerText = JSON.stringify(data, null, 2);
          showVisualError(data.detail || 'Extraction failed.');
        }

        // Telemetry
        headersTelemetryPre.innerText = JSON.stringify({
          endpoint: '/extract',
          method: 'POST',
          model_selected: model,
          client_file_name: loadedFileBlob.name,
          client_file_size_bytes: loadedFileBlob.size,
          http_status: res.status,
          latency_ms: elapsedMs,
          timestamp: new Date().toISOString()
        }, null, 2);

      } catch (err) {
        const elapsedMs = Math.round(performance.now() - startTime);
        responseLatency.innerText = `${elapsedMs}ms`;
        responseStatusBadge.innerText = 'Network Error';
        responseStatusBadge.style.color = 'var(--color-danger)';
        jsonPreformatted.innerText = `Error: ${err.message}`;
        showVisualError(err.message);
      } finally {
        executeBtn.disabled = false;
        executeBtn.innerText = 'Execute Extraction (POST /extract)';
      }
    });

    function renderVisualReport(report) {
      document.getElementById('visualEmptyState').style.display = 'none';
      document.getElementById('visualContent').style.display = 'block';

      document.getElementById('resPatientName').innerText = report.patient_name || 'Not Specified';
      document.getElementById('resPatientId').innerText = report.patient_id || 'N/A';
      document.getElementById('resDate').innerText = report.date || 'N/A';
      document.getElementById('resDoctor').innerText = report.doctor_name || report.lab_name || 'N/A';
      document.getElementById('resSummary').innerText = report.clinical_summary || 'Structured tests extracted successfully.';

      const tbody = document.getElementById('resTableBody');
      tbody.innerHTML = '';

      if (report.tests && report.tests.length > 0) {
        report.tests.forEach(test => {
          const tr = document.createElement('tr');
          const isAbnormal = test.is_abnormal === true;
          tr.innerHTML = `
            <td><strong>${test.name || 'Unnamed Test'}</strong></td>
            <td>${test.value || '—'} ${test.unit || ''}</td>
            <td><span style="color: var(--color-muted);">${test.reference_range || '—'}</span></td>
            <td><span style="font-family: var(--font-mono); font-size: 0.72rem;">${test.category || 'General'}</span></td>
            <td>
              ${isAbnormal
                ? '<span class="badge-abnormal">Abnormal</span>'
                : '<span class="badge-normal">Normal</span>'}
            </td>
          `;
          tbody.appendChild(tr);
        });
      } else {
        tbody.innerHTML = '<tr><td colspan="5" style="text-align: center; color: var(--color-muted);">No lab test rows detected in document.</td></tr>';
      }
    }

    function showVisualError(message) {
      document.getElementById('visualEmptyState').style.display = 'block';
      document.getElementById('visualContent').style.display = 'none';
      document.getElementById('visualEmptyState').innerHTML = `
        <div style="font-size: 2rem; margin-bottom: 0.5rem; color: var(--color-danger);">⚠️</div>
        <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--color-danger);">${message}</div>
      `;
    }

    copyResultBtn?.addEventListener('click', () => {
      if (currentResponseJson) {
        navigator.clipboard.writeText(JSON.stringify(currentResponseJson, null, 2));
        const origText = copyResultBtn.innerText;
        copyResultBtn.innerText = 'Copied!';
        setTimeout(() => { copyResultBtn.innerText = origText; }, 2000);
      }
    });
  </script>
</body>
</html>
"""
