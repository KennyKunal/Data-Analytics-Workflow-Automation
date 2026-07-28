#https://www.bigbasket.com/ps/?q=milk

import re, time
from playwright.sync_api import Playwright, sync_playwright, expect

'''
milks
curd & yoghurt
panner & tofu
'''

#https://www.bigbasket.com/ps/?q=curd 
#https://www.bigbasket.com/ps/?q=milk
#https://www.bigbasket.com/ps/?q=paneer
#https://www.bigbasket.com/ps/?q=tofu
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.bigbasket.com/ps/?q=Yoghurt")
    time.sleep(2)

    parent_prod = page.locator(".bFjDCO")

    products = []

    for i in range(parent_prod.count()):
        card = parent_prod.nth(i)

        brand = card.locator(".gGuxrf").inner_text()
        product = card.locator(".h-10.w-full").inner_text()
        quantity = card.locator(".py-1\\.5.xl\\:py-1").inner_text()
        try:
            price = card.locator(".jnBJRV.hpkXHR").inner_text()
        except:
            price = 'N/A'
        products.append({
            "brand": brand,
            "product": product,
            "quantity": quantity,
            "price": price,
            "category": "Milk",
            "source": "BigBasket"
        })

    print(products)
    print(len(products))


    # brands = page.locator('.gGuxrf').all_inner_texts()
    # products = page.locator('.h-10.w-full').all_inner_texts()
    # quantity = page.locator(".py-1\\.5.xl\\:py-1").all_inner_texts()
    # price = page.locator(".jnBJRV.hpkXHR").all_inner_texts()
    # print(brands)
    
    # print(products)
    
    # print(quantity)
    # print(price)
    # print(len(brands))
    # print(len(products))
    # print(len(quantity))
    # print(len(price))

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
