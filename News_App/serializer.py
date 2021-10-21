from rest_framework import serializers
from . models import *

class NewsArticleSerializer(serializers.ModelSerializer):
      class Meta:
            model=NewsArticle
            fields=["title","body","pic","type"]
            
class CommentSerializer(serializers.ModelSerializer):
      class Meta:
            model=Comment
            fields="__all__"