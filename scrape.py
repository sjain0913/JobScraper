import requests
import pprint
from bs4 import BeautifulSoup

url = "https://www.monster.com/jobs/search/?q=Software-intern&where=Atlanta"
page = requests.get(url)
print(page)