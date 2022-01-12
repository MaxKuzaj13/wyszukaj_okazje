import time
from requests import get
from bs4 import BeautifulSoup
from discord_notification import discord
import json

try:
    with open('json_db.txt') as json_file:
        data = json.load(json_file)
    found_products = data
    json_file.close()
except FileNotFoundError:
    found_products = {}


def scrap_data():
    url = 'https://www.olx.pl/motoryzacja/motocykle-skutery/skuter/warszawa/q-skuter/?search%5Bfilter_float_price%3Afrom%5D=500&search%5Bfilter_enum_condition%5D%5B0%5D=notdamaged'
    page = get(url)
    content = BeautifulSoup(page.text, 'html.parser')
    products = content.find_all(class_='offer-wrapper')

    for product in products:
        name = product.select_one('.title-cell h3').text.strip()
        price = product.select_one('.price strong').text.strip()
        url = product.select_one('.title-cell a')['href']

        if name not in found_products:
            found_products[name] = str(price)
            discord.post(content=f"Znaleziono: {name} za {price} link: {url}")

    with open('json_db.txt', 'w', encoding='utf-8') as outfile:
        json.dump(found_products, outfile)
        time.sleep(1)




