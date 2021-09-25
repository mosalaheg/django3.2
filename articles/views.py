from django import http
from articles.models import Article
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.template.loader import render_to_string, get_template

# Create your views here.


def index(request):
    article_obj = Article.objects.get(id=1)
    context = {
        "article_obj": article_obj
    }
    # html_string = render_to_string("index.html", context)
    html_temp = get_template("index.html")
    html_string =html_temp.render(context)
    return HttpResponse(html_string)