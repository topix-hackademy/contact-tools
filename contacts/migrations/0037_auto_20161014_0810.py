# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-14 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0036_auto_20161013_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(default='logos/nologo.png', help_text='Company logo', upload_to='logos/'),
        ),
    ]
