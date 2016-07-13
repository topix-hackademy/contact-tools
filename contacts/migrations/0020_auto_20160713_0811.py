# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0019_auto_20160713_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_tax_code',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='Tax Code'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_vat_number',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='VAT Number'),
        ),
    ]
