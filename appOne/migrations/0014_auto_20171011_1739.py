# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0013_auto_20171011_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='am3',
            name='fac',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='am3',
            name='subject',
            field=models.CharField(default='', max_length=250),
        ),
    ]