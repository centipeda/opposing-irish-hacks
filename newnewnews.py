#Watson Time
import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('7AQhKTuRCG_tEM68269k1zZiQFQbovXHGNIX_Q1kxyWT')
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)

discovery.set_service_url('https://gateway-syd.watsonplatform.net/discovery/api')

with open('./test-doc1.html') as fileinfo:
    add_doc = discovery.add_document(
        '{environment_id}',
        '{collection_id}',
        file=fileinfo).get_result()
print(json.dumps(add_doc, indent=2))
