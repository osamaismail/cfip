from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q





def allBlogs(request):
    allBlogs = Blog.objects.filter(Q(accepted=True)|Q(deleted=False)).order_by('-created')
    p = Paginator(allBlogs, 9)
    page = request.GET.get('page')
    blogsAll = p.get_page(page)
    context = {'blogsAll':blogsAll}
    return render(request, 'blog/allBlogs.html', context)


def blog(request, id):
    blogInfo = Blog.objects.get(id=id)
    context = {'blogInfo':blogInfo}
    return render(request, 'blog/blog.html', context)


# def category(request, id):
#     categ = BlogCategory.objects.get(id=id)
#     blogsAll = Blog.objects.filter(category=categ)
#     context = {
#         'blogsAll':blogsAll,
#     }
#     return render(request, 'blog/allBlogs.html', context)