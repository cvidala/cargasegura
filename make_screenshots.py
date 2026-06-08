import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

URL     = 'https://cvidala.github.io/cargasegura/'
OUT_DIR = r'c:/Users/Picay/Calculadora kg'

# Play Store pide min 1080x1920 o 1080x2340 portrait
VIEWPORT = {'width': 390, 'height': 844}   # iPhone 14 logical
SCALE    = 3                                 # device pixel ratio -> 1170x2532

with sync_playwright() as p:
    browser = p.chromium.launch()

    # Screenshot 1: vista "Mi Carga" vacía (pantalla principal)
    page = browser.new_page(
        viewport=VIEWPORT,
        device_scale_factor=SCALE,
        is_mobile=True,
        has_touch=True
    )
    page.goto(URL, wait_until='networkidle', timeout=30000)
    page.wait_for_timeout(1500)
    page.screenshot(path=f'{OUT_DIR}/screenshot-1.png', full_page=False)
    print('screenshot-1.png  (Mi Carga vacía)')

    # Screenshot 2: carga con materiales agregados
    # Agregar 3 sacos cemento + 2 volcanitas vía UI
    page.goto(URL, wait_until='networkidle', timeout=30000)
    page.wait_for_timeout(1000)

    # Ir a categoría Sacos
    page.locator('button.category-tab[data-category="sacos"]').click()
    page.wait_for_timeout(400)
    # Agregar 3 sacos cemento 25kg
    for _ in range(3):
        page.locator('button[onclick*="saco_cemento_25kg"][aria-label*="Aumentar"]').click()
        page.wait_for_timeout(150)

    # Ir a Planchas
    page.locator('button.category-tab[data-category="planchas"]').click()
    page.wait_for_timeout(400)
    # Agregar 2 volcanitas
    for _ in range(2):
        page.locator('button[onclick*="volcanita_10mm"][aria-label*="Aumentar"]').click()
        page.wait_for_timeout(150)

    # Volver a Mi Carga
    page.locator('button.category-tab[data-category="mi-carga"]').click()
    page.wait_for_timeout(600)
    page.screenshot(path=f'{OUT_DIR}/screenshot-2.png', full_page=False)
    print('screenshot-2.png  (Mi Carga con materiales)')

    # Screenshot 3: buscador en acción
    page.locator('#search-input').fill('fierro')
    page.wait_for_timeout(500)
    page.screenshot(path=f'{OUT_DIR}/screenshot-3.png', full_page=False)
    print('screenshot-3.png  (Búsqueda "fierro")')

    browser.close()

print('Listo.')
