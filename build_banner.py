"""Embeds the Luffy Gear 5 GIF into assets/banner.svg as an animated background.

Usage (run inside this folder):
    python build_banner.py                       # downloads the default GIF
    python build_banner.py path/to/luffy.gif     # or use a local file
"""
import base64, sys, urllib.request

URL = "https://www.gifcen.com/wp-content/uploads/2024/04/luffy-gear-5-4.gif"

if len(sys.argv) > 1:
    data = open(sys.argv[1], "rb").read()
else:
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req).read()

print(f"GIF size: {len(data)/1024:.0f} KB")
if len(data) > 4 * 1024 * 1024:
    print("Warning: over 4 MB, the banner may load slowly. Try a smaller GIF.")

b64 = base64.b64encode(data).decode()
tag = ('<image href="data:image/gif;base64,%s" x="0" y="-150" width="1000" '
       'height="560" preserveAspectRatio="xMidYMid slice" opacity="0.75"/>' % b64)

svg = open("assets/banner_template.svg", encoding="utf-8").read().replace("{{GIF}}", tag)
open("assets/banner.svg", "w", encoding="utf-8").write(svg)
print("Done -> assets/banner.svg")
