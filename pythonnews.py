import os
import sys
import newspaper
import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

environment_id = 'system'
collection_id = 'news-en'

def get_url():
    return "https://www.npr.org/2019/11/08/777573489/white-house-broke-from-normal-process-handling-trump-ukraine-call-witness-said"
    for l in sys.stdin:
        url = l
    return url
    
def get_title(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    print("article title: ".format(article.title))
    return article.title

def watson_auth():
    authenticator = IAMAuthenticator('JuD8ZyOZjrfEJzMiPjIRLUTLejmuEe8kuyKUn1xSzeol')
    discovery = DiscoveryV1(
        version='2019-04-30',
        authenticator=authenticator
    )
    discovery.set_service_url('https://gateway.watsonplatform.net/discovery/api')

    return discovery

    # Env and Collection IDs

def first_query(discovery, title):
    firstDoc = discovery.query(environment_id, collection_id, filter="title:{}".format(title), deduplicate = True, deduplicate_field=title, count = 20)

    # print(firstDoc)
    return firstDoc

def second_query(discovery, docID, docurl):
    #Insert code using data from first document to find similar documents
    secondDoc = discovery.query(environment_id, collection_id, query="title:{}".format(docurl),
                                similar=True, similar_document_ids=docID, similar_fields = "title", count = 5, deduplicate = True)  

    return secondDoc


def main():
    url = get_url()
    title = get_title(url)
    discover = watson_auth()
    firstDoc = first_query(discover, title)
    #docID = print(json.dumps(firstDoc.get_result()[0], indent=2))
    #docID = firstDoc.get_result()['results'][0]['id']
    docID = firstDoc.get_result()['results'][0]['id']
    docurl = firstDoc.get_result()['results'][0]['title']
    #docConcepts = firstDoc.get_results()['enrichments'][0]['options']['concepts']
    #print(docConcepts)
    secondDoc = second_query(discover, docID, docurl)
    print(secondDoc.get_result()['results'][2]['url'])
    print(secondDoc.get_result()['results'][2]['title'])
    #print(secondDoc['result'][0]['title'])
    #docTitle = secondDoc.get_result()['results'][0]['title']

def test():
    url = get_url()
    title = get_title(url)
    discover = watson_auth()
    data = first_query(discover, title)
    print(data.get_result()[''])

if __name__ == "__main__":
    main()

"""
query(self, environment_id, collection_id, filter=None, query=None,
natural_language_query=None, passages=None, aggregation=None, count=None,
return_=None, offset=None, sort=None, highlight=None, passages_fields=None,
passages_count=None, passages_characters=None, deduplicate=None,
deduplicate_field=None, similar=, similar_document_ids=None,
similar_fields=None, bias=None, spelling_suggestions=None,
x_watson_logging_opt_out=None, **kwargs)
"""