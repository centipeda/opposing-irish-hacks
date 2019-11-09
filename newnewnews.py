#Watson Time
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('7AQhKTuRCG_tEM68269k1zZiQFQbovXHGNIX_Q1kxyWT')
assistant = AssistantV1(
    version='2018-07-10',
    authenticator=authenticator)
assistant.set_service_url('<url as per region>')