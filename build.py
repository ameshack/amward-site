"""Build the site from src/page.html.

Writes:
  index.html          published page (owner-review notes removed)
  review.html         review version with owner-review notes visible
  dist/artifact.html  review version with images inlined, for the Claude artifact

Owner-review notes are wrapped in <!--REVIEW--> ... <!--/REVIEW--> in the source.
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
IMAGES = {
    "{{REUSE}}": "reuse.jpg",
    "{{CAP}}": "climate-action.jpg",
    "{{GREENER}}": "greener-life.jpg",
    "{{SFR}}": "sfrecycles.jpg",
}
RESUME = "AM_Ward_Resume.pdf"
REVIEW_BLOCK = re.compile(r"\s*<!--REVIEW-->.*?<!--/REVIEW-->", re.S)


def fill_images(page, inline):
    for token, name in IMAGES.items():
        path = ROOT / "src" / "img" / name
        if inline:
            src = "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()
        else:
            src = "src/img/" + name
        page = page.replace(token, src)
    assert "{{" not in page, "unreplaced image placeholder"
    return page


def standalone(page):
    split = page.index("</style>") + len("</style>")
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        "<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
        + page[:split] + "\n</head>\n<body>\n" + page[split:] + "\n</body>\n</html>\n"
    )


source = (ROOT / "src" / "page.html").read_text()
final = REVIEW_BLOCK.sub("", source)
assert "REVIEW" not in final, "unbalanced review markers"

(ROOT / "index.html").write_text(standalone(fill_images(final, inline=False)))
(ROOT / "review.html").write_text(standalone(fill_images(source, inline=False)))
(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "artifact.html").write_text(fill_images(source, inline=True))

print("Built index.html, review.html and dist/artifact.html")
if not (ROOT / RESUME).exists():
    print(f"WARNING: {RESUME} is missing; the Download resume button will not work until it is added.")
