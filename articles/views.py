from django.shortcuts import render,redirect

import articles
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:index')
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html',context)
