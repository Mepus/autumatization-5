from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


driver.get("http://uitestingplayground.com/classattr")

serch_locator = "button.btn.class2.btn-primary.btn-test"
serch_input = driver.find_element(By.CSS_SELECTOR, serch_locator)

serch_input.send_keys(Keys.RETURN)

sleep(50)

driver.quit()