# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-18 16:47
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
                ('title', models.CharField(max_length=200)),
                ('complete_status', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False)),
            ],
        ),
    ]
