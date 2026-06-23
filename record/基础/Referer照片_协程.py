import requests
from lxml import etree
from pathlib import Path
import time
import asyncio
import aiohttp

t_start = time.time()

def write_img(task):
    data, n = task.result()
    if data != "error":
        with open(f'./return/{n}.jpg', 'wb') as fp:
            fp.write(data)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "http://blog.sina.com.cn/"
}

async def fetch(src, n):
    async with aiohttp.ClientSession() as session:
        async with session.get(src, headers=headers) as response:
            if response.status == 200:
                data = await response.read()
                return data, n
            else:
                return "error", n

async def main(img_src):
    task_list = []
    n = 1
    for src in img_src:
        task = asyncio.create_task(fetch(src, n))
        task.add_done_callback(write_img)
        task_list.append(task)
        n += 1
    await asyncio.wait(task_list)


url = "http://blog.sina.com.cn/s/blog_01ebcb8a0102zi2o.html?tj=1"
response = requests.get(url, headers=headers, timeout=10)
response.encoding = "utf-8"
if response.status_code == 200:
    tree = etree.HTML(response.text)
    img_src = tree.xpath('//*[@id="sina_keyword_ad_area2"]/div/a/img/@real_src')
    n = 1
    asyncio.run(main(img_src))

t_over = time.time()
print('用时'+str(t_over-t_start)+'s')