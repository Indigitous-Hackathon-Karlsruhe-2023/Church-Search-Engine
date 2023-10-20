import requests

API_KEY = '***'
CSE_ID = '***'
ENDPOINT = "https://www.googleapis.com/customsearch/v1"

def fetch_from_google_cse(query):
    params = {
        'q': query,
        'key': API_KEY,
        'cx': CSE_ID
    }

    response = requests.get(ENDPOINT, params=params)
    data = response.json()
    return data

# Test
query = "Internationale Christliche Gemeinde Karlsruhe"
results = fetch_from_google_cse(query)

# Extracting and printing URLs from the results
for result in results.get('items', []):
    print(result.get('link'))
