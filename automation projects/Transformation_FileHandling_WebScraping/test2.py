from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument('--disable-blink-features=AutomationControlled')
i = 0
driver = webdriver.Chrome()


delay = 10
y = 0
elements = []
for i in range(1, 16):
    driver.get(f"https://www.justdial.com/Delhi/Ceiling-Tile-Dealers-Armstrong/nct-11271379/page-{i}")
    for timer in range(0, 10):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 200
        time.sleep(2)
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'jdresult_box')))
            print("Page is ready!")
        except TimeoutException:
            print("Loading took too much time!")
            break
    shops = driver.find_elements(By.CLASS_NAME, 'resultbox_info')
    elements.append(shops)
    print(len(elements))

