# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0010_auto_20171011_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='dlda',
            name='res10',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='dlda',
            name='res3',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='dlda',
            name='res4',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='dlda',
            name='res5',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='dlda',
            name='res6',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='dlda',
            name='res7',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='dlda',
            name='res8',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='dlda',
            name='res9',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res10',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res3',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res4',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res5',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res6',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res7',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res8',
            field=models.IntegerField(default=True),
        ),
        migrations.AddField(
            model_name='oopm',
            name='res9',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='dlda',
            name='res1',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='dlda',
            name='res2',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='oopm',
            name='res1',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='oopm',
            name='res2',
            field=models.IntegerField(default=True),
        ),
    ]