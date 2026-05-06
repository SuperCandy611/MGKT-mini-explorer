# Landing Page Prompt Template

Use this prompt with Claude to regenerate or adapt `docs/index.html` for a new project.

---

## Prompt

```
Create docs/index.html as a single-page GitHub Pages site.
No external dependencies (no CDN, no Google Fonts) — pure HTML + inline CSS only.

STRUCTURE — include exactly these 7 sections in order:
1. Hero header: project title (h1) + one-sentence tagline (matches README).
2. Goal: 1–3 sentences stating the research questions.
3. Procedure: ordered list of 4–6 steps written in plain language (no code blocks).
4. Outcome: embed two figures from docs/ with 1–2 sentence captions per figure.
5. Caveats: unordered list of at least 2 limitations (sampling, self-report, inference scope, etc.).
6. Repo link: a styled button linking to the GitHub repo.
7. Author + Date: name, ID, affiliation, Claude attribution, month + year.

STYLE:
- Color palette: 2 main colors + 1 background. Pick colors that match the figures already in the project.
  Current palette: --blue: #2B5F8E (matches steelblue bars), --red: #E05C5C (matches median line), --bg: #F7F9FC (matches chart background).
- Font: system-ui / -apple-system stack (no external fonts).
- Layout: single column, max-width 860px, centered.
- Section styling: white card with border-radius 10px, subtle 1px border, 32px padding.
- Section label: h2 uppercase, letter-spacing 1px, primary color, underlined with 2px border.
- Body text: 17px, line-height 1.7.

FIGURES:
- Copy figure files into docs/ first.
- Reference them with relative paths (e.g., src="fig1_score_distribution.png").
- Each figure: full-width img + figcaption below in muted color.

DESIGN RATIONALE (why these choices):
- Matching chart colors → figures feel embedded, not pasted in.
- system-ui stack → zero latency, best native font per OS.
- Single column 860px → academic reading width, mobile-friendly without media queries.
- Section-as-card pattern → clear visual hierarchy without heavy frameworks.

OUTPUT:
- Write to docs/index.html.
- Also copy relevant figures from reports/ to docs/.
- Commit with: git add docs/ && git commit -m "add GitHub Pages landing page"
```

---

## Customisation checklist

When reusing for a new project, update these values:

| Placeholder | Replace with |
|-------------|-------------|
| Project title & tagline | Your repo's title and one-liner |
| `--blue` hex | Dominant color in your figures |
| `--red` hex | Accent color in your figures |
| `--bg` hex | Background color in your figures |
| Figure filenames | Your actual output PNGs |
| Goal text | Your research questions |
| Procedure steps | Your actual pipeline steps |
| Caveats | Limitations specific to your dataset |
| GitHub repo URL | Your repo URL |
| Author block | Your name, ID, affiliation |
