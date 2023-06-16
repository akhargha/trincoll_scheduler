from bs4 import BeautifulSoup

import requests

html_text = requests.get('https://internet3.trincoll.edu/ptools/courselisting.aspx').text
soup = BeautifulSoup(html_text,'lxml')
items = soup.select('option[value]')
values = [item.get('value') for item in items]
textValues = [item.text for item in items]
print(textValues)