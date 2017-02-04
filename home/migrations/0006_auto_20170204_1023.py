# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-04 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170204_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='about',
            name='image_url',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image_url',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='recent',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='recent',
            name='image_url',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='upcoming',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]