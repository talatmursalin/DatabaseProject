# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20170218_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminpost',
            name='title',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='adminpost',
            name='date',
            field=models.CharField(default=b'2017-06-23 10:06:58', max_length=100),
        ),
    ]
