import time
import requests
from parsel import Selector

start = time.perf_counter()

# ejemplo de parsel
# tiene selectores específicos de CSS
r = requests.get("https://books.toscrape.com/")
html = Selector(text=r.text)

print(html.css("h1::text").get())

for item in html.css("article.product_pod"):
    book = {
        "name": item.css("h3 a").attrib["title"],
        "link": item.css("h3 a").attrib["href"],
        "price": item.css("p.price_color::text").get(),
        "img": item.css("img.thumbnail").attrib["src"],
    }
    print(book)

print(f"{time.perf_counter()-start} segundos")
