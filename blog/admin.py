from django.contrib import admin
from blog.models import BlogType, Blog


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'id')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'id', 'blog_type', 'blog_author', 'blog_create_time', 'blog_update_time')
