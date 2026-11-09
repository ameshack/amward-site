"""Build the Asia Meshack site.

    python3 build.py            published site, written to the repository root
    python3 build.py --preview  review copy in dist/preview/ (owner notes visible,
                                links end in index.html so pages open as files)

Sources: src/content.py (specialties and projects), src/site.css, src/site.js,
src/img/. Text wrapped in <!--REVIEW--> ... <!--/REVIEW--> appears only in the
preview.
"""
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
import content as C  # noqa: E402

PREVIEW = "--preview" in sys.argv
OUT = ROOT / "dist" / "preview" if PREVIEW else ROOT
REVIEW_BLOCK = re.compile(r"\s*<!--REVIEW-->.*?<!--/REVIEW-->", re.S)
FONTS = ("https://fonts.googleapis.com/css2?family=Manrope:wght@600;700;800"
         "&family=Source+Sans+3:wght@400;600;700&display=swap")


def href(root, path):
    """Link to a page directory ("" for home, "brand/") from a page at depth root."""
    if PREVIEW:
        return f"{root}{path}index.html"
    return f"{root}{path}" if path else (root or "./")


def review(html):
    return f"<!--REVIEW-->{html}<!--/REVIEW-->"


def header(root, current):
    work_items = "".join(
        f'<li><a href="{href(root, s["slug"] + "/")}"><strong>{s["name"]}</strong><span>{s["card"]}</span></a></li>'
        for s in C.SPECIALTIES.values())
    mobile_work = "".join(
        f'<a class="sub" href="{href(root, s["slug"] + "/")}">{s["name"]}</a>' for s in C.SPECIALTIES.values())
    about_current = ' aria-current="page"' if current == "about" else ""
    return f"""<a class="skip" href="#main">Skip to content</a>
{review('<div class="review-bar"><div class="wrap">Review version: owner-review notes appear in yellow boxes and are removed from the published site.</div></div>')}
<header class="site-header">
  <div class="wrap">
    <a class="wordmark" href="{href(root, '')}">Asia Meshack, MBA</a>
    <nav class="nav" aria-label="Main">
      <div class="nav-work">
        <button class="nav-work-btn" type="button" aria-expanded="false" aria-controls="work-menu">Work</button>
        <ul class="work-menu" id="work-menu" hidden>{work_items}</ul>
      </div>
      <a href="{href(root, 'about/')}"{about_current}>About</a>
      <a class="ext" href="{C.LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
      <a class="btn btn-primary" href="#contact">Let’s talk</a>
    </nav>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="mobile-panel">Menu</button>
    <nav class="mobile-panel" id="mobile-panel" aria-label="Main">
      <span class="group">Work</span>{mobile_work}
      <a href="{href(root, 'about/')}">About &amp; experience</a>
      <a class="ext" href="{C.LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
      <a class="btn btn-primary" href="#contact">Let’s talk</a>
    </nav>
  </div>
</header>"""


def contact(root, heading="Interested in working together? Let’s talk."):
    return f"""<section class="section contact" id="contact" aria-labelledby="contact-h">
  <div class="wrap">
    <h2 id="contact-h">{heading}</h2>
    <p>I’m open to full-time and consulting work in brand, product marketing, communications and organizational leadership.</p>
    <div class="btn-row">
      <button class="btn btn-primary" type="button" id="reveal">Email me</button>
      <span class="addr" id="email" hidden></span>
      <button class="btn btn-secondary" type="button" id="copy" hidden>Copy</button>
      <a class="btn btn-secondary ext" href="{C.LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
    </div>
    <p class="status" id="status" aria-live="polite"></p>
  </div>
</section>"""


def footer(root):
    links = "".join(f'<li><a href="{href(root, s["slug"] + "/")}">{s["name"]}</a></li>' for s in C.SPECIALTIES.values())
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <a class="wordmark" href="{href(root, '')}">Asia Meshack</a>
      <nav aria-label="Footer"><ul>{links}<li><a href="{href(root, 'about/')}">About</a></li><li><a class="ext" href="{C.LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li><li><a href="#contact">Let’s talk</a></li></ul></nav>
    </div>
    <small>Asia Meshack · Atlanta, Georgia · Remote, USA</small>
  </div>
</footer>"""


def head(title, description, path):
    url = C.SITE_URL + path
    image = C.SITE_URL + "src/img/reuse.jpg"
    return f"""<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Asia Meshack">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">"""


def document(root, page_id, title, description, path, main, fragment=False):
    css = f'<link rel="stylesheet" href="{root}assets/site.css">'
    ext = "index.html" if PREVIEW else ""
    body = f"""{header(root, page_id)}
<main id="main">
{main}
{contact(root)}
</main>
{footer(root)}
<script src="{root}assets/site.js"></script>"""
    meta = head(title, description, path) + "\n" + css
    if fragment:
        # Artifact pages are wrapped in their own document skeleton.
        return (f'{meta}\n<meta name="claude:viewport-fit-sides" content="cover">\n'
                f'<div data-shell></div>\n{body}').replace(
                    '<div data-shell></div>',
                    f'<script>document.body.dataset.root="{root}";document.body.dataset.ext="{ext}";document.body.dataset.page="{page_id}";</script>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{meta}
</head>
<body data-root="{root}" data-ext="{ext}" data-page="{page_id}">
{body}
</body>
</html>
"""


def img(root, image, eager=False):
    loading = "eager" if eager else "lazy"
    classes = [f"focus-{image['focus']}"] if image.get("focus") else []
    if image.get("fit") == "contain":
        classes.append("fit-contain")
    cls = f' class="{" ".join(classes)}"' if classes else ""
    return (f'<img{cls} src="{root}src/img/{image["src"]}" alt="{image["alt"]}" '
            f'width="{image["w"]}" height="{image["h"]}" loading="{loading}" decoding="async">')


def meta_line(p):
    return " · ".join(x for x in (p["org"], p.get("program")) if x)


def outcome(p):
    figure, label = p["outcome"]
    if not figure:
        return f'<p class="outcome mandate"><span>{label}</span></p>'
    second = ""
    if p.get("secondary"):
        f2, l2 = p["secondary"]
        second = f'<p class="outcome-2"><b>{f2}</b><span>{l2}</span></p>'
    return f'<div class="outcomes-pair"><p class="outcome"><b>{figure}</b><span>{label}</span></p>{second}</div>'


def media_cards(root, p):
    """Coverage and examples shown under a project's summary (title, outlet, date, role)."""
    cards = []
    for m in p.get("media", []):
        thumb = ""
        if m.get("img"):
            thumb = (f'<img src="{root}src/img/{m["img"]}" alt="{m["alt"]}" width="640" height="360" '
                     'loading="lazy" decoding="async">')
        source = " · ".join(x for x in (m.get("outlet"), m.get("date")) if x)
        headline = m["headline"]
        if m.get("url"):
            headline = f'<a class="ext" href="{m["url"]}" target="_blank" rel="noopener">{headline}</a>'
        extra = ""
        if m.get("extra"):
            label, url = m["extra"]
            extra = f'<p class="media-extra"><a class="ext" href="{url}" target="_blank" rel="noopener">{label}</a></p>'
        kind = " media-text" if not thumb else ""
        cards.append(f"""<li class="media-card{kind}">{thumb}<div class="media-body">
        <p class="media-label">{m["label"]}</p>
        <p class="media-source">{source}</p>
        <p class="media-headline">{headline}</p>
        <p class="media-role">{m["text"]}</p>{extra}
      </div></li>""")
    return f'\n    <ul class="media-grid" aria-label="Examples">{"".join(cards)}</ul>' if cards else ""


def project(root, pid):
    p = C.PROJECTS[pid]
    approach = f'\n      <div><dt>Strategic approach</dt><dd>{p["approach"]}</dd></div>' if p.get("approach") else ""
    details = "".join(f"<div><h4>{h}</h4>{body}</div>" for h, body in p["details"])
    details = re.sub(r'href="@([^"#]*)(#[^"]*)?"',
                     lambda m: f'href="{href(root, m.group(1))}{m.group(2) or ""}"', details)
    details = details.replace('src="@img/', f'src="{root}src/img/')
    links = "".join(f'<a class="ext" href="{u}" target="_blank" rel="noopener">{t}</a>' for t, u in p["links"])
    links = f'<div class="links">{links}</div>' if links else ""
    image = p.get("image")
    layout = image.get("layout", "side") if image else "text"
    if image and image.get("pair"):
        # Two images shown side by side as the project's primary visual
        media = '<div class="project-media media-pair">' + "".join(
            f'<figure>{img(root, im)}<figcaption class="pair-label">{im["label"]}</figcaption></figure>' if im.get("label") else img(root, im)
            for im in image["pair"]) + "</div>"
    else:
        media = f'<div class="project-media">{img(root, image)}</div>' if image else ""
        if image and image.get("zoom"):
            # Diagrams: open the full-size file so small text stays readable on phones
            media = (f'<div class="project-media"><a class="zoom" href="{root}src/img/{image["src"]}" target="_blank" rel="noopener">'
                     f'{img(root, image)}<span class="zoom-hint">View full size</span></a></div>')
    size = " project-compact" if p.get("compact") else ""
    media_section = ""
    if p.get("media_heading"):
        media_section = f'<div><h4>{p["media_heading"]}</h4>{media_cards(root, p)}</div>'
    return f"""<article class="project project-{layout}{size}" id="{pid}">
  {media}
  <div class="project-body">
    <p class="meta">{meta_line(p)}</p>
    <h3>{p["title"]}</h3>
    {outcome(p)}
    <dl class="summary">
      <div><dt>The challenge</dt><dd>{p["challenge"]}</dd></div>
      <div><dt>{p.get("role_label", "My role")}</dt><dd>{p["role"]}</dd></div>{approach}
    </dl>{"" if p.get("media_heading") else media_cards(root, p)}
    <details class="more">
      <summary>Explore the project<span class="sr-only">: {p["title"]}</span></summary>
      <div class="detail">{media_section}{details}{links}</div>
    </details>
  </div>
</article>"""


def home(root):
    s = C.SPECIALTIES
    proofs = "".join(f"<li><b>{f}</b><span>{l}</span><small>{w}</small></li>" for f, l, w in C.PROOF_POINTS)
    orgs = "".join(f'<li><img src="{root}src/img/logos/{f}" alt="{n}" style="height:{h}px" decoding="async"></li>'
                   for n, f, h in C.RECENT_WORK if (ROOT / "src" / "img" / "logos" / f).exists())
    cards = []
    for sp in (s[k] for k in C.HOME_CARD_ORDER):
        v = sp["card_visual"]
        cls = "card-visual phone" if v.get("phone") else "card-visual"
        style = f' style="object-position:{v["position"]}"' if v.get("position") else ""
        visual = f'<div class="{cls}"><img src="{root}src/img/{v["img"]}" alt=""{style} loading="lazy" decoding="async"></div>'
        cards.append(f"""<a class="card" href="{href(root, sp['slug'] + '/')}">
  {visual}
  <div class="card-body"><h3>{sp['name']}</h3><p>{sp['card']}</p><span class="arrow-link">Explore {sp.get('short', sp['name'])}</span></div>
</a>""")
    return f"""<section class="hero" aria-labelledby="hero-h">
  <div class="wrap">
    <div class="hero-copy">
      <p class="eyebrow">Marketing, communications &amp; organizational leader</p>
      <h1 id="hero-h">I turn audience insight into stronger brands, product growth and organizational impact.</h1>
      <p class="lede">I’m a marketing and communications leader who builds brands, brings products to market and drives measurable growth. Across consumer, enterprise and public-sector organizations, I’ve led strategies, teams and operations that deliver results, while building AI-enabled capabilities that improve how work gets done.</p>
      <div class="btn-row"><a class="btn btn-primary" href="#work">Explore my work</a><a class="btn btn-secondary" href="#contact">Let’s talk</a></div>
    </div>
    <div class="collage" aria-label="Selected project work">
      <figure class="c1">{img(root, C.PROJECTS['delta-campaign']['image'], eager=True)}</figure>
      <figure class="c2"><img src="{root}src/img/greener-life-logo.jpg" alt="Georgia Natural Gas Greener Life logo with green leaf shapes" width="766" height="556" loading="eager" decoding="async"></figure>
      <figure class="c3"><img src="{root}src/img/ms-top-of-mind.jpg" alt="Microsoft FY26 Top of Mind leadership communications banner" width="900" height="421" loading="eager" decoding="async"></figure>
    </div>
  </div>
</section>

<section class="orgs" aria-labelledby="orgs-h">
  <div class="wrap">
    <h2 class="eyebrow" id="orgs-h">Where I’ve made an impact</h2>
    <ul>{orgs}</ul>
  </div>
</section>

<section class="section outcomes" aria-labelledby="outcomes-h">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Selected outcomes</p><h2 id="outcomes-h">Results across brand, product and people</h2></div>
    <ul>{proofs}</ul>
  </div>
</section>

<section class="section" id="work" aria-labelledby="work-h">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">My work</p><h2 id="work-h">Choose an area to explore</h2></div>
    <div class="cards">{''.join(cards)}</div>
  </div>
</section>

<section class="section throughline" aria-labelledby="about-h">
  <div class="wrap">
    <h2 id="about-h">One throughline, four disciplines</h2>
    <div class="copy">
      <p class="lede">Whether I’m building a brand, bringing a product to market or helping employees navigate change, my work starts with understanding people and translating that insight into strategies that drive action and measurable outcomes.</p>
      <p>I’ve led brand, product marketing, communications and operations independently and together—from global companies like Microsoft and Delta Air Lines to the City &amp; County of San Francisco, where I led a multidisciplinary team supporting 20+ services and technology products.</p>
      <a class="arrow-link" href="{href(root, 'about/')}">See my experience and credentials</a>
    </div>
  </div>
</section>"""


def related(root, exclude):
    return "".join(
        f'<a href="{href(root, o["slug"] + "/")}"><strong>{o["name"]}</strong><span>{o["card"]}</span></a>'
        for k, o in C.SPECIALTIES.items() if k != exclude)


def specialty(root, key):
    sp = C.SPECIALTIES[key]
    caps = "".join(f"<li>{c}</li>" for c in sp["capabilities"])
    projects = "".join(project(root, p) for p in sp["projects"])
    note = ""
    if key == "brand":
        note = review('<p class="review" style="margin-top:24px">Across all four pages, “The challenge” and “My role” lines and the “Explore the project” details are new summaries drawn from your current site and master CV. Please check them.</p>')
    return f"""<section class="page-hero" aria-labelledby="page-h">
  <div class="wrap">
    <p class="crumbs"><a href="{href(root, '')}#work">Work</a> / {sp['name']}</p>
    <h1 id="page-h">{sp['name']}</h1>
    <p class="lede">{sp['intro']}</p>
    <ul class="caps" aria-label="Capabilities">{caps}</ul>
  </div>
</section>

<section class="section" style="padding-top:24px" aria-labelledby="featured-h">
  <div class="wrap">
    <div class="section-head"><h2 id="featured-h">Selected projects</h2></div>
    <div class="featured">{projects}</div>
    {note}
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="related-h">
  <div class="wrap">
    <div class="section-head"><h2 id="related-h">Explore other work</h2></div>
    <div class="related">{related(root, key)}</div>
  </div>
</section>"""


def about(root):
    roles = []
    for years, org, title, desc, slugs in C.EXPERIENCE:
        rel = ""
        if slugs:
            rel = '<p class="role-links">Related work: ' + " · ".join(
                f'<a href="{href(root, s + "/")}">{C.SPECIALTIES[s].get("short", C.SPECIALTIES[s]["name"])}</a>' for s in slugs) + "</p>"
        roles.append(f'<li><span class="when">{years}</span><div class="role">{org}<span class="t">{title}</span><p>{desc}</p>{rel}</div></li>')
    # Capabilities lead; tool lists are set smaller so they read as supporting detail.
    tech = "".join(f'<div{"" if i == 0 else " class=\"tool\""}><dt>{t}</dt><dd>{d}</dd></div>'
                   for i, (t, d) in enumerate(C.TECH_ROWS))
    awards = "".join(f'<li><span class="yr">{y}</span>{n}<span>{w}</span></li>' for y, n, w in C.AWARDS)
    edu = "".join(f"<li>{n}{f'<span>{d}</span>' if d else ''}</li>" for n, d in C.EDUCATION)
    return f"""<section class="page-hero" aria-labelledby="page-h">
  <div class="wrap">
    <p class="crumbs"><a href="{href(root, '')}">Home</a> / About</p>
    <h1 id="page-h">About &amp; experience</h1>
    <p class="lede">{C.ABOUT_INTRO}</p>
    {review('<p class="review">The introduction above is new copy for your review. Everything else on this page comes from your current site.</p>')}
    <ul class="caps jump" aria-label="On this page"><li><a href="#experience">Experience</a></li><li><a href="#technology-ai">Technology &amp; AI</a></li><li><a href="#credentials">Recognition &amp; credentials</a></li></ul>
  </div>
</section>

<section class="section split" id="experience" aria-labelledby="exp-h" style="padding-top:24px">
  <div class="wrap">
    <div class="split-head"><p class="eyebrow">Experience</p><h2 id="exp-h">Experience across industries and borders</h2><p>Global companies and mission-driven organizations, in the US and abroad.</p></div>
    <ol class="roles">{''.join(roles)}</ol>
  </div>
</section>

<section class="section split tech" id="technology-ai" aria-labelledby="tech-h">
  <div class="wrap">
    <div class="split-head"><p class="eyebrow">Technology &amp; AI</p><h2 id="tech-h">Technology &amp; AI capabilities</h2><p>{C.TECH_INTRO}</p></div>
    <div class="tech-body"><p class="tech-capability">{C.TECH_CAPABILITY}</p><dl class="tech-rows">{tech}</dl></div>
  </div>
</section>

<section class="section" id="credentials" aria-labelledby="cred-h">
  <div class="wrap">
    <div class="section-head"><p class="eyebrow">Recognition &amp; credentials</p><h2 id="cred-h">Awards, education and languages</h2></div>
    <div class="cred-grid">
      <div><h3>Awards</h3><ul>{awards}</ul></div>
      <div class="stack">
        <div><h3>Education &amp; certification</h3><ul>{edu}</ul></div>
        <div><h3>Languages</h3><ul><li>{C.LANGUAGES}</li></ul></div>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="related-h">
  <div class="wrap">
    <div class="section-head"><h2 id="related-h">Explore my work</h2></div>
    <div class="related four">{related(root, None)}</div>
  </div>
</section>"""


def write(path, html):
    if not PREVIEW:
        html = REVIEW_BLOCK.sub("", html)
        assert "REVIEW" not in html, "unbalanced review markers"
    target = OUT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html)


if PREVIEW and OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "assets").mkdir(exist_ok=True)
shutil.copy(ROOT / "src" / "site.css", OUT / "assets" / "site.css")
shutil.copy(ROOT / "src" / "site.js", OUT / "assets" / "site.js")
if PREVIEW:
    shutil.copytree(ROOT / "src" / "img", OUT / "src" / "img")

home_title = "Asia Meshack | Marketing, Communications & Organizational Leader"
home_desc = ("Asia Meshack is a marketing and communications leader across brand, product marketing, "
             "internal and executive communications, and leadership and operations.")
write("index.html", document("", "home", home_title, home_desc, "", home("")))
if PREVIEW:
    # The artifact viewer wraps its main page in a document of its own.
    write("artifact-home.html", document("", "home", "Asia Meshack Redesign", home_desc, "", home(""), fragment=True))

for key, sp in C.SPECIALTIES.items():
    title = f"{sp['title'].capitalize()} | Asia Meshack"
    write(f"{key}/index.html", document("../", key, title, sp["description"], key + "/", specialty("../", key)))
write("about/index.html", document("../", "about", "About and experience | Asia Meshack",
                                   "Experience, technology and AI capabilities, awards and education of Asia Meshack.",
                                   "about/", about("../")))

print(f"Built {'preview in dist/preview' if PREVIEW else 'site'}: home, "
      f"{', '.join(C.SPECIALTIES)}, about")
