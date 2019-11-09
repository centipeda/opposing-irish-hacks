from newspaper import Article
from newsapi import NewsApiClient
import sys
import datetime

url = "https://www.npr.org/2019/11/09/777588186/william-barr-emerges-as-the-attorney-general-trump-wanted-democrats-not-so-much"
article = Article(url)
article.download()
article.parse()
article.nlp()
keywords = article.keywords

date= article.publish_date

earliest = date - datetime.timedelta(days=14)

if((date + datetime.timedelta(days=14)).isoformat() < datetime.datetime.now().isoformat()):
    latest = date + datetime.timedlta(days=14)
else:
    latest = datetime.datetime.now()



query = " OR ".join(keywords)

print("keywords: " + query)

client = NewsApiClient(api_key='0cfc6dadf31e40d588afd3cbb5020b09')

all_articles = client.get_everything(q=query,
                                      sources='bbc-news, cnn, fox-news, msnbc, the-wall-street-journal, the huffington-post, the washington-post',
                                      from_param=earliest.isoformat(),
                                      to=latest.isoformat(),
                                      language='en',
                                      sort_by='relevancy'
                                      )

links = [a['url'] for a in all_articles['articles']]
for l in links[0:3]:
    print(l)

