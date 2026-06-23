import requests
from lxml import etree
import time
import asyncio
import aiohttp

url = "https://bixuejian.5000yan.com/"

t_start = time.time()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url,headers = headers)
response.encoding = "utf-8"

async def main (Li):
    task_list = []
    f = open("./return/章节名.txt","w",encoding = "utf-8")
    session = aiohttp.ClientSession()
    for list_ditail in Li:
        task = asyncio.create_task(fetch(session, list_ditail, f))
        task.add_done_callback(write_title)
        task_list.append(task)
    await asyncio.wait(task_list)
    f.close()
    await session.close()

async def fetch(session, list_ditail, f):
    url_detail = list_ditail.xpath('./a/@href')[0]
    async with session.get(url_detail, headers=headers) as detail_response:
        detail = etree.HTML(await detail_response.text(encoding = "utf-8"))
        title = detail.xpath('/html/head/title/text()')[0]
        title = title.removesuffix(" - 《碧血剑》")
        return title, f

def write_title(task):
    title, f = task.result()
    with open("./return/章节名.txt", "a", encoding="utf-8") as f:
        f.write(title + '\n')

if response.status_code == 200:
    xpath = etree.HTML(response.text)
    Li = xpath.xpath('/html/body/div[@class="container mt-md-2"]/div[@class="row custom-row"]/div[@class="col-md-9  gx-2"]/div[@class="p-2 my-2 bg-white rounded"]/ul/li')
    asyncio.run(main(Li))

t_end = time.time()
print(t_end-t_start)