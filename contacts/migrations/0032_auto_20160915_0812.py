# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0031_auto_20160728_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_custom_id',
            field=models.IntegerField(null=True, verbose_name='Custom ID', blank=True),
        ),
    ]
