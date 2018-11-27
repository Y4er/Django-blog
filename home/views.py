from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, BlogType


# 首页
def home(request):
    count = Blog.objects.count()
    type_notice = get_object_or_404(BlogType, hide=True)  # 获取不显示的文章分类
    notice = Blog.objects.filter(blog_type=type_notice)[:min(count, 7)]  # 取最新的7篇
    context = {}
    context['count'] = count
    context['notice'] = notice
    return render_to_response('home.html', context=context)
