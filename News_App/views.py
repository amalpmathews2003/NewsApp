from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from . models import *
from . forms import *
import sys
sys.path.append("..")
# from Python_Codes.news_api import news_api_get


def searchNews(request):
      if request.method=="POST":
            searched=request.POST['search']	
            results=NewsArticle.objects.filter(title__icontains=searched).order_by('-date')
            return render(request,'News_App/search-result.html',{"articles":results})

def addComment(request,id):
      if request.method=="POST":
            form=CommentForm(request.POST)
            if form.is_valid():
                  form=form.save(commit=False)
                  form.newsArticle_id=id
                  form.save()
                  return redirect('news-article',id)
      else:
            form=CommentForm
            return redirect('home')

def news(request):
      articles=[]
      datas=NewsArticle.objects.all()
      for data in datas:
            com=Comment.objects.filter(newsArticle=data.id)
            tags=Tags.objects.filter(newsArticle=data.id)
            articles.append({"data":data,'comments':com,'tags':tags})
      return render(request,'News_App/news.html',{"articles":articles})

def showNewsArticle(request,id):
      data=NewsArticle.objects.get(id=id)
      com=Comment.objects.filter(newsArticle=id)
      tags=Tags.objects.filter(newsArticle=id)
      return render(request,'News_App/newsArticle.html',
      {'article':{'data':data,'comments':com,'tags':tags,'comment_num':len(com)}
      ,'form':CommentForm})


def home(request):
      with open('Python_Codes/news.txt','r',encoding='utf-8') as f:
            data=f.read()
      return render(request, 'News_App/home.html', {'data':eval(data)})

# def news_api_call(request):
#       return render(request,'News_App/news_api.html',{"news":news_api_get()})

def auth_test(request):
      return render(request,'News_App/auth_test.html',{})

def convertDate(date):
      from dateutil.parser import parse
      tzinfos = {"IST": "Asia/Kolkata"}
      return parse(date, tzinfos=tzinfos)

def addToDatabse(newses):
      for news in newses:
            article=NewsArticle()
            article.title=news['title']
            article.body=news['body']
            article.pic_url=news['img']
            article.href=news['href']
            article.date=convertDate(news['date'])
            article.save()
            for tag in news['tags']:
                  try:
                        Tag=Tags()
                        Tag.tag=tag
                        Tag.newsArticle=article
                  except:
                        pass

            

def addNewstoDatabase(request):
      with open('Python_Codes/news.txt','r',encoding='utf-8') as f:
            data=f.read()
            data=eval(data)
            top_news=data['top_news']
            addToDatabse(top_news)

            print(f'{len(top_news)}added to database')
      return redirect('home')


























class NewsArticlesReactView(APIView):
      serializer_class = NewsArticleSerializer

      def get(self, request):
            all = [{"Title": news.title,
            "Image":"http://127.0.0.1:8000"+news.pic.url, "Date": news.date, 
            "Desc":news.desc,"ID":news.id
            } for news in NewsArticle.objects.all()]
            return Response(all)

      def post(self, request):
            serializer = NewsArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                  # print(serializer)
                  serializer.save()
                  return Response('Article added succesfully')


class CommentReactView(APIView):
      serializer_class = CommentSerializer

      def get(self, request):
            all = [{"Article": comment.newsArticle.title, "comment": comment.comment}
            for comment in Comment.objects.all()]
            return Response(all)

      def post(self, request):
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                  #print(serializer)
                  serializer.save()
                  return Response("Comment added succesfully") 
