"""Build the site: inline images into src/page.html.

Writes:
  index.html          standalone page served by GitHub Pages
  dist/artifact.html  body-only version for the Claude artifact
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
IMAGES = {
    "{{CAP}}": "climate-action.jpg",
    "{{GASSY}}": "gassy.jpg",
    "{{BATTERY}}": "battery.jpg",
    "{{SFR}}": "sfrecycles.jpg",
    "{{EASF}}": "energyaccess.jpg",
    "{{ERH}}": "erh.jpg",
    "{{REUSE}}": "reuse.jpg",
    "{{GREENER}}": "greener-life.jpg",
}

page = (ROOT / "src" / "page.html").read_text()
for token, name in IMAGES.items():
    data = base64.b64encode((ROOT / "src" / "img" / name).read_bytes()).decode()
    page = page.replace(token, "data:image/jpeg;base64," + data)
assert "{{" not in page, "unreplaced image placeholder"

(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "artifact.html").write_text(page)

split = page.index("</style>") + len("</style>")
standalone = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
    "<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
    + page[:split] + "\n</head>\n<body>\n" + page[split:] + "\n</body>\n</html>\n"
)
(ROOT / "index.html").write_text(standalone)
print("Built index.html and dist/artifact.html")
