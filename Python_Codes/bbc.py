import requests
from bs4 import BeautifulSoup

url="https://www.bbc.com/news"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')


