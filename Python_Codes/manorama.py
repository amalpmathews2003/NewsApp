import requests
from bs4 import BeautifulSoup
import os


os.chdir(os.path.dirname(__file__))


def scrap():
      url="https://www.manoramaonline.com"
      r=requests.get(url)
      soup=BeautifulSoup(r.content,'html5lib')
      all=[]
      news=soup.find("div",{"class":"ml-story-list-left"})
      for i in range(1,4):
            news2=news.find("div",{"class":f"story-list-0{i}"})
            if(i>1):
                  head=news2.find('div',{"class":f"subhead-00{2}-ml"}).find('a')
            else:
                  head=news2.find('div',{"class":f"subhead-00{1}-ml"}).find('a')
   
            title=head['title']
            href=head['href']
            img=news2.find("div",{"class":"image-block"}).find('a').find("img")['data-src-web']
            try:
                  desc=news2.find('p',{'class':'content-ml-001'}).find('a').text
                  all.append({'title':title,"desc":desc,'href':href,'img':url+img})
            except:
                  all.append({'title':title,'href':href,'img':url+img})
            

      

      
      news=soup.find("div",{"class":"ml-story-list-right"}).find_all('div',{'class':'story-content'})

      for story in news:
            a=story.find('a')
            img=a.find('img')['data-src-web']
            all.append({"title":a['title'],"href":a['href'],"img":url+img})

      with open('temp.txt','w', encoding="utf-8") as f:
            print(all,file=f)
            # for i in all:
            #       print(i,file=f)
  

scrap()


