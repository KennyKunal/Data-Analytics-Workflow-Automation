import re, time
from playwright.sync_api import Playwright, sync_playwright, expect

'''
milks
curd & yoghurt
panner & tofu
'''
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.in/alm/category?_encoding=UTF8&almBrandId=ctnow&node=16984555031&ref_=cct_cg_sfz2s1tr_3a1")
    time.sleep(2)
    page.locator('#x17477539031').click()
    time.sleep(2)
    previous_height = 0

    # scrolling to fetch all data 
    while True:
        # Scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # Wait for new content to load
        page.wait_for_timeout(2000)

        # Get new page height
        current_height = page.evaluate("document.body.scrollHeight")

        if current_height == previous_height:
            break

        previous_height = current_height

    print("Finished scrolling")


    # data extractor
    data = page.locator('.a-offscreen').all_inner_texts()
    # print(elem_text)

    # data validation 
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
            "price": price
        })
    print(products)

    time.sleep(30)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
