import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'

try:
    response = requests.get(url)
    response.raise_for_status()  # Will raise HTTPError if request failed 
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

headlines = soup.find_all(['h1', 'h2', 'h3'])

headline_list = []
for tag in headlines:
    text = tag.get_text(strip=True)
    if text and text not in headline_list:
        headline_list.append(text)

output_file = 'headlines.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for idx, headline in enumerate(headline_list, start=1):
        f.write(f"{idx}. {headline}\n")

print(f"{len(headline_list)} headlines saved to '{output_file}'")
