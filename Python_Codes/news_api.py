api_key="54404813513f4327bc025151cde77a10"
import requests
def news_api_get():
      r=requests.get(f'https://newsapi.org/v2/everything?q=kerala&sortBy=popularity&apiKey={api_key}')
      r=r.json()
      news=[]
      for article in r['articles']:
            title=article['title']
            desc=article['description']
            url=article['url']
            image=article['urlToImage']
            content=article['content']

            article={'title':title,'description':desc,'url':url,'image':image,'content':content}
            news.append(article)
      return news