import requests
from bs4 import BeautifulSoup
from pathlib import Path

output_dir = Path("return")
output_dir.mkdir(parents=True, exist_ok=True)

url = "https://www.baidu.com" 
session = requests.Session()
headers = {
    
}

# proxies = {
#     "http": "http://127.0.0.1:1080",
#     "https": "http://127.0.0.1:1080",
# }
response = session.get(url, timeout=10)
coding = response.apparent_encoding     # 设置编码
response.encoding = "utf-8"
file = open (output_dir / "web.html",mode = "w",encoding = "utf-8")
# csrf = open (output_dir / "CERF_Token.txt",mode = "w",encoding = coding)

if response.status_code == 200:
    file.write(response.text)
    # soup = BeautifulSoup(response.text,"html.parser")
    # csrf_token = soup.find("input", {"name": "csrf_token"})["value"]
    # csrf.write(csrf_token)
    print ("success")
else:
    print(response.status_code)
    print(response.headers)
file.close()
