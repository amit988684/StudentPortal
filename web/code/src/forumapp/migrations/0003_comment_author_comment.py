# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-04 18:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forumapp', '0002_auto_20180304_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_comment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
