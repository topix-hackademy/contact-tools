# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-17 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0038_auto_20161014_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_mailingaddress',
            field=models.TextField(blank=True, null=True, verbose_name='Mailing Address'),
        ),
    ]