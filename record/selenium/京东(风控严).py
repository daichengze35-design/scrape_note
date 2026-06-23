from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

jd = webdriver.Chrome()

jd.get('https://www.jd.com/')
sleep(5)
jd.implicitly_wait(7)
jd.find_element(By.XPATH,'//*[@id="login2025-dialog-close"]').click()
sleep(10)
jd.find_element(By.XPATH,'/html/body/div[9]/div/div/div[1]').click()
sleep(5)
jd.find_element(By.XPATH,'//*[@id="search"]/div[2]/div[2]/div/div/div[1]/input').click()
sleep(3)
jd.find_element(By.XPATH,'//*[@id="search"]/div[2]/div[2]/div/div/div[1]/input').send_keys('mac pro m1')
sleep(2)
# btn = jd.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
btn = jd.find_element(By.XPATH,'//*[@id="search"]/div/div[2]/button')

btn.click() #点击按钮
sleep(2)
#js注入
jd.execute_script('document.documentElement.scrollTo(0,2000)')
sleep(5)
#关闭浏览器
jd.quit()
