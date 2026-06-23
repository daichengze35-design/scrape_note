from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
time.sleep(5)
driver.implicitly_wait(5)

driver.switch_to.frame("iframeResult")
item = driver.find_element(By.XPATH, "/html/body/div[2]")
action = ActionChains(driver)
action.click_and_hold(item)
action.move_by_offset(250,0).perform()
time.sleep(0.5)
action.release(item).perform()
time.sleep(1)
driver.switch_to.alert.accept()

time.sleep(5)
driver.quit()