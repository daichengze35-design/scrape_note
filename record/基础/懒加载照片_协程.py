import requests
from lxml import etree
import time
import os
import asyncio
import aiohttp

semaphore = asyncio.Semaphore(5)

def write_file(task):
    title, data = task.result()
    with open(f'./return/img/{title}.jpg', 'wb') as fp:
        fp.write(data)

async def fetch_image(session, url_detail, title, semaphore):
    async with semaphore:
        async with session.get(url_detail, headers=headers) as response:
            data = await response.read()
            return title, data

async def main(img_src):
    session = aiohttp.ClientSession()
    task_list = []
    for src in img_src:
        url_detail = "https:" + src.xpath('.//img/@data-original')[0]
        title = src.xpath('.//img/@alt')[0]
        task = asyncio.create_task(fetch_image(session, url_detail, title, semaphore))
        task.add_done_callback(write_file)
        task_list.append(task)
    await asyncio.wait(task_list)
    await session.close()
    

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
    asyncio.run(main(img_src))
t_over = time.time()
print('用时'+str(t_over-t_start)+'s')