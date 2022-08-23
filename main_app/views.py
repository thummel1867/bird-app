from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.


def home(request):
    #   return render(request, 'main_app/home.html')
    return HttpResponse("Home")


def about(request):
    return render(request, 'main_app/about.html')


def articles_index(request):
    articles = Article.objects.all()
    return render(request, 'main_app/cats/index.html', {'articles': articles})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'main_app/cats/detail.html', {'article': article})

