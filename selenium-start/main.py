from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/home/pro-02-001/Documents/chrome driver/chromedriver"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")

events_date = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(events_date)):
    events[n] = {
        "time": events_date[n].text,
        "name": events_name[n].text
    }


print(events)