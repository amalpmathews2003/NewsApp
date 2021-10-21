import requests
from bs4 import BeautifulSoup
import os

class Manorama:
      def __init__(self):
            self.url="https://www.manoramaonline.com"
            r=requests.get(self.url)
            soup=BeautifulSoup(r.content,'html5lib')
            self.articles={}
            self.scrap_top_news(soup)
            
            os.chdir(os.path.dirname(__file__))
            self.scrap_top_news(soup)
            self.scrap_trendin_news(soup)
            self.save()

      def scrap_top_news(self,soup):
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
                        body=self.scrap_news_body(href)

                        all.append({'title':title,"desc":desc,'href':href,'img':url+img,
                        "body":body["body_text"],'tags':body['tags'],'date':body['date']
                        })
                  except:
                        body=self.scrap_news_body(href)
                        all.append({'title':title,'href':href,'img':self.url+img,
                        "body":body["body_text"],'tags':body['tags'],'date':body['date']
                        })
                        
            news=soup.find("div",{"class":"ml-story-list-right"}).find_all('div',{'class':'story-content'})

            for story in news:
                  a=story.find('a')
                  img=a.find('img')['data-src-web']
                  body=self.scrap_news_body(a['href'])
                  all.append({"title":a['title'],"href":a['href'],"img":self.url+img,
                  "body":body["body_text"],'tags':body['tags'],'date':body['date']})
                  
            self.articles['top_news']=all


      def scrap_trendin_news(self,soup):
            trending_now=[]
            soup=soup.find('div',{'class':'trending-blk-001'}).find('div',{'class':'trending-news-blk'})
            soup=soup.find_all('li',{'class':''})     
            for article in soup:
                  href=article.find('a')['href']
                  title=article.find('a')['title']
                  img=self.url+article.find('div').find('img')['data-src-web']

                  body=self.scrap_news_body(href)

                  trending_now.append({'title':title,
                  'href':href,'img':img,'body':body['body_text'],'date':body['date'],
                  'tags':body['tags']})
            self.articles['trending_now']=trending_now

      def scrap_news_body(self,url):
            r=requests.get(url)
            soup=BeautifulSoup(r.content,'html5lib')
            date=soup.find('time',{'class':'story-author-date'}).text
            body=soup.find('div',{'class':'article rte-article'})
            body_text=[]
            for p in body.find_all('p',{'class':''}):
                  body_text.append(p.text)
            li=soup.find('div',{'class':'mmtagblock section'}).find('div',{'class':'story-tags'}).find('ul',{'class':'story-tags-list'}).find_all('li')
            tags=[]
            for tag in li:
                  tags.append(tag.find('a').text)
            print(f"Scraped {url}")
            return {'date':date,'body_text':body_text,'tags':tags}

      def save(self):
            with open('news.txt','w', encoding="utf-8") as f:
                  print(self.articles,file=f)



Manorama()