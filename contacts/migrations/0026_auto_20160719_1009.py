# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0025_remove_company_contact_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ccrelation',
            options={'verbose_name_plural': 'CCRelations'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('company_name',), 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('contact_email',), 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('service_name',), 'verbose_name_plural': 'Services'},
        ),
        migrations.AlterField(
            model_name='companytype',
            name='type_name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Company Type'),
        ),
    ]