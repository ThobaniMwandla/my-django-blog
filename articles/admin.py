from nntplib import ArticleInfo
from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    listdisplay = ('title', 'published', 'author')
