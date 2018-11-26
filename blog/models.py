from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField


class BlogType(models.Model):
    type_name = models.CharField(verbose_name="文章分类", max_length=10)
    hide = models.BooleanField(verbose_name="隐藏", default=False)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    blog_title = models.CharField(verbose_name="文章标题", max_length=15)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name="文章分类")
    # blog_content = models.TextField(verbose_name="文章内容")
    blog_content = MDTextField(verbose_name="文章内容")
    blog_author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="文章作者")
    blog_create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    blog_update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    ishide = models.ForeignKey(BlogType, related_name="ishide", on_delete=models.DO_NOTHING, verbose_name="隐藏吗？")

    # 后台显示缩略名 并倒序
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-blog_update_time']

    def __str__(self):
        return self.blog_title
