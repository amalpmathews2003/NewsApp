from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.home2,name="home"),
    path('1',views.home,name="home1"),
   #path('news',views.news_api_call,name="news-api-call"),
   path('news',views.news,name="news"),
      path('news/<int:id>',views.showNewsArticle,name="news-article"),
   path('news2',views.NewsArticlesReactView.as_view(),name="news-display"),
    path('comment2',views.CommentReactView.as_view(),name="comment-display"),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('ok',views.auth_test),
    path('news/<int:id>/comment',views.addComment,name="add-comment"),
    path('search',views.searchNews,name='search'),
    path('add',views.addNewstoDatabase)
]
