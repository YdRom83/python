from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

url = 'https://www.cbr.ru/key-indicators/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

currency = soup.find_all("div", class_="d-flex title-subinfo")

for i in currency:
    name = i.find("div", class_="col-md-5").text.strip()
    print(name)