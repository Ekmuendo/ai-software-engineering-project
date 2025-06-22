from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize browser
driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Valid login
driver.find_element(By.ID, "username").send_keys("evans")
driver.find_element(By.ID, "password").send_keys("validpass")
driver.find_element(By.ID, "login-btn").click()
time.sleep(2)
print("✅ Valid login test passed." if "dashboard" in driver.current_url else "❌ Failed")

# Invalid login
driver.get("https://example.com/login")
driver.find_element(By.ID, "username").send_keys("evans")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.ID, "login-btn").click()
time.sleep(2)
print("✅ Invalid login test passed." if "error" in driver.page_source else "❌ Failed")

driver.quit()
