# https://sites.google.com/a/chromium.org/chromedriver/downloads
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv

os.environ['PATH'] += r"C:\Program Files (x86)\chrome-win64"

driver = webdriver.Chrome()
# in the get method we can use or any website name
time.sleep(1)
driver.get("https://www.google.com/maps/place/Bhubaneswar,+Odisha/@20.300807,85.6556413,11z/data=!3m1!4b1!4m6!3m5!1s0x3a1909d2d5170aa5:0xfc580e2b68b33fa8!8m2!3d20.2960587!4d85.8245398!16zL20vMDNjenFz?entry=ttu")
print(driver.title)
time.sleep(5)
#print(driver.page_source)

search = driver.find_element(By.CLASS_NAME, "maps-landing")
print(search)
#link = driver.find_element(By.LINK_TEXT,"Nearby")
#link.click()
# search.send_keys("All")
# search.send_keys(Keys.RETURN)
#try:
   # element = WebDriverWait(driver, 10).until(
       # EC.presence_of_element_located((By.LINK_TEXT, "maps-landing"))
    #)
    #element.click()
    #element = WebDriverWait(driver, 10).until(
        # enter the adress of butten element to prees the button
       # EC.presence_of_element_located((By.CLASS_NAME, "maps-landing"))
    #)
   # element.click()
    # always click a link or button element

   # driver.back()
    # driver back funtion is to back the our task or what we done in the url
   # driver.forward()
    # is to go forward in the url
    # for nagigate in the url and click which think we want

    # in place of body we can write the name of tag name
    #iframe = main.find_element(By.TAG_NAME, "iframe")
    #for iframe in iframe:
     #   header = iframe.find_element(By.ID, "hfcr")
      #  print(header.text)
#finally:
   # driver.quit()
# main = driver.find_element(By.ID, "main")

#print(main.text)
#print(driver.page_source)
# driver.close()