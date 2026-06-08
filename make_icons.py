import sys, os
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

svg_path = r'c:/Users/Picay/Calculadora kg/icon.svg'
out_dir  = r'c:/Users/Picay/Calculadora kg'

svg_url = 'file:///' + svg_path.replace('\\', '/').replace(' ', '%20')

html = f"""<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<style>
  * {{ margin: 0; padding: 0; }}
  body {{ background: transparent; width: 100vw; height: 100vh; overflow: hidden; }}
  img {{ display: block; width: 100%; height: 100%; object-fit: contain; }}
</style>
</head><body>
<img src="{svg_url}">
</body></html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    for size in [192, 512]:
        page = browser.new_page(viewport={'width': size, 'height': size})
        page.set_content(html)
        page.wait_for_timeout(800)
        page.screenshot(
            path=f'{out_dir}/icon-{size}.png',
            clip={'x': 0, 'y': 0, 'width': size, 'height': size},
            omit_background=True
        )
        print(f'icon-{size}.png creado')
    browser.close()
