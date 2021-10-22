from django.contrib import admin
from News_App.models import * 
from User_App.models import *

class NewsArticleAdminInline(admin.StackedInline):
    model=Comment

class NewsArticleAdmin(admin.ModelAdmin):
    search_fields=['title','body']
    list_filter=['date','type']
    list_display=['title','date','type']
    readonly_fields = ('id','likes')
    fields=['title','body',('pic','pic_url'),('likes','type'),'date','href','id','priority']
    ordering=['-date']
    #readonly_fields=['date']
    #inlines=[NewsArticleAdminInline]

# Register your models here.
admin.site.register(NewsArticle,NewsArticleAdmin)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Tags)

