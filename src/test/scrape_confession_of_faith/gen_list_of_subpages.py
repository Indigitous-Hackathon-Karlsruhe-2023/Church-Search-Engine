import requests
import os
import json

def search_subpages(site_url, api_key, search_engine_id, max_results=10):
    base_url = "https://www.googleapis.com/customsearch/v1"
    query = f"site:{site_url}"
    
    subpages = []
    start_index = 1
    
    while len(subpages) < max_results:
        params = {
            'key': api_key,
            'cx': search_engine_id,
            'q': query,
            'start': start_index
        }
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('items', [])
            
            if not items:
                break
            
            for item in items:
                subpages.append(item['link'])
                if len(subpages) >= max_results:
                    break
            
            start_index += len(items)
        else:
            print(f"Error: {response.status_code}")
            break
    
    return list(set(subpages))

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


# Replace these with your actual API key and Search Engine ID
api_key = os.environ.get('GOOGLE_API_KEY')
search_engine_id = os.environ.get('GOOGLE_SEARCH_ENGINE_ID')

site_url = "https://faecherkirche.de/"
max_results = 100

subpages = search_subpages(site_url, api_key, search_engine_id, max_results)

print(f"Subpages of {site_url}:")
for i, subpage in enumerate(subpages, 1):
    print(f"{i}. {subpage}")

base_url = "https://faecherkirche.de/"

# Create a dictionary to store the data
data = {
    "base_url": base_url,
    "subpages": subpages
}

# Save the data to a JSON file
save_to_json(data, "faecherkirche_subpages.json")

print(f"Subpages saved to faecherkirche_subpages.json")