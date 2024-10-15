import ollama

import json

# Open and read the JSON file
with open('src/test/scrape_confession_of_faith/faecherkirche_subpages.json', 'r') as file:
    data = json.load(file)
    
# Access and print specific values
print("\nAccessing specific values:")
print(f"Base URL: {data['base_url']}")
print(f"Number of subpages: {len(data['subpages'])}")

concatenated_urls = '\n'.join(data['subpages'])

prompt = "From the following list of subpages of a website, find the link mostly to be the confession of faith. Output only the url: " + concatenated_urls

print(f"Prompt: {prompt}\n\n")

response = ollama.chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': prompt,
  },
])
print(response['message']['content'])