import requests
import bs4
import csv
from time import sleep
from random import randint

file = open("iphone.csv", 'w', encoding='UTF-8', newline='\n')
page = 1
file_obj = csv.writer(file)
file_obj.writerow(["Name", "Price"])

while page < 6:
    url = f'https://itechnics.ge/products/list/45?subcategory=false&page={page}'
    response = requests.get(url)
    content = response.text
    soup = bs4.BeautifulSoup(content, "html.parser")
    full_item = soup.find('div', {"class": "content-wrapper"})
    single_item = full_item.find_all('div', {"class": "product-item"})
    for each in single_item:
        name = each.find('p', {"class": "product-item__title"})
        final_name = name.text.strip()
        price = each.find('div', {"class": "[ flex items-center justify-center ]"})
        final_price = price.p.text.strip()
        file_obj.writerow([final_name, final_price])

    page += 1
    sleep(randint(15, 20))
