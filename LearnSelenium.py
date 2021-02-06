from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://cdcwviafapvd01/AMIGA")
assert "AMIGA" in driver.title
elem = driver.find_element_by_xpath("//html/body/div[1]/amiga-app/div/nav/div/ul/li[1]/a")
elem.click()
srchbtn=driver.find_element_by_id("rdCustSearch")
# select_srchbtn=Select(srchbtn)
srchbtn.click()
last_name = driver.find_element_by_id("txtLastName")
last_name.send_keys("SMITH")
submit_btn = driver.find_element_by_id("btnSearch")
submit_btn.click()
# elem = driver.find_element_by_xpath("//html/body/div/amiga-app/div/nav/div/ul/li[2]")
# # elem.clear()
# elem.click()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# elem.send_keys()
# assert "No results found." not in driver.page_source
# driver.close()