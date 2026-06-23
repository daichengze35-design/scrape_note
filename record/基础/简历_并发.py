import requests
from lxml import etree
from pathlib import Path
import time
from threading import Thread

output_dir = Path("return")
output_dir.mkdir(parents=True, exist_ok=True)

def download_jianli(div):
    global headers, f
    url_detail = div.xpath('./a/@href')[0]
    title = div.xpath('./a/img/@alt')[0]
    detail_response = requests.get(url_detail,headers = headers,timeout=10)
    path_detail = etree.HTML(detail_response.text)
    url_jl = path_detail.xpath('//ul[@class="clearfix"]/li[1]/a/@href')[0]
    jl = requests.get(url_jl,headers=headers,timeout = 20).content
    with open(f"./return/简历/{title}.rar","wb") as f:
        f.write(jl)
    print (title + "抓取成功")

t_start = time.time()
thread_list = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
for page in range(1,2):
    if page == 1:
        url = 'https://sc.chinaz.com/jianli/free.html'
    else:
        url = 'https://sc.chinaz.com/jianli/free_%d.html'%page
    response = requests.get(url,headers = headers,timeout=10)
    response.encoding = "utf-8"
    path = etree.HTML(response.text)
    list_div = path.xpath('/html/body//div[@id="main"]/div[@class="main_list jl_main" and @id="container"]/div')
    for div in list_div:
        t = Thread(target=download_jianli, args=(div,))
        t.start()
        thread_list.append(t)
for t in thread_list:
    t.join()
t_end = time.time()
print('用时'+str(t_end-t_start))