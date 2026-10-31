# A.M. Ward — personal site

Portfolio site covering four focus areas: Brand, Product Marketing, Internal & Executive Communications, and Leadership & Operations.

## Structure

- `src/page.html` — page source (HTML, CSS and JS in one file). Images are referenced by placeholders such as `{{REUSE}}`.
- `src/img/` — campaign images, inlined at build time.
- `build.py` — fills the placeholders and writes the published files.
- `index.html` — the published page served by GitHub Pages, with owner-review notes removed. Don't edit it by hand.
- `review.html` — the same page with owner-review notes visible (notes are wrapped in `<!--REVIEW-->` … `<!--/REVIEW-->` in the source).
- `AM_Ward_Resume.pdf` — the resume behind the **Download resume** button (to be added by the owner).

## Editing

1. Edit `src/page.html` (or add an image to `src/img/` and register it in `build.py`).
2. Run `python3 build.py`.
3. Commit the source and the rebuilt `index.html` and `review.html`.

## Publishing

GitHub Pages: **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)`**.

The contact email is not stored as plain text; the page assembles it only when a visitor clicks **Email me**.
