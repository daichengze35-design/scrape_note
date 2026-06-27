import requests
import json
from pathlib import Path

output_dir = Path("return")
output_dir.mkdir(parents=True, exist_ok=True)


api = ""
response = requests.get(api)
data = response.json()
file = open(output_dir / "return.json", mode="w", encoding="utf-8")
json.dump(data,file,ensure_ascii = False,indent = 4)
file.close()