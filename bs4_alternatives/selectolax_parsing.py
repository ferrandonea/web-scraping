import time
import requests
from selectolax.parser import HTMLParser

start = time.perf_counter()

# ejemplo de parsel
# tiene selectores específicos de CSS
r = requests.get("https://books.toscrape.com/")

html = HTMLParser(r.text)

print(html.css_first("h1").text())

for item in html.css("article.product_pod"):
    book = {
        "name": item.css_first("h3 a").attributes["title"],
        "link": item.css_first("h3 a").attributes["href"],
        "price": item.css_first("p.price_color").text(),
        "img": item.css_first("img.thumbnail").attributes["src"],
    }
    print(book)

print(f"{time.perf_counter()-start} segundos")
