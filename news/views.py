from django.shortcuts import render
from .models import Category, News
from django.core.paginator import Paginator
from django.db.models import Q




def allNews(request):
    allNews = News.objects.filter(Q(accepted=True)|Q(deleted=False)).order_by('-created')
    p = Paginator(allNews, 9)
    page = request.GET.get('page')
    newsAll = p.get_page(page)
    context = {'newsAll':newsAll}
    return render(request, 'news/allNews.html', context)


def news(request, id):
    newsInfo = News.objects.get(id=id)
    context = {'newsInfo':newsInfo}
    return render(request, 'news/news.html', context)


# def category(request, id):
#     categ = Category.objects.get(id=id)
#     newsInfo = News.objects.filter(category=categ)
#     context = {
#         'newsAll':newsInfo,
#     }
#     return render(request, 'news/allNews.html', context)