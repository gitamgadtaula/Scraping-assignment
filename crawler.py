import requests
from bs4 import BeautifulSoup
reqs = requests.get('https://nagariknews.nagariknetwork.com/')
soup = BeautifulSoup(reqs.text, 'html.parser')
cleanedUrls = []
for link in soup.find_all('a'):
    if "https://" in link['href']:
        print(link['href'])
