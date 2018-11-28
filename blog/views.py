from django.shortcuts import get_object_or_404, render_to_response
from blog.models import Blog, BlogType, ReadNum
from django.core.paginator import Paginator as pagetool
import random


# 博客文章列表
def blog_list(request):
    # 分页
    # 获取显示的分类
    types = getTypes()
    allBlogList = Blog.objects.filter(blog_type__in=types)  # 获取显示的所有文章
    paginator = pagetool(allBlogList, 8)  # 每8篇文章分页
    pagenum = request.GET.get('page', 1)  # 当前get请求的page
    page = paginator.get_page(pagenum)  # 获取分页的8篇文章
    page_now = page.number
    page_range = list(range(max(page_now - 4, 1), page_now)) + list(
        range(page_now, min(page_now + 4, paginator.num_pages) + 1))

    context = {}
    context['blogs'] = page.object_list
    context['page'] = page
    context['page_range'] = page_range
    context['types'] = types
    context['random_blogs'] = randomPost()
    return render_to_response('blog_list.html', context=context)


# 具体的某篇文章
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    if not request.COOKIES.get('blog_%s_read' % id):
        if ReadNum.objects.filter(blog=blog).count():
            # 存在此篇文章的阅读量
            readnum = ReadNum.objects.get(blog=blog)
        else:
            readnum = ReadNum(blog=blog)
        readnum.read_num += 1
        readnum.save()
    # 获取不隐藏分类
    types = getTypes()
    context = {}
    context['types'] = types
    context['blog'] = blog
    context['random_blogs'] = randomPost()
    response = render_to_response('blog_detail.html', context)
    response.set_cookie('blog_%s_read' % id, 'true')
    return response


# 某个具体的分类
def blog_type(request, id):
    blog_type = get_object_or_404(BlogType, id=id)

    # 分页
    allBlogList = Blog.objects.filter(blog_type=blog_type)  # 获取所有文章
    paginator = pagetool(allBlogList, 8)  # 每8篇文章分页
    pagenum = request.GET.get('page', 1)  # 当前get请求的page
    page = paginator.get_page(pagenum)  # 获取分页的8篇文章
    page_now = page.number
    page_range = list(range(max(page_now - 4, 1), page_now)) + list(
        range(page_now, min(page_now + 4, paginator.num_pages) + 1))

    types = getTypes()
    context = {}
    context['blog_type'] = blog_type
    context['blogs'] = page.object_list
    context['page'] = page
    context['page_range'] = page_range
    context['types'] = types
    context['random_blogs'] = randomPost()
    return render_to_response('blog_list.html', context)


# 获取显示的文章分类
def getTypes():
    types = BlogType.objects.all().filter(hide=False)
    return types


def randomPost():
    blogs = Blog.objects.filter(blog_type__hide=False)
    count = 10
    random_blogs = random.sample(list(blogs), count)
    return list(random_blogs[:count])
