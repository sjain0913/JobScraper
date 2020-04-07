import requests
import pprint
from bs4 import BeautifulSoup

URL = "https://www.monster.com/jobs/search/?q=Software-intern&where=Atlanta"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id = 'SearchResults')
jobElements = results.find_all('section', class_='card-content')

#searching for a specific job type (not right because case and whitespace matters)
#myJobs = results.find_all("h2", string='Python Developer')
myJobs = results.find_all('h2', string=lambda text: 'java' in text.lower())
#print(len(myJobs))

#for getting the applying links with the titles of each job
# for p_job in myJobs:
#     link = p_job.find('a')['href']
#     print(p_job.text.strip())
#     print(f"Apply here: {link}\n")

for jobElement in jobElements:
    titleElement = jobElement.find('h2', class_='title')
    companyElement = jobElement.find('div', class_='company')
    locationElement = jobElement.find('div', class_='location')
    if None in (titleElement, companyElement, locationElement):
        continue

    jobTitle = titleElement.text.strip()
    companyTitle = companyElement.text.strip()
    locationTitle = locationElement.text.strip()