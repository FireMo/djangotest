# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "publish"]
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ['publish', 'author']


# 将BlogArticles类注册到admin中
admin.site.register(BlogArticles, BlogArticlesAdmin)
# admin.site.register(BlogArticles)


