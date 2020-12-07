import requests
from bs4 import BeautifulSoup as soup

site = requests.get(https://www.vg.no/)

soup = bs(site.content)

print(soup)