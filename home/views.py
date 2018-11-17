from django.shortcuts import render_to_response
from blog.models import Blog


# 首页
def home(request):
    count = Blog.objects.count()
    context = {}
    context['count'] = count
    return render_to_response('home.html', context=context)
