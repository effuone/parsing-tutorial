from bs4 import BeautifulSoup
import requests
import json

url = 'https://krisha.kz/prodazha/kvartiry/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

def getIntsFromString(s):
    return int(''.join(filter(str.isdigit, s)))

def get_appartaments(soup):
    appartament_tags = soup.find_all('div', class_="a-card")
    appartaments = []
    for appartament_tag in appartament_tags:
        appartament = {
            'image_url': appartament_tag.find('img').get('src'),
            'title': appartament_tag.find('img').get('title'),
            'price': getIntsFromString(appartament_tag.find('div', class_='a-card__price').get_text().strip()),
            'location': appartament_tag.find_all('div', class_='card-stats__item')[0].get_text(),
            'publish_date': appartament_tag.find_all('div', class_='card-stats__item')[0].get_text()
        }
        appartaments.append(appartament)
    return appartaments

def saveFile(data_dict, file_path):
    json_data = json.dumps(data_dict, indent=4, ensure_ascii=False)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(json_data)

    print(f"JSON file '{file_path}' has been created.")

aps = get_appartaments(soup)
print(aps)
saveFile(aps, 'haty.json')