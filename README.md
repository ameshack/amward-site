# A.M. Ward — personal site

Portfolio site for A.M. Ward: a homepage plus one page per specialty (Brand, Product Marketing, Internal & Executive Communications, Leadership & Operations) and an About page.

## Structure

- `src/content.py` — specialties, projects and shared copy. Each project is defined once and listed by id on the specialty pages that use it.
- `src/site.css`, `src/site.js` — shared styles and behavior (menus, email reveal, links from the old single-page site, opening a project from a link).
- `src/img/` — project images.
- `build.py` — generates the pages. Don't edit the generated HTML by hand.
- Generated output: `index.html`, `brand/`, `product-marketing/`, `communications/`, `leadership/`, `about/`, `assets/`.
- `AM_Ward_Resume.pdf` — the resume behind the **Download resume** button. Until it is added, the build leaves the button out.

## Editing

1. Edit `src/content.py`, `src/site.css`, `src/site.js` or the templates in `build.py`.
2. Run `python3 build.py` for the published site, or `python3 build.py --preview` for a review copy in `dist/preview/` with owner-review notes.
3. Commit the source and the regenerated pages.

Text wrapped in `<!--REVIEW-->` … `<!--/REVIEW-->` appears only in the review copy.

## Publishing

GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / `(root)`**. Pages link to each other with relative URLs, so they work under `/amward-site/`.

The contact email is not stored as plain text; the page assembles it only when a visitor clicks **Email me**.
