from django.db import models
from PIL import Image


class NewsArticle(models.Model):
      title=models.CharField(max_length=255)
      priority=models.IntegerField(default=0)
      body=models.TextField()
      pic=models.ImageField(upload_to="images/",default='IMG',null=True) 
      pic_url=models.URLField(max_length=200,default=False)
      date=models.DateTimeField()
      likes=models.IntegerField(default=0)
      types=["Top News","Trending","News","Sports","Health","Children","Life","Tech","Astro","Health","Movie","Carrer","Travel","Home","Auto","Music"]
      newsTypes=[(item,item) for (idx,item) in enumerate(types)]
      type=models.CharField(max_length=30,choices=newsTypes,default="News")
      href=models.URLField(max_length=200,default=False)
      #updated=models.DateTimeField(auto_now=True)
      #author=models.ForeignKey()
      #tags=models.ForeignKey(Tags,on_delete=models.CASCADE,related_name="tags")

      def __str__(self):
            return self.title


class Comment(models.Model):
      newsArticle=models.ForeignKey(NewsArticle,on_delete=models.CASCADE,related_name="article",)
      comment=models.TextField()
      def __str__(self):
            return self.comment

class Tags(models.Model):
      newsArticle=models.ForeignKey(NewsArticle,on_delete=models.CASCADE,related_name="tags",)
      tag=models.CharField(max_length=30,unique=True)
      class Meta:
            verbose_name_plural="Tags"
      def __str__(self):
            return self.tag
