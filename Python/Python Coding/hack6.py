#!/usr/bin/python
from selenium import webdriver
import time 

driver = webdriver.Chrome()
driver.get("https://Jamildababneh.com")
searchbox = driver.find_element_by_xpath ('//*[@id="topNav"]/nav/div/ul/li[7]/a/span')
time.sleep(3)
searchbox.click()
txt = "Hello"
txt = txt.reverse()
print(txt)
