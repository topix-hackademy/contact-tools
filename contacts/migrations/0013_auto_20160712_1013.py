# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 10:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200, verbose_name='Contact Type')),
                ('is_valid', models.BooleanField(default=True, verbose_name='Is Valid')),
                ('creation_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation Date')),
            ],
            options={
                'ordering': ('type_name',),
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('contact_email',)},
        ),
    ]