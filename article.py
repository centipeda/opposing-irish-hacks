import newspaper
from newspaper import article
import bs4
from bs4 import BeautifulSoup
import requests

url = input()
article = Article(url)
article.download()
article.html
article.parse()

keywords = article.keywords

