import requests
from lxml import etree
from pathlib import Path
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import os
from multiprocessing import Value

output_dir = Path("return")
output_dir.mkdir(parents=True, exist_ok=True)

def download_jianli(div, page):
    global headers, f
    url_detail = div.xpath('./a/@href')[0]
    title = div.xpath('./a/img/@alt')[0]
    detail_response = requests.get(url_detail,headers = headers,timeout=10)
    path_detail = etree.HTML(detail_response.text)
    url_jl = path_detail.xpath('//ul[@class="clearfix"]/li[1]/a/@href')[0]
    response = requests.get(url_jl,headers=headers,timeout = 20)
    if response.status_code == 200:
        success_count.value += 1
        jl = response.content
        os.makedirs(f"./return/简历/{page}", exist_ok=True)
        with open(f"./return/简历/{page}/{title}.rar","wb") as f:
            f.write(jl)
        print (title + "抓取成功")

def main(page):
    t_process_start = time.time()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    if page == 1:
        url = 'https://sc.chinaz.com/jianli/free.html'
    else:
        url = 'https://sc.chinaz.com/jianli/free_%d.html'%page
    response = requests.get(url,headers = headers,timeout=50)
    response.encoding = "utf-8"
    path = etree.HTML(response.text)
    pool = ThreadPoolExecutor(max_workers=10)
    list_div = path.xpath('/html/body//div[@id="main"]/div[@class="main_list jl_main" and @id="container"]/div')
    for div in list_div:
        pool.submit(download_jianli, div, page)
        num.value += 1
    pool.shutdown(wait=True)
    t_process_end = time.time()
    print(f"第{page}页抓取完成，共抓取{len(list_div)}份简历模板，用时{t_process_end - t_process_start:.2f}秒")

t_start = time.time()
num = Value("i", 0)
success_count = Value("i", 0)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
Process_pool = ProcessPoolExecutor(max_workers=5)
for page in range(1,10):
    Process_pool.submit(main,page)
Process_pool.shutdown(wait=True)
t_end = time.time()
print('用时'+str(t_end-t_start)+"秒，共抓取"+str(num.value)+"份简历模板，成功抓取"+str(success_count.value)+"份简历模板")