from django.shortcuts import get_object_or_404, render_to_response
from blog.models import Blog, BlogType
from django.db.models import Q      # ~Q filter取反
from django.core.paginator import Paginator as pagetool


# 博客文章列表
def blog_list(request):
    # 获取不显示的文章分类
    type_notice = get_object_or_404(BlogType, hide=True)
    # 分页
    allBlogList = Blog.objects.all().filter(~Q(blog_type=type_notice))  # 获取所有文章
    paginator = pagetool(allBlogList, 8)  # 每8篇文章分页
    pagenum = request.GET.get('page', 1)  # 当前get请求的page
    page = paginator.get_page(pagenum)  # 获取分页的8篇文章
    page_now = page.number
    page_range = list(range(max(page_now - 4, 1), page_now)) + list(
        range(page_now, min(page_now + 4, paginator.num_pages) + 1))

    # 分类列表
    types = BlogType.objects.all()

    context = {}
    context['blogs'] = page.object_list
    context['page'] = page
    context['page_range'] = page_range
    context['types'] = types
    return render_to_response('blog_list.html', context=context)


# 具体的某篇文章
def blog_detail(request, id):
    context = {}

    types = BlogType.objects.all()
    context['types'] = types
    context['blog'] = get_object_or_404(Blog, id=id)
    return render_to_response('blog_detail.html', context)


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

    types = BlogType.objects.all()

    context = {}
    context['blog_type'] = blog_type
    context['blogs'] = page.object_list
    context['page'] = page
    context['page_range'] = page_range
    context['types'] = types

    return render_to_response('blog_list.html', context)

# TODO 按作者分类
