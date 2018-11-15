from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', blog, name='blog'),
    path('<int:id>', blog_detail, name='blog_detail'),
    path('type/<int:id>', blog_type, name='blog_type'),
]