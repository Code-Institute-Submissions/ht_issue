# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0002_auto_20180626_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmgr',
            name='email',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='productmgr',
            name='mgr',
            field=models.CharField(max_length=40),
        ),
    ]