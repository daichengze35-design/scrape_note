# 因并发量没有限制，有时会报错，使用线程池的请参考 ./Referer照片_线程池.py

import requests
from lxml import etree
from pathlib import Path
import time
from threading import Thread

t_start = time.time()

def download_image(src, n):
    global headers
    data = requests.get(src, headers=headers).content
    with open(f'./return/{n}.jpg', 'wb') as fp:
        fp.write(data)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "http://blog.sina.com.cn/"
}

thread_list = []

url = "http://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1"
response = requests.get(url, headers=headers, timeout=10)
response.encoding = "utf-8"
if response.status_code == 200:
    tree = etree.HTML(response.text)
    img_src = tree.xpath('//*[@id="sina_keyword_ad_area2"]/div/a/img/@real_src')
    n=1
    for src in img_src:
        t = Thread(target=download_image, args=(src, n))
        t.start()
        thread_list.append(t)
        n+=1

for t in thread_list:
    t.join()

t_over = time.time()
print('用时'+str(t_over-t_start)+'s')