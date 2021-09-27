import articles
from django import http
from django.db.models import query
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .models import Article
# from django.template.loader import render_to_string, get_template

# Create your views here.


def index(request):
    article_list = Article.objects.all()
    context = {
        "article_list": article_list,
    }

    return render(request, "articles/index.html", context)

def search(request):
    search = request.GET

    queryset = get_object_or_404(Article, id= search.get("query"))
    context = {
        'article': queryset,
    }
    return render(request, "articles/search.html", context)

def create(request):
    context = {}
    if request.method == "POST":
        title= request.POST.get("title")
        content= request.POST.get("content")
        article= Article.objects.create(title= title, content= content)
        context["article"]= article
        context["is_created"]= True

    return render(request, "articles/create.html", context)



def show(request, id):
   pass

def edit(request, id):
   pass

def delete(request, id):
    pass