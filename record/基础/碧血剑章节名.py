import requests
from lxml import etree
import time

url = "https://bixuejian.5000yan.com/"

t_start = time.time()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url,headers = headers)
response.encoding = "utf-8"

f = open("./return/章节名.txt","w",encoding = "utf-8")
if response.status_code == 200:
    xpath = etree.HTML(response.text)
    Li = xpath.xpath('/html/body/div[@class="container mt-md-2"]/div[@class="row custom-row"]/div[@class="col-md-9  gx-2"]/div[@class="p-2 my-2 bg-white rounded"]/ul/li')
    for list_ditail in Li:
        url_detail = list_ditail.xpath('./a/@href')[0]
        detail_response = requests.get(url_detail,headers = headers)
        detail_response.encoding = "utf-8"
        detail = etree.HTML(detail_response.text)
        title = detail.xpath('/html/head/title/text()')[0]
        title = title.removesuffix(" - 《碧血剑》")
        f.write(title+'\n')
        print(title)
f.close()

t_end = time.time()
print(t_end-t_start)