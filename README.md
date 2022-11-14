### Assignment on Information Retrieval for Advanced Database Management Systems - Kathmandu University

#### Task 1: Choose any Nepali online news website and crawl all the links and hyperlinks within the website. Based on the links and hyperlinks, conclude that the website is a “hub” or an “authority”. Please consider repeated counts of the same link/hyperlink just as one hyperlink.

<br/>

#### Task 2:  Scrape data from 5 Nepali online news websites for the last two months (September – October 2022) focusing on the keywords “समाचार”, “आम निर्वाचन २०७९” “विचार”, “राजनीति” etc. Remove Nepali stopwords from the scrapped text. Compute the term frequencies of the top twenty terms/words in each of these genres and display the information in the form of a graph. Project the popularity graphs of political leaders and parties on the basis of mentions and positive/negative comments in the articles.

To install the project
`pip3 install -r requirements.txt `

##### For Task 1:

`python3 crawler.py`

##### For Task 2:

Here are two different python files. <br />
<b>scrape.py</b> is a first python file to run which scrapes 5 different news website and stores the content in corpus.txt

`python3 scraper.py`

<b>results.py</b> is a second python file which does work like filtering the stop words and generates the output for the assignment.

`python3 result.py`
