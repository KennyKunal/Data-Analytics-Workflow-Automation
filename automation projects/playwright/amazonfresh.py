import time
from playwright.sync_api import sync_playwright, Playwright

URL = "https://www.amazon.in/alm/category?_encoding=UTF8&almBrandId=ctnow&node=16984555031&ref_=cct_cg_sfz2s1tr_3a1"

CATEGORIES = {
    "Milk": "#x4859603031",
    "Curd & Yoghurt": "#x4859611031",
    "Paneer & Tofu": "#x17477539031"
}


def scroll_to_bottom(page):
    previous_height = 0

    while True:
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(2000)

        current_height = page.evaluate("document.body.scrollHeight")

        if current_height == previous_height:
            break

        previous_height = current_height

    print("Finished scrolling")


def extract_products(page, category):
    data = page.locator(".a-offscreen").all_inner_texts()

    products = []
    i = 0

    while i < len(data):
        # Product name
        name = data[i]
        i += 1

        # Quantity
        if i < len(data) and not data[i].startswith("₹"):
            quantity = data[i]
            i += 1
        else:
            quantity = "N/A"

        # Price
        if i < len(data) and data[i].startswith("₹"):
            price = data[i]
            i += 1
        else:
            price = "N/A"

        products.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "category": category,
            "source": "Amazon Fresh"
        })

    return products


def scrape_category(page, category_name, selector):
    print(f"\nScraping {category_name}...")

    page.goto(URL)
    page.wait_for_load_state("networkidle")

    page.locator(selector).click()
    page.wait_for_timeout(2000)

    scroll_to_bottom(page)

    return extract_products(page, category_name)


def run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    all_products = []

    for category, selector in CATEGORIES.items():
        products = scrape_category(page, category, selector)

        print(f"{len(products)} products found.")

        all_products.extend(products)

    print("\nTotal Products:", len(all_products))

    for product in all_products:
        print(product)

    time.sleep(10)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)