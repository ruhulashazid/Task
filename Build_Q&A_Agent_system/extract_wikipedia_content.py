

import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/Bangladesh"
response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')

    content = soup.find_all('p')
    text_content = ' '.join([para.text for para in content])

    with open("bangladesh_wiki.txt", "w", encoding="utf-8") as file:
        file.write(text_content)
    print("Content successfully extracted and saved to bangladesh_wiki.txt")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
