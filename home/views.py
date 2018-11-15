from django.shortcuts import render_to_response


# 首页
def home(request):
    context = {}
    return render_to_response('home.html', context=context)
