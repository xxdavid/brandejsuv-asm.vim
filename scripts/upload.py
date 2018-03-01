#!/usr/bin/env python3
import requests
import sys
from bs4 import BeautifulSoup

exercise = sys.argv[1]
filename = sys.argv[2]
issession = sys.argv[3]
iscreds = sys.argv[4]
term = sys.argv[5]

with open(filename) as file:
    content = file.read()

print(content)

cookies = {
    'issession': issession,
    'iscreds': iscreds
}

response = requests.post(
    f'https://is.muni.cz/auth/edutools/brandejs/compsyslab?fakulta=1433;obdobi={term};ukol=i{exercise}',
    data={
        'ukol': f'i{exercise}',
        'fakulta': '1433',
        'obdobi': term,
        'asembler': content,
        'exppar': '1',
        'kontrola': 'Zkontrolovat'
    },
    cookies=cookies
)


soup = BeautifulSoup(response.text, 'html.parser')

if len(soup.find_all('div', {'class': 'potvrzeni'})) > 1:
    print("Úkol splněn!")
else:
    errors = soup.find_all('div', {'class': 'chyba'})

    print(errors[2].get_text().replace('Řešení nesplňuje zadání', 'Řešení nesplňuje zadání.\n'))
    if len(errors) > 3:
        print(errors[3].get_text())

