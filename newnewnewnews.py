import requests
queryString = "IBM"
apiKey = "JuD8ZyOZjrfEJzMiPjIRLUTLejmuEe8kuyKUn1xSzeol"
queryURL = "https://gateway.watsonplatform.net/discovery/api/v1/environments/system?version=2019-04-30&query=enriched_text.keywords.text::'Barr'"

url = queryURL.format(queryString)
print(url)
response = requests.get(url, auth=('apikey', apiKey))
print(response)


