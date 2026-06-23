import requests
from lxml import etree
import time
import os

os.makedirs('./return/img', exist_ok=True)

t_start = time.time()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}
url = "https://sc.chinaz.com/tupian/meinvtupian.html"
response = requests.get(url, headers=headers, timeout=10)
response.encoding = "utf-8"
if response.status_code == 200:
    tree = etree.HTML(response.text)
    img_src = tree.xpath('//*[@*="夏日街头小清新碎花裙美女图片"]/../..//div[@class="item"]')
    for src in img_src:
        url_detail = "https:" + src.xpath('.//img/@data-original')[0]
        title = src.xpath('.//img/@alt')[0]
        data = requests.get(url_detail, headers=headers).content
        with open(f'./return/img/{title}.jpg', 'wb') as fp:
            fp.write(data)
t_over = time.time()
print('用时'+str(t_over-t_start)+'s')