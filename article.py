import newspaper
from newspaper import article
import soupsieve

url = input()
article = Article(url)
article.download()
article.html
article.parse()

keywords = article.keywords

