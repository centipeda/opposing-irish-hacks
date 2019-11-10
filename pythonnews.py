import os
import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


authenticator = IAMAuthenticator('JuD8ZyOZjrfEJzMiPjIRLUTLejmuEe8kuyKUn1xSzeol')
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)

discovery.set_service_url('https://gateway.watsonplatform.net/discovery/api')

#Env and Collection IDs
environment_id = 'system'
collection_id = 'news-en'

firstDoc = query(self, environment_id, collection_id, query="title:'William Barr'")

print(firstDoc)

"""
query(self, environment_id, collection_id, filter=None, query=None,
natural_language_query=None, passages=None, aggregation=None, count=None,
return_=None, offset=None, sort=None, highlight=None, passages_fields=None,
passages_count=None, passages_characters=None, deduplicate=None,
deduplicate_field=None, similar=, similar_document_ids=None,
similar_fields=None, bias=None, spelling_suggestions=None,
x_watson_logging_opt_out=None, **kwargs)
"""