from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


def all_blogs(request):
    blogs = Blog.objects.all()

    paginator = Paginator(blogs, 2)  # По 3 статьи на каждой странице
    try:
        page = request.GET.get('page')  # извлекаем из запроса GET-параметр page,который указывает текущую страницу
    except:
        page = 1
        raise Exception

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/all_blogs.html', context={'blogs': blogs,
                                                           'page': page,
                                                           'posts': posts})


def details(request, blog_id):
    post = get_object_or_404(Blog, id=blog_id)

    return render(request, 'blog/details.html', {'post': post})
