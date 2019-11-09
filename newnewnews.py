#Watson Time
import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('7AQhKTuRCG_tEM68269k1zZiQFQbovXHGNIX_Q1kxyWT')
discovery = DiscoveryV1(
    version='2018-08-01',
    authenticator=authenticator)
discovery.set_service_url('https://gateway.watsonplatform.net/discovery/api')

environments = discovery.list_environments().get_result()
print(json.dumps(environments, indent=2))

news_environment_id = 'system'
print(json.dumps(news_environment_id, indent=2))

collections = discovery.list_collections(news_environment_id).get_result()
news_collections = [x for x in collections['collections']]
print(json.dumps(collections, indent=2))

configurations = discovery.list_configurations(
    environment_id=news_environment_id).get_result()
print(json.dumps(configurations, indent=2))

query_results = discovery.query(
    news_environment_id,
    news_collections[0]['collection_id'],
    filter='extracted_metadata.sha1::f5*',
    return_fields='extracted_metadata.sha1').get_result()
print(json.dumps(query_results, indent=2))