import requests
import json

def search_churches_and_store(url, headers=None, params=None, output_file='response.json'):
    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=params)
        
        # Check if the response was successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Parse the JSON data from the response

            # Save the data to a JSON file
            with open(output_file, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            
            print(f"Data successfully stored in {output_file}")
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    url = 'https://find.church.tools/api/search?quickSearch=true&query=FEG karlsruhe'
    # headers = {
    #     'Authorization': 'Bearer your_access_token'  # If authentication is needed
    # }
    # params = {
    #     'query': 'example',  # Example query parameters
    #     'limit': 10
    # }
    
    search_churches_and_store(url, headers=None, params=None, output_file='src/test/church_tools_api/church_tools_api_response.json')
