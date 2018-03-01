#!/usr/bin/env python3
import requests
import sys
from bs4 import BeautifulSoup

exercise = sys.argv[1]
issession = sys.argv[2]
iscreds = sys.argv[3]
term = sys.argv[4]

cookies = {
    'issession': issession,
    'iscreds': iscreds
}

response = requests.get(
    f'https://is.muni.cz/auth/edutools/brandejs/compsyslab?fakulta=1433;obdobi={term};ukol=i{exercise}',
    cookies=cookies
)

html = response.text
startH2 = html.find("<h2>")
startDiv = html.find("<div>", startH2)
print(BeautifulSoup(html[startH2+4:startDiv-1], 'html.parser').get_text().strip().replace('Výklad\n\n', '\n\nVýklad:'))
