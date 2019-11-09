from newspaper import Article
#from googlesearch import search
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

#find keywords and add them to query
keywords = article.keywords
print(keywords)

query = ""
for k in keywords:
    query = query + k + " "

"""for j in search(query, tld="co.in", num=2, stop = 2, pause=2):
    print(j)

center_query= query + "("
for c in center:
    center_query = center_query + "site:" + c + " OR "
center_query = center_query[:-4]
center_query+=")"

left_query = query + "("
for l in left:
    left_query = left_query + "site:" + c + " OR "
left_query = left_query[:-4]
left_query+=")"

right_query= query + "("
for r in right:
    right_query = right_query + "site:" + r + " OR "
right_query = right_query[:-4]
right_query+=")"
print(right_query)

#Check which list site is in and filter query to sites from
#other two lists
alreadyFound = False

if not alreadyFound:
    for site in center:
        if site in url:
            alreadyFound = True
            for j in search(right_query, tld="co.in", num = 20, stop=20, pause = 2):
                print(j)
            for j in search(left_query, tld="co.in", num=20, stop=20, pause=2):
                print(j)

if not alreadyFound:
    for site in right:
        if site in url:
            alreadyFound = True
            for j in search(left_query, tld="co.in", num = 20, stop=20, pause = 2):
                print(j)
            for j in search(center_query, tld="co.in", num=20, stop=20, pause=2):
                print(j)

if not alreadyFound:
    for site in left:
        if site in url:
            alreadyFound = True
            for j in search(right_query, tld="co.in", num = 20, stop=20, pause = 2):
                print(j)
            for j in search(center_query, tld="co.in", num=20, stop=20, pause=2):
                print(j)
"""
