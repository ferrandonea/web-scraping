import time

import requests
from bs4 import BeautifulSoup

start = time.perf_counter()

# ejemplo de bs4
r = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(r.text, "html.parser")

print(soup.find("h1").text)

for item in soup.find_all("article", {"class": "product_pod"}):
    book = {
        "name": item.find("h3").find("a").attrs["title"],
        "link": item.find("a").attrs["href"],
        "price": item.find("p", "price_color").text,
        "img": item.find("img", "thumbnail").attrs["src"],
    }
    print(book)

print(f"{time.perf_counter()-start} segundos")
