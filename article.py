from newspaper import Article
from googlesearch import search
import requests

#url = input()
url = "https://www.cnn.com/2019/11/08/us/osu-abuse-lawsuit-title-ix/index.html"
article = Article(url)
article.download()
article.parse()
article.nlp()

center = ["bbc.com", "apnews.com", "reuters.com", "npr.org", "abcnews.go.com", "wsj.com", "nytimes.com", "politico.com", "cbsnews.com", "businessinsider.com", "fortune.com"]
left = ["cnn.com", "washingtonpost.com", "vox.com", "newyorker.com", "theatlantic.com", "huffingtonpost.com", "vanityfair.com", "progressive.org"]
right =["foxnews.com", "msnbc.com", "nypost.com", "reason.com"]

keywords = article.keywords
print(keywords)

query = ""
for k in keywords:
    query = query + k + " "

for j in search(query, tld="co.in", num=20, pause=2): 
    print(j) 