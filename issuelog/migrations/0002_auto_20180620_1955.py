# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuelog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(default='bug', max_length=10),
        ),
    ]
