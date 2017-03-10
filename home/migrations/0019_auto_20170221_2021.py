# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_uvaproblems'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='propic',
            field=models.FileField(default=b'http://www.freeiconspng.com/uploads/profile-icon-9.png', upload_to=b''),
        ),
        migrations.AddField(
            model_name='uvaproblems',
            name='category',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bio',
            name='about',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bio',
            name='current_add',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bio',
            name='permanent_add',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]