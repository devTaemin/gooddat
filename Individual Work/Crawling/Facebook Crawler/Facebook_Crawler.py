from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

usr = "Type facebook ID"
pwd = "Type facebook PW"

path = '/Users/cross/Downloads/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN) 
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

a = driver.find_element_by_xpath('//*[@id="userNavigationLabel"]')
a.click()
b = driver.find_element_by_xpath("//*[contains(text(), 'js')]")
b.click()


#b = driver.find_element_by_xpath('//*[contains(@id, "js")]/div/div/ul/li[5]/a/span/span/div/div[1]')
#b.click()
"""
try:
    element = WebDriverWait(driver,10).until(
         EC.presence_of_element_located((By.CLASS_NAME, "lfloat _ohe")))
    b = driver.find_element_by_xpath('//*[contains(@id, "js")]/div/div/ul/li[5]/a/span/span/div/div[1]')
    b.click()
except TimeoutException:
    print("Failed to load search bar at www.google.com")
"""