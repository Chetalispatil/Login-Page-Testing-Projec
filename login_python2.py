from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()  # Opens a Chrome browser window

# Open your HTML login form
driver.get("file:///D:/python/project/login%20project/login.html") 

driver.get("file:///C:/Users/Chetali/Desktop/login.html")
driver.find_element(By.ID, "username").send_keys("john")
driver.find_element(By.ID, "password").send_keys("wrongpass")
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
             

# Pause to observe result (the alert)
time.sleep(2)

# Close the browser
driver.quit()
