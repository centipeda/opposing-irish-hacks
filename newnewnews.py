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



curl -X POST -u "apikey:CUjh24sJMFvIO7WeXPUSWH5do9XqKBWfbuY88w7XK_f9" \
-H "Content-Type: application/json" \
-d "{\"name\":\"my-first-environment\",\"description\":\"exploring environments\"}" \
"https://gateway-syd.watsonplatform.net/discovery/api/v1/environments?version=2019-04-30"


curl -X POST -u "apikey":"CUjh24sJMFvIO7WeXPUSWH5do9XqKBWfbuY88w7XK_f9" -H "Content-Type: application/json" -d '{
  "name": "my_environment",
  "description": "My environment"
}' "https://gateway.watsonplatform.net/discovery/api/v1/environments?version=2019-04-30"


curl -u "apikey:5f-M-WPa-tIzPVfRiitIJXhn2Q3oh25rXLI8pyOkDpMx" "https://gateway.watsonplatform.net/discovery/api/v1/environments/system/collections/news-en/query?version=2019-04-30&query=enriched_text.entities.text:IBM"