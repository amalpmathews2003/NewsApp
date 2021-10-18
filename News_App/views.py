from django.shortcuts import render
import sys
sys.path.append("..")
from Python_Codes.news_api import news_api_get
def home(request):
      context={"data":"hello world"}
      return render(request,'News_App/home.html',context)

def news_api_call(request):
      return render(request,'News_App/news_api.html',{"news":news_api_get()})