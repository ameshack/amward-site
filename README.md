# Asia Meshack — personal site

Portfolio site for Asia Meshack: a homepage plus one page per specialty (Brand, Product Marketing, Internal & Executive Communications, Leadership & Operations) and an About page.

## Structure

- `src/content.py` — specialties, projects and shared copy. Each project is defined once and listed by id on the specialty pages that use it.
- `src/site.css`, `src/site.js` — shared styles and behavior (menus, email reveal, links from the old single-page site, opening a project from a link).
- `src/img/` — project images.
- `build.py` — generates the pages. Don't edit the generated HTML by hand.
- Generated output: `index.html`, `brand/`, `product-marketing/`, `communications/`, `leadership/`, `about/`, `assets/`.
- `AM_Ward_Resume.pdf` — the resume behind the **Download resume** button. Until it is added, the build leaves the button out.

## Image sources

Project images are the owner's own campaign, product and published materials. `src/img/strategic-plan.jpg` is cropped from the cover of San Francisco Environment's published 2021–2023 Strategic Plan.

`src/img/year-end-wrap-up.jpg` is a Microsoft year-end video title card, edited at the owner’s request to remove an executive’s name, an internal-use marking and the Microsoft logo. `src/img/year-end-wrap-up-logo.jpg` keeps the logo; point `card_visual` and the `microsoft-exec` image at it to swap it back.

The Holiday Gratitude Campaign project (`microsoft-holiday` in `src/content.py`) is kept in reserve and not published; add its id to a specialty's `projects` list to show it.

## Editing

1. Edit `src/content.py`, `src/site.css`, `src/site.js` or the templates in `build.py`.
2. Run `python3 build.py` for the published site, or `python3 build.py --preview` for a review copy in `dist/preview/` with owner-review notes.
3. Commit the source and the regenerated pages.

Text wrapped in `<!--REVIEW-->` … `<!--/REVIEW-->` appears only in the review copy.

## Publishing

GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / `(root)`**. Pages link to each other with relative URLs, so they work under `/amward-site/`.

The contact email is not stored as plain text; the page assembles it only when a visitor clicks **Email me**.
