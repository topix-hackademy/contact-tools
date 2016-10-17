# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-14 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0037_auto_20161014_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_tax_code',
            field=models.CharField(blank=True, help_text='(eg. codice fiscale)', max_length=30, null=True, verbose_name='Tax Code'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_vat_number',
            field=models.CharField(blank=True, help_text='international VAT number (eg. partita IVA)', max_length=30, null=True, verbose_name='VAT Number'),
        ),
    ]
