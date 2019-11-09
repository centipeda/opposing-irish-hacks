import newspaper
from newspaper import article

url = input()
article = Article(url)
article.download()
article.html
article.parse()

keywords = article.keywords

