# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-19 18:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='by_user',
            field=models.TextField(default='', max_length=100),
        ),
    ]