# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 15:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0016_auto_20160712_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='ccrelation',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation Date'),
        ),
        migrations.AddField(
            model_name='contact',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation Date'),
        ),
        migrations.AlterField(
            model_name='service',
            name='delete_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Delete Date'),
        ),
    ]
