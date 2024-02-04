from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os
import itertools
from selenium.webdriver.common.by import By


os.environ['PATH'] += r"C:\Program Files (x86)\chrome-win64"
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)

link = driver.find_element(By.ID, "langSelect-EN")
link.click()
driver.implicitly_wait(5)
#action_chain.move_to_element(element).click().perform()


cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)

for i in itertools.count():
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
