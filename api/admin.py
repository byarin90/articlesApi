from django.contrib import admin

# Register your models here.
from .models import Article




# admin.site.register(Article)

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    # filter cols
    list_filter = ('title','description')
    #display cols
    list_display = ('title','description')
    