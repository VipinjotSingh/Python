from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://google.com/")
#browser.maximize_window()
#assert 'Google' in browser.title

#WebDriverWait(browser, 10).until(
    #EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
#)

elem = browser.find_element(By.CLASS_NAME, "gLFyf")# Find the search box
elem.clear()
elem.send_keys("Cookie Clicker" + Keys.RETURN)

Link = browser.find_element(By.PARTIAL_LINK_TEXT, "Cookie Clicker")
Link.click()
 
#browser.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"
#cookie = browser.find_element(By.XPATH, "//button[@id='bigCookie']")
WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='langSelect-EN']"))
)
language = browser.find_element(By.XPATH, "//div[@id='langSelect-EN']")
language.click()

WebDriverWait(browser, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)
cookie = browser.find_element(By.ID, cookie_id)
cookie.click()
#browser.implicitly_wait(100)

while True:
    cookie.click()
    cookies_count = browser.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",",""))
    print(cookies_count)
    
    for i in range(4):
        product_price = browser.find_element(By.ID, product_price_prefix +str(i)).text.replace(",","")
        if not product_price.isdigit():
            continue
        
        product_price = int(product_price.replace(",",""))
    
        if cookies_count >= product_price:
            product = browser.find_element(By.ID, product_prefix + str(i))
            product.click()
            break