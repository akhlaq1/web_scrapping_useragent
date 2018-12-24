import requests
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

ua = UserAgent()

header = {'useragent':ua.chrome}

page = requests.get('https://www.python.org',headers=header)

soup = BeautifulSoup(page.content,'html.parser')

type(soup)