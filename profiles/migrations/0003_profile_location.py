# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-21 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='my location default', max_length=120),
        ),
    ]
