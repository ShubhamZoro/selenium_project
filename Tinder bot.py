import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
email_="shubhamshekhar19@gmail.com"
password_=''
driver_path="D:\python\chromedriver.exe"
driver=webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get(url="https://tinder.com/")
log_in=driver.find_element_by_xpath('//*[@id="s-138260025"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()
time.sleep(2)
try:
    more_option=driver.find_element_by_xpath('//*[@id="s-1866641101"]/div/div/div[1]/div/div[3]/span/button')
    time.sleep(2)
    more_option.click()
except:
    More_option = driver.find_element_by_xpath('//*[@id="s-1866641101"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')

else:
    More_option = driver.find_element_by_xpath('//*[@id="s-1866641101"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
More_option.click()
time.sleep(2)
base_window = driver.window_handles[0]
# fb_login_window = driver.window_handles[1]
driver.switch_to.window(base_window)
print(driver.title)
# email=driver.find_element_by_id("email")
# email.send_keys(email_)
# password=driver.find_element_by_name("pass")
# password.send_keys(password_)
# password.send_keys(Keys.ENTER)
# time.sleep(2)
# driver.switch_to.window(base_window)
# print(driver.title)
# time.sleep(3)
# allow=driver.find_element_by_xpath('//*[@id="s-1866641101"]/div/div/div/div/div[3]/button[1]')
# allow.click()
# notification=driver.find_element_by_xpath('//*[@id="s-1866641101"]/div/div/div/div/div[3]/button[2]')
# notification.click()
# accept=driver.find_element_by_xpath('//*[@id="s-138260025"]/div/div[2]/div/div/div[1]/button')
# accept.click()
# time.sleep(5)
# for i in range(50):
#     like=driver.find_element_by_xpath('//*[@id="s-138260025"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span/svg')
#     like.click()
#     time.sleep(3)