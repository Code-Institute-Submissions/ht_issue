# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuelog', '0006_auto_20180621_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_status',
            field=models.CharField(choices=[('open', 'open'), ('pending', 'pending'), ('closed', 'closed')], default='open', max_length=10),
        ),
    ]
