from django.shortcuts import render
from . import models
from django.shortcuts import get_object_or_404


def article_view(request, id):
    article = get_object_or_404(models.Article, id=id)
    articles = models.Article.objects.all()
    sidebar = models.Sidebar.objects.all()
    print([article.id for article in articles])  # Debug print

    return render(request, "article/article.html", {
        "article": article,
        "articles": articles,
        "sidebar": sidebar
    })
