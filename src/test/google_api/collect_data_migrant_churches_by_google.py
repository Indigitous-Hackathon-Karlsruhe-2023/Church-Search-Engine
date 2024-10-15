import requests
from googletrans import Translator

API_KEY = 'AIzaSyC8PdvC3vP7yJ0TUiEzY3XxIfM9rZeoFgg'
CSE_ID = '170baafe75a1a4e11'
ENDPOINT = "https://www.googleapis.com/customsearch/v1"

translator = Translator()

def fetch_from_google_cse(language, location, language_of_location="de"):
    # Formulate the query using the two keywords
    query_en = f"evangelical church, {language} in {location}"

    query_translated = translator.translate(query_en, language_of_location)

    params = {
        'q': query_translated.text,
        'key': API_KEY,
        'cx': CSE_ID
    }

    response = requests.get(ENDPOINT, params=params)
    data = response.json()
    return data

# Test
language = "German"
location = "Rome"
results = fetch_from_google_cse(language, location, "it")

# Extracting and printing URLs from the results
for result in results.get('items', []):
    print(result.get('link'))
