
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC
driver_path_chrome = SC(os.getcwd() + '\drivers\chromedriver.exe')
driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')


driver = webdriver.Firefox(service=driver_path_firefox)




url = 'https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html'
driver.get(url)
q1_full_xpath='/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'
q1 = driver.find_element('xpath', q1_full_xpath)
q1.send_keys('some')











