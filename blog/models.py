from django.db import models
from django.contrib.auth.models import User


class BlogType(models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    blog_title = models.CharField(max_length=15)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    blog_content = models.TextField()
    blog_author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    blog_create_time = models.DateTimeField(auto_now_add=True)
    blog_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title
