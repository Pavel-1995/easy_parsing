import csv

import requests

import json

from bs4 import BeautifulSoup


#
# url = "https://e-zoo.by/"
#
headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
# #
# req = requests.get(url, headers=headers)
# src = req.text
# #print(src)
#
# with open("index.html", 'w') as file:
#      file.write(src)
# #
# with open("index.html") as file:
#       src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# #all_hrefs_column2 = soup.find("div", class_= "menu__lists menu__lists--filtered menu__lists--cat")
# all_hrefs_column2 = soup.find_all(class_= "menu__dropdown")
#
# print(all_hrefs_column2)
# all_href_dict = {}
# for item in all_hrefs_column2:
#        item_text = item.text
#        item_href = "https://e-zoo.by" +item.get('href')
#        #print(f"{item_text}: {item_href}")
#        all_href_dict[item_text] = item_href
# #
# with open("all_href_dict.json", "w") as file:
#       json.dump(all_href_dict, file, indent=4, ensure_ascii=False)
# #       # indent - отступ, ensure_ascii - экранизация
#
with open("all_href_dict.json") as file:
    all_hrefs = json.load(file)

count = 0
for category_name, category_href in all_hrefs.items():

    if count == 0:
        rep = [",", " ", "-"]
        for item in rep:
            if item in category_name:
                category_name = category_name.replace(item, "_")

        req = requests.get(url=category_href, headers=headers)
        src = req.text

        with open(f"date/{count}_{category_name}.html", "w") as file:
            file.write(src)

        with open(f"date/{count}_{category_name}.html") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        table_head = soup.find(class_="animals").find_all("p")

        animals_dog = table_head[0].text
        animals_cat = table_head[1].text
        animals_bird = table_head[2].text
        animals_rodent = table_head[3].text
        animals_fish = table_head[4].text


        with open(f"date/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    animals_dog,
                    animals_cat,
                    animals_bird,
                    animals_rodent,
                    animals_fish
                )
            )

        animals_dog_data = soup.find(class_="menu__lists menu__lists--filtered menu__lists--dog").find_all("a")
        for item in animals_dog_data:
            animals_dog_data_catalog = item.text
            print(animals_dog_data_catalog)





        count+=1











