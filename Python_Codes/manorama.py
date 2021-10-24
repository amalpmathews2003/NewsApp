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
            self.scrap_trending_news(soup)
            self.scrape_X_news("Sports","https://www.manoramaonline.com/sports.html")
            self.scrape_X_news('Health',"https://www.manoramaonline.com/health.html")
            self.scrape_X_news('Movie',"https://www.manoramaonline.com/movies.html")
            self.scrape_X_news('Tech',"https://www.manoramaonline.com/technology.html")
            self.scrape_X_news('Children',"https://www.manoramaonline.com/children.html")
            self.scrape_X_news('Life',"https://www.manoramaonline.com/style.html")
            self.scrape_X_news('Astro',"https://www.manoramaonline.com/astrology.html")
            self.scrape_X_news('Auto',"https://www.manoramaonline.com/fasttrack.html")
            self.scrape_X_news('Music',"https://www.manoramaonline.com/music.html")
            self.scrape_X_news('Home',"https://www.manoramaonline.com/homestyle.html")
            self.save()

      def scrap_top_news(self,soup):
            priority=1
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
                  
                  body=self.scrap_news_body(href)

                  all.append({'title':title,'href':href,'img':body['img'],
                  "body":body["body_text"],'tags':body['tags'],'date':body['date'],'priority':priority
                  })
                  
                  priority+=1
                        
            news=soup.find("div",{"class":"ml-story-list-right"}).find_all('div',{'class':'story-content'})

            for story in news:
                  a=story.find('a')
                  img=a.find('img')['data-src-web']
                  body=self.scrap_news_body(a['href'])
                  all.append({"title":a['title'],"href":a['href'],"img":body['img'],
                  "body":body["body_text"],'tags':body['tags'],'date':body['date'],
                  'priority':priority
                  })
                  priority+=1
                  
            self.articles['Top News']=all


      def scrap_trending_news(self,soup):
            priority=1
            trending_now=[]
            soup=soup.find('div',{'class':'trending-blk-001'}).find('div',{'class':'trending-news-blk'})
            soup=soup.find_all('li',{'class':''})     
            for article in soup:
                  href=article.find('a')['href']
                  body=self.scrap_news_body(href)

                  trending_now.append({'title':body['title'],
                  'href':href,'img':body['img'],'body':body['body_text'],'date':body['date'],
                  'tags':body['tags'],'priority':priority
                  })
                  priority+=1
            self.articles['Trending']=trending_now

      def scrape_sports_news(self,url=""):
            url="https://www.manoramaonline.com/sports.html"
            r=requests.get(url)
            soup=BeautifulSoup(r.content,'html5lib')
            priority=1
            top_stories=soup.find('div',{'class':'section-top-story-listing'}).find_all('li')
            sports=[]
            for stories in top_stories:
                  href=stories.find('a')['href']
                  body=self.scrap_news_body(href)
                  sports.append({'title':body['title'],
                  'href':href,'img':body['img'],'body':body['body_text'],'date':body['date'],
                  'tags':body['tags'],'priority':priority
                  })
                  priority+=1
            self.articles['Sports']=sports
      def scrape_X_news(self,type,url=""):

            r=requests.get(url)
            soup=BeautifulSoup(r.content,'html5lib')
            priority=1
            top_stories=soup.find('div',{'class':'section-top-story-listing'}).find_all('li')
            health=[]
            for stories in top_stories:
                  href=stories.find('a')['href']
                  body=self.scrap_news_body(href)
                  health.append({'title':body['title'],
                  'href':href,'img':body['img'],'body':body['body_text'],'date':body['date'],
                  'tags':body['tags'],'priority':priority
                  })
                  priority+=1
            self.articles[type]=health
            
      def scrap_news_body(self,url):
            r=requests.get(url)
            soup=BeautifulSoup(r.content,'html5lib')
            title=soup.find('div',{'class':'story-header'}).find('h1',{'class':'story-headline'}).text
            date=soup.find('time',{'class':'story-author-date'}).text
            body=soup.find('div',{'class':'article rte-article'})
            body_text=[]
            for p in body.find_all('p',{'class':''}):
                  body_text.append(p.text)
            tags=[]
            try:
                  li=soup.find('div',{'class':'mmtagblock section'}).find('div',{'class':'story-tags'}).find('ul',{'class':'story-tags-list'}).find_all('li')
                  for tag in li:
                        tags.append(tag.find('a').text)
            except:
                  pass
            print(f"Scraped {url}")
            img=soup.find('div',{'class':'story-figure-image'}).find('img')['src']
            return {'date':date,'body_text':body_text,'tags':tags,'img':img,'title':title}



      def save(self):
            with open('news.txt','w', encoding="utf-8") as f:
                  print(self.articles,file=f)
      def create_html(self):

            pass


a=Manorama()
