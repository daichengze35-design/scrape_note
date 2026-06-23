import requests
from lxml import etree
import time
import asyncio
import aiohttp
import os
from concurrent.futures import ThreadPoolExecutor

os.makedirs('./return/简历', exist_ok=True)

async def fetch(div, session, semaphore):
    url_detail = div.xpath('./a/@href')[0]
    title = div.xpath('./a/img/@alt')[0]
    async with semaphore:
        async with session.get(url_detail, headers=headers, timeout = 30) as detail_response:
            path_detail = etree.HTML(await detail_response.text())
            url_jl = path_detail.xpath('//ul[@class="clearfix"]/li[1]/a/@href')[0]
            async with session.get(url_jl, headers=headers, timeout = 30) as jl_response:
                jl = await jl_response.read()
        return title, jl

def write_jl(task):
    title, jl = task.result()
    with open(f"./return/简历/{title}.rar","wb") as f:
        f.write(jl)
    print (title + "抓取成功")

async def main (list_div, page, semaphore):
    session = aiohttp.ClientSession()
    task_list = []
    for div in list_div:
        task = asyncio.create_task(fetch(div, session, semaphore))
        task.add_done_callback(write_jl)
        task_list.append(task)
    await asyncio.wait(task_list)
    await session.close()
    print("第"+str(page)+"页抓取成功")

def run_main(page):
    semaphore = asyncio.Semaphore(5)
    if page == 1:
        url = 'https://sc.chinaz.com/jianli/free.html'
    else:
        url = 'https://sc.chinaz.com/jianli/free_%d.html'%page
    print ("开始第"+str(page)+"页抓取")
    response = requests.get(url,headers = headers,timeout=10)
    response.encoding = "utf-8"
    path = etree.HTML(response.text)
    list_div = path.xpath('/html/body//div[@id="main"]/div[@class="main_list jl_main" and @id="container"]/div')
    asyncio.run(main(list_div, page, semaphore))

t_start = time.time()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

pool = ThreadPoolExecutor(max_workers=5)

for page in range(1,3):
    pool.submit(run_main, page)

pool.shutdown(wait=True)
t_end = time.time()
print('用时'+str(t_end-t_start))