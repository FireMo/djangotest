# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-07-24 03:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]