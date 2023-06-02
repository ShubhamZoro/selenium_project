from selenium import webdriver
import time
email="s9905020863@gmail.com"
password=""
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
driver_path="D:\python\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)
driver.get(url="https://www.linkedin.com/jobs/search/?geoId=102713980&keywords=Python%20Developer")

driver.maximize_window()
sign_in=driver.find_element_by_link_text("Sign in")
sign_in.click()
time.sleep(7)
email_=driver.find_element_by_id("username")
email_.send_keys(email)
time.sleep(4)
password_=driver.find_element_by_id("password")
password_.send_keys(password)
sign_in_=driver.find_element_by_tag_name("button")
sign_in_.click()
# jobs=driver.find_element_by_xpath("Jobs")
# jobs.click()


time.sleep(2)


apply_button=driver.find_element_by_css_selector(".jobs-save-button")

apply_button.click()









