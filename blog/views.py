# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import BlogArticles


# 该函数被称为视图函数，参数request负责响应所接受到的请求且不能少，总是位于第一的位置
def blog_title(request):
    blogs = BlogArticles.objects.all()
    # render模板渲染
    return render(request, "blog/title.html", {"blog": blogs})

# Create your views here.
