# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-26 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
