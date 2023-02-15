from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


driver.get("http://uitestingplayground.com/dynamicid")

serch_locator = "button[id=b1cd0c23-fc87-e998-28f4-3d8d0e58e83a]"

serch_input = driver.find_element(By.CSS_SELECTOR, serch_locator)

serch_input.send_keys("Python")
serch_input.send_keys(Keys.RETURN)

sleep(50)

driver.quit()