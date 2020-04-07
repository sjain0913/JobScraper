import requests

url = "https://www.monster.com/jobs/search/?q=Software-intern&where=Atlanta"
page = requests.get(url)