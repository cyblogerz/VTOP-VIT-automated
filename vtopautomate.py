from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

PATH="C:\Program Files (x86)\chromedriver"

driver=webdriver.Chrome(PATH)
driver.get("https://vtop.vitbhopal.ac.in/vtop/")
vtop=driver.find_element_by_class_name("btn-primary")
vtop.click()

driver.implicitly_wait(5)
user_input=driver.find_element_by_name("uname")
pass_input=driver.find_element_by_name("passwd")
user_input.send_keys("username")#enter username
pass_input.send_keys("pass")#enter password

bt_submit = driver.find_element_by_id("captcha")

# wait for the user to click the submit button (check every 1s with a 1000s timeout)
WebDriverWait(driver, timeout=1000, poll_frequency=1) \
  .until(EC.staleness_of(bt_submit))

print("signed in")
driver.implicitly_wait(5)
select=driver.find_element_by_xpath('.//span[@class = "fa fa-graduation-cap"]')
select.click()
select=driver.find_element_by_link_text('Time Table')#replace timetable with the thing you need
select.click()


