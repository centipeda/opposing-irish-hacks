from newspaper import Article
from newsapi import NewsApiClient
import sys

url = "https://www.npr.org/2019/11/09/777588186/william-barr-emerges-as-the-attorney-general-trump-wanted-democrats-not-so-much"
article = Article(url)
article.download()
article.parse()
article.nlp()
keywords = article.keywords

print("keywords: " + " OR ".join(keywords))

client = NewsApiClient(api_key='0cfc6dadf31e40d588afd3cbb5020b09')

all_articles = client.get_everything(q=' OR '.join(keywords),
                                      sources='bbc-news, cnn, fox-news',
                                      from_param='2019-11-01',
                                      to='2019-11-09',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

# links = [a for a in all_articles.articles]
print(all_articles['articles'][0].url)

