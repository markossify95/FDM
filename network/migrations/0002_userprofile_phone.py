# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-25 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='N/A', max_length=15),
        ),
    ]