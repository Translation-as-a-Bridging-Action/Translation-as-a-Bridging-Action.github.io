"""Bundle the project page into a single self-contained HTML file.

Inlines CSS, JS, images (as compressed JPEG data URIs) and videos (as base64
data URIs) so the resulting ``Cam3D_ProjectPage.html`` can be opened offline by
double-clicking, with no local server required.

Usage:
    python3 build_standalone.py
"""

import base64
import io
import os
import re

from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "Cam3D_ProjectPage.html")

MAX_W = 1700      # downscale very large figures for sharing
JPEG_Q = 85

with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
    html = f.read()

# Inline CSS
with open(os.path.join(ROOT, "static/css/style.css"), encoding="utf-8") as f:
    css = f.read()
html = html.replace(
    '<link rel="stylesheet" href="static/css/style.css">',
    "<style>\n" + css + "\n</style>",
)

# Inline JS
with open(os.path.join(ROOT, "static/js/main.js"), encoding="utf-8") as f:
    js = f.read()
html = html.replace(
    '<script src="static/js/main.js"></script>',
    "<script>\n" + js + "\n</script>",
)


def to_data_uri(path):
    img = Image.open(path)
    if img.width > MAX_W:
        h = round(img.height * MAX_W / img.width)
        img = img.resize((MAX_W, h), Image.LANCZOS)
    # Flatten onto white and encode as JPEG (figures all have white backgrounds)
    if img.mode in ("RGBA", "P", "LA"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[-1])
        img = bg
    else:
        img = img.convert("RGB")
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=JPEG_Q, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"


def repl_img(match):
    src = match.group(1)
    full = os.path.join(ROOT, src)
    if os.path.exists(full):
        return 'src="' + to_data_uri(full) + '"'
    print("WARN missing", full)
    return match.group(0)


html = re.sub(r'src="(static/images/[^"]+)"', repl_img, html)


def repl_video(match):
    src = match.group(1)
    full = os.path.join(ROOT, src)
    if os.path.exists(full):
        with open(full, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode("ascii")
        return 'src="data:video/mp4;base64,' + b64 + '"'
    print("WARN missing", full)
    return match.group(0)


html = re.sub(r'src="((?:mp4|mp4_hand|mp4_action_bridge_vis)/[^"]+\.mp4)"', repl_video, html)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

size_mb = os.path.getsize(OUT) / (1024 * 1024)
print(f"wrote {OUT}  ({size_mb:.1f} MB)")
