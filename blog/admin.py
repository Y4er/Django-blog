from django.contrib import admin
from blog.models import BlogType, Blog


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name', 'id', 'hide']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_title', 'ishide', 'blog_type', 'blog_content', 'blog_author', 'blog_create_time',
                    'blog_update_time']
