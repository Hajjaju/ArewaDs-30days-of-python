#Number one
import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    data = {'url': url, 'links': links}
    json_data = json.dumps(data, indent=2)
    with open('scraped_data.json', 'w') as json_file:
        json_file.write(json_data)
    print('Data has been successfully scraped and saved as scrapped_dataset.json')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)

#NUMBER TWO
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'border': '1'})
    df = pd.read_html(str(table))[0]  
    data = df.to_dict(orient='records')
    json_data = json.dumps(data, indent=2)
    with open('uci_datasets.json', 'w') as json_file:
        json_file.write(json_data)

    print('Table data has been successfully extracted and saved as uci_datasets.json')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)

# Number three

import requests
from bs4 import BeautifulSoup
import json
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    presidents_table = soup.find('table', {'class': 'wikitable'})
    presidents_data = []
    for row in presidents_table.find_all('tr')[1:]:  
        columns = row.find_all(['td', 'th'])
        president_info = [col.get_text(strip=True) for col in columns]
        presidents_data.append(president_info)
    keys = ["No.", "Presidency", "President", "President number", "Presidency start", "Presidency end", "Vice President"]
    presidents_list = [dict(zip(keys, president_info)) for president_info in presidents_data]
    json_data = json.dumps(presidents_list, indent=2)
    with open('presidents_data.json', 'w') as json_file:
        json_file.write(json_data)

    print('Presidents data has been successfully scraped and saved as presidents_dataset.json')
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
