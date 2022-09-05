import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator('uLkvpNs8DGq76S8B-Wdzlm5muLCMIu3FFzsw1Zjxv6F6')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/2b40ef26-23b6-4185-906e-d22870a9ffbf')

def english_to_french(english_text):
    #write the code here
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text