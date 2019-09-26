from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# 모든 article 을 보여주는 페이지
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# Get 으로 들어오면 생성하는 페이지 rendering
# Post 로 들어오면 생성
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')
        # client 가 입력을 잘못입력했을 때 입력값을 그대로 다시 보여줌
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
