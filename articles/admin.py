from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "content"]
    search_fields = ["title", "content"]
    list_per_page = 25
    list_display_links = ["id", "title"]
admin.site.register(Article, ArticleAdmin)
