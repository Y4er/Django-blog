from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, BlogType


# 首页
def home(request):
    # 计数
    count = Blog.objects.count()
    # 公告
    notice = Blog.objects.filter(blog_type__hide=True)[:min(count, 10)]  # 取最新的7篇
    # 最近更新
    last_blogs = Blog.objects.filter(blog_type__hide=False)[:min(count, 10)]
    context = {}
    context['count'] = count
    context['notice'] = notice
    context['last_blogs'] = last_blogs
    return render_to_response('home.html', context=context)
