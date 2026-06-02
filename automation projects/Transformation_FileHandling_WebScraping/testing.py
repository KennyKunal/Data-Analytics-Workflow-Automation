from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get('https://www.justdial.com/Delhi/Ceiling-Tile-Dealers-Armstrong/nct-11271379')
y = 0
for i in range(1,200):
    print(i)
    try:
        for timer in range(0, 2):
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 50
            time.sleep(1)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.jsx-98ac5e1b53154d9c')))
        name = driver.find_element(By.XPATH,f'/html/body/div/section/section/div/div[5]/div[1]/div/div[1]/div[{i}]/div/div/div[2]/h2/a').text
        address = driver.find_element(By.XPATH, f'/html/body/div/section/section/div/div[5]/div[1]/div/div[1]/div[{i}]/div/div/div[2]/h2/a/div[2]').text
        try:
            ph_number = driver.find_element(By.XPATH, f'/html/body/div/section/section/div/div[5]/div[1]/div/div[1]/div[{i}]/div/div/div[2]/div[5]/div[1]/div[1]/div')
        except:
            ph_number = driver.find_element(By.XPATH,f'/html/body/div/section/section/div/div[5]/div[1]/div/div[1]/div[{i}]/div/div/div[2]/div[4]/div[1]/div[1]/div/span')
        if ph_number.text == 'Show Number':
            ph_number.click()
            phone_number = ph_number.text
        else:
            phone_number = ph_number.text
        rating = driver.find_element(By.XPATH,f'/html/body/div/section/section/div/div[5]/div[1]/div/div[1]/div[{i}]/div/div/div[2]/div[2]/div[1]').text
        image_url = driver.find_element(By.XPATH, f'/html/body/div/section/section/div/div[5]/div[1]/div/div[1]/div[{i}]/div/div/div[1]/a/div[1]/div[1]/span/img').get_attribute('src')
        image_alt = driver.find_element(By.XPATH, f'/html/body/div/section/section/div/div[5]/div[1]/div/div[1]/div[{i}]/div/div/div[1]/a/div[1]/div[1]/span/img').get_attribute('alt')
        name_link = driver.find_element(By.XPATH, f'/html/body/div/section/section/div/div[5]/div[1]/div/div[1]/div[{i}]/div/div/div[2]/h2/a').get_attribute('href')
        try:
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 250
            time.sleep(0.1)
        except:
            pass
        print(f'name: {name} address: {address} \n phone_number: {phone_number} rating: {rating} \n img_url: {image_url}')
        print(f'img_alt: {image_alt} \n name_link: {name_link}')
    except:
        pass

By.TAG_NAME