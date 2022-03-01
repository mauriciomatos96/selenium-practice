from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/pro-02-001/Documents/chrome driver/chromedriver"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get("http://secure-retreat-92358.herokuapp.com/")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# all_portal = driver.find_element(By.LINK_TEXT, "All portals")
# all_portal.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

name_field = driver.find_element(By.NAME, "fName")
name_field.send_keys("Mauricio")
last_name_field = driver.find_element(By.NAME, "lName")
last_name_field.send_keys("Matos")
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("mauriciomatos44@gmail.com")
sign_up_button = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up_button.click()