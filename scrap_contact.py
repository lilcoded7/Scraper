from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DataBase import DB  # Import your DB module here
import time

def get_contact_value(driver):
    return driver.find_element(By.ID, 'phone').get_attribute('value')

def scraper():
    driver = webdriver.Chrome()
    try:
        driver.get('https://www.zhilepin.com/site/hunter-regist.html')
        country_code_input = driver.find_element(By.ID, 'countryCode')
        contact_input = driver.find_element(By.ID, 'phone')
        country_code_input.send_keys('')
        contact_input.send_keys('')
        submit_button = driver.find_element(By.CLASS_NAME, 'cursor')
        submit_button.click()
        wait = WebDriverWait(driver, 999)
        country_code = wait.until(EC.presence_of_element_located((By.ID, 'countryCode'))).get_attribute('value')
        while True:
            contact = get_contact_value(driver)
            if contact.strip():
                DB('phonenumbers').insert_data(country_code.strip(), contact.strip())
                print('Country Code:', country_code.strip())
                print('Contact:', contact.strip())
            time.sleep(5)
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

scraper()
