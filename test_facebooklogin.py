from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(1)
driver.find_element_by_name("email").send_keys("utkarshsontakke123@gmail.com")
driver.find_element_by_name("pass").send_keys("xyz")
time.sleep(2)
driver.find_element_by_name("login").click()
time.sleep(5)
driver.close()
print("Test case has successfully completed")

