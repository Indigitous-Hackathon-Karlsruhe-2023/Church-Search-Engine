import json

def load_json_and_get_website(json_file):
    try:
        # Load the JSON data from the file
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        # Navigate through the JSON structure to get the website
        website = data['data'][0].get('website', 'Website not found')

        print(f"{website}")
        return website

    except FileNotFoundError:
        print(f"File '{json_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{json_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    json_file = 'src/test/church_tools_api/church_tools_api_response.json'  # Replace with your JSON file path
    load_json_and_get_website(json_file)
