from django.shortcuts import get_object_or_404, render_to_response
from blog.models import Blog, BlogType


# 首页
def blog(request):
    context = {}
    context['blogs'] = Blog.objects.all();
    return render_to_response('blog_home.html', context=context)


# 具体的某篇文章
def blog_detail(request, id):
    context = {}
    context['blog'] = get_object_or_404(Blog, id=id)
    return render_to_response('blog_detail.html', context)


# 某个具体的分类
def blog_type(request, id):
    context = {}
    blog_type = get_object_or_404(BlogType, id=id)
    context['blog_type'] = blog_type
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    return render_to_response('blog_type.html', context)
