import json
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException

load_dotenv()
APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION_TRY = '2018-05-01'


authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION_TRY,
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    french_text = ""
    try:
        translations = language_translator.translate(
        text = [english_text],
        model_id = 'en-fr').get_result()
        french_text = dict(translations["translations"][0])["translation"]
    except ApiException as ex:
        french_text = str(ex.code)
    return french_text

def french_to_english(french_text):
    english_text = ""
    try:
        translations = language_translator.translate(
        text = [french_text],
        model_id = 'fr-en').get_result()
        english_text = dict(translations["translations"][0])["translation"]
    except ApiException as ex:
        english_text = str(ex.code)
    return english_text
