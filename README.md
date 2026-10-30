# A.M. Ward — personal site

Portfolio site covering four focus areas: Brand, Product Marketing, Internal & Executive Communications, and Leadership & Operations.

## Structure

- `src/page.html` — page source (HTML, CSS and JS in one file). Images are referenced by placeholders such as `{{REUSE}}`.
- `src/img/` — campaign images, inlined at build time.
- `build.py` — fills the placeholders and writes the published files.
- `index.html` — the built, self-contained page served by GitHub Pages. Don't edit it by hand.

## Editing

1. Edit `src/page.html` (or add an image to `src/img/` and register it in `build.py`).
2. Run `python3 build.py`.
3. Commit both the source and the rebuilt `index.html`.

## Publishing

GitHub Pages: **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)`**.

The contact email is not stored as plain text; the page assembles it only when a visitor clicks **Email me**.
