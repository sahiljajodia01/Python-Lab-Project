# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-29 18:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='AOA', max_length=250)),
                ('fac', models.CharField(default='', max_length=250)),
                ('res1', models.IntegerField(default=1)),
                ('res2', models.IntegerField(default=1)),
                ('res3', models.IntegerField(default=1)),
                ('res4', models.IntegerField(default=1)),
                ('res5', models.IntegerField(default=1)),
                ('res6', models.IntegerField(default=1)),
                ('res7', models.IntegerField(default=1)),
                ('res8', models.IntegerField(default=1)),
                ('res9', models.IntegerField(default=1)),
                ('a', models.CharField(max_length=50)),
                ('sug', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=50)),
                ('lname', models.CharField(blank=True, max_length=50)),
                ('sap_id', models.BigIntegerField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(default=60004160045, on_delete=django.db.models.deletion.CASCADE, to='appOne.UserProfile'),
        ),
    ]
