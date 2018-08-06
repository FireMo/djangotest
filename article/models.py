# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ArticleColumn(models.Model):
    # 用户与文章为一对多的关系
    user = models.ForeignKey(User, related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column


