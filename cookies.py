
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s=Service("D:\\python\\chromedriver.exe")

driver=webdriver.Chrome(service=s)




driver.maximize_window()
click_time=time.time()
LOOP_DURATION =5
# driver.get to open the mention website
driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie_anchor = driver.find_element("id","bigCookie")
cookie_anchor.click()
cookie_anchor.click()
cookie_anchor.click()

k=0
count=0
for i in range(2000):
    cookie_anchor.click()

    try:
        price_cookie = int(driver.find_element("id","cookies").text.split(" ")[0].replace(",",""))

    except:
        price_cookie = int(driver.find_element("id","cookies").text.split(" ")[0])

    try:
        pro_price = int(driver.find_element("id",f"productPrice{k}").text.split(" ")[0].replace(",", ""))
    except:
        pro_price = int(driver.find_element("id",f"productPrice{k}").text.split(" ")[0])

    print(price_cookie)
    if click_time>=LOOP_DURATION:
            if price_cookie>pro_price:
                click_1=driver.find_element("id",f"product{k}")
                LOOP_DURATION+=100
                click_1.click()
                k+=1
            else:
                count+=1
                if count>300:
                    count=0
                    k=0
                else:
                    pass

    else:
        click_1 = driver.find_element_by_id(f"product{k}")
        click_1.click()
        click_time+=20*k
        k+=1




driver.quit()