import requests
import json
import os
import sys
import newspaper

for l in sys.stdin:
    articleLink = l
article = newspaper.Article(articleLink)
article.download()
article.parse()
articleTitle = article.title

queryString = ""
apiKey = ""
queryURL = "https://gateway.watsonplatform.net/discovery/api/v1/environments/system?version=2019-04-30&query="
command = '/usr/bin/curl -u apikey:{} {}'.format(apiKey, queryURL)

stream = os.popen(command + queryString)
data = stream.read()

articleData = data['results'][0]


#1st Query (Match title of article, return entities)
#enriched_title.entities.disambiguation.name::'ArticleName'
#enriched_title.entities.text::'ArticleName'
#title::'ArticleName'

#Get entities from the article that is queried

#2nd Query (Find related articles to the entities of first article)
#Possibilites - Find keywords, publication date
#enriched_text.keywords.relevance:'keywords of first article',publication_date::'publication date of 1st article'
#

#queryURL = "https://gateway.watsonplatform.net/discovery/api/v1/environments/system?version=2019-04-30&query=enriched_text.keywords.text::'Barr'"
