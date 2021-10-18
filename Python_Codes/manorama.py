import requests
from bs4 import BeautifulSoup

url="https://www.manoramanews.com/"
r=requests.get(url)
soup=BeautifulSoup(r.content,'html5lib')

top_stories=soup.find_all('div',{'class':'topstoriesdisplay section'},'li')

print(top_stories[0].text)