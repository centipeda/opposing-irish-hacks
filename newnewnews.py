#Watson Time
import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('7AQhKTuRCG_tEM68269k1zZiQFQbovXHGNIX_Q1kxyWT')
discovery = DiscoveryV1(
    version='2018-08-01',
    authenticator=authenticator)
discovery.set_service_url('https://gateway-syd.watsonplatform.net/discovery/api')

environments = discovery.list_environments().get_result()
print(json.dumps(environments, indent=2))

