from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scraper():
    driver = webdriver.Chrome()
    driver.get('https://www.zhilepin.com/site/hunter-regist.html')
    country_code_input = driver.find_element(By.ID, 'countryCode')
    contact_input = driver.find_element(By.ID, 'phone')
    country_code_input.send_keys('')
    contact_input.send_keys('')
    submit_button = driver.find_element(By.CLASS_NAME, 'cursor')
    submit_button.click()
    wait = WebDriverWait(driver, 630000)
    country_code = country_code_input.get_attribute('value')
    contact = contact_input.get_attribute('value')
    
    print('Country Code:', country_code.strip())
    print('Contact:', contact.strip())
    driver.quit()


scraper()