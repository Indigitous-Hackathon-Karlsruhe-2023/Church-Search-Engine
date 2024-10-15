import requests

def fetch_markdown_content(url_confession_of_faith):
    url = "https://r.jina.ai/" + url_confession_of_faith
    headers = {
        'Authorization': 'Bearer jina_bd90b8240f304278841c81c0033005e5zBb-1gmIQxSCMHpGjels_XEI2_OG'
    }

    response = requests.get(url, headers=headers)
    markdown_content = response.text

    return markdown_content

def save_markdown_to_file(markdown_content, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

url_confession_of_faith = "https://faecherkirche.de/vision-glaube-werte/"

markdown_confession_of_faith = fetch_markdown_content(url_confession_of_faith)

md_filename = "src/test/scrape_confession_of_faith/confession_of_faith.md"

save_markdown_to_file(markdown_confession_of_faith, md_filename)