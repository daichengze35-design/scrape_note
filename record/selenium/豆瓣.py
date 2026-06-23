from time import sleep
from selenium import webdriver
from lxml import etree

driver = webdriver.Chrome()

driver.get('https://movie.douban.com/typerank?type_name=%E6%82%AC%E7%96%91&type=10&interval_id=100:90&action=')
sleep(2)
driver.execute_script('document.documentElement.scrollTo(0,2000)')
sleep(2)
#获取页面源码数据
page_text = driver.page_source
#数据解析：解析页面源码数据中动态加载的电影详情数据
tree = etree.HTML(page_text)

ret = tree.xpath('//*[@class="movie-content"]//a/text()')
print(ret)
driver.quit()