# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-24 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0007_auto_20191024_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='bidding_time',
        ),
        migrations.AddField(
            model_name='artifact',
            name='end_bidding_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]