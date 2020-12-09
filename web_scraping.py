#documentasjon https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#dokumentasjon css https://www.w3schools.com/cssref/css_selectors.asp


import requests
from bs4 import BeautifulSoup as bs

site = requests.get("https://keithgalli.github.io/web-scraping/example.html")

soup = bs(site.content)

print(soup.prettify())