from newspaper import Article
import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
nltk.download('stopwords')

urls = ['https://election.onlinekhabar.com',
        'https://setopati.com',
        'https://ekantipur.com',
        'https://ratopati.com',
        'https://nagariknews.nagariknetwork.com'
        ]

f = open('corpus.txt', 'a')  # A file where we store our scraped data


for url in urls:
    # running loop on our targeted newspaper one by one
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    cleanedUrls = []
    for link in soup.find_all('a'):
        if "https://" in link['href']:
            cleanedUrls.append(link["href"])
            print('___________________________________________')
            print('scraping ....', link.get('href'))
            article = Article(link.get('href'), language='hi')
            article.download()
            # article.html
            article.parse()
            article.nlp()
            data = {
                "TITLE": article.title,
                "keywords": article.keywords,
                "summary": article.summary,
                "TEXT": article.text,
                "img_url": article.top_image,
            }
            f.write(article.title)
            f.write(article.text)
            print(data)
f.close()
