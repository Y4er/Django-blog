from django.contrib import admin
from blog.models import BlogType, Blog


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_title', 'blog_type', 'blog_author', 'blog_create_time', 'blog_update_time')
