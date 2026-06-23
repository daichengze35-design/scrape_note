import requests
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.51miz.com/"
}
url = 'https://www.51miz.com/shipin/'
response = requests.get(url=url,headers=headers)
page_text = response.text


tree = etree.HTML(page_text)
div_list = tree.xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div')
print(len(div_list))
for div in div_list:
    src_list = div.xpath('./a/div/div/div/video/source/@src')
    print(len(src_list))
    for src in src_list:
        src = 'https:'+src
        video_data = requests.get(url=src,headers=headers).content
        video_title = src.split('/')[-1]
        with open(f"./return/videos/{video_title}",'wb') as fp:
            fp.write(video_data)
        print(video_title,'爬取保存成功！')