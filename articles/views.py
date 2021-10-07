from django import http
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, ArticleModelForm

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

@login_required
def create(request):
    #form = ArticleForm(request.POST or None)
    form = ArticleModelForm(request.POST or None)
    context = {
        "form": form,
    }
    if form.is_valid():
        # print(form.cleaned_data)
        article = form.save()
        context["article"]= article
        context["is_created"]= True

    return render(request, "articles/create.html", context)



def show(request, id):
   pass

@login_required
def edit(request, id):
   pass

@login_required
def delete(request, id):
    pass