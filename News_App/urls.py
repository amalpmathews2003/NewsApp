from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('news',views.news_api_call,name="news-api-call")
]
