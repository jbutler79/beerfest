# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbtf', '0002_auto_20160204_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='wordpress_logo_url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='beer',
            name='description',
            field=models.TextField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
