# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


# 该函数被称为视图函数，参数request负责响应所接受到的请求且不能少，总是位于第一的位置
def blog_title(request):
    blogs = BlogArticles.objects.all()
    # render模板渲染
    return render(request, "blog/title.html", {"blogs": blogs})


# 响应查看文章详情的请求
def blog_article(request, article_id):
    article = BlogArticles.objects.get(id=article_id)
    # 对超索引的请求进行404处理
    # article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": pub})
