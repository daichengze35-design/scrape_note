import requests
from lxml import etree
from pathlib import Path
import time

t_start = time.time()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "http://blog.sina.com.cn/"
}
url = "http://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1"
response = requests.get(url, headers=headers, timeout=10)
response.encoding = "utf-8"
print (response.status_code)
if response.status_code == 200:
    tree = etree.HTML(response.text)
    img_src = tree.xpath('//*[@id="sina_keyword_ad_area2"]/div/a/img/@real_src')
    n=1
    for src in img_src:
        data = requests.get(src, headers=headers).content
        with open(f'./return/{n}.jpg', 'wb') as fp:
            fp.write(data)
        n+=1

t_over = time.time()
print('用时'+str(t_over-t_start)+'s')