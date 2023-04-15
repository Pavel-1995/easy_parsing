import requests
from bs4 import BeautifulSoup
import json


# url = "https://e-zoo.by/"
#
# headers = {
#     "accept": "*/*",
#     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# #print(src)
#
# with open("index.html", 'w') as file:
#      file.write(src)

with open("index.html") as file:
      src = file.read()

soup = BeautifulSoup(src, 'lxml')
#all_hrefs_column2 = soup.find("div", class_= "menu__lists menu__lists--filtered menu__lists--cat")
all_hrefs_column2 = soup.find_all(class_= "menu__dropdown")

#print(all_hrefs_column2)
all_href = {}
for item in all_hrefs_column2:
       item_text = item.text
       item_href = "https://e-zoo.by" +item.get('href')
       #print(f"{item_text}: {item_href}")
       all_href[item_text] = item_href

with open("all_htef.json", "w") as file:
      json.dump(all_href, file, indent=4, ensure_ascii=False)







