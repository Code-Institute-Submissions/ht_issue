# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issuelog', '0002_auto_20180620_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
