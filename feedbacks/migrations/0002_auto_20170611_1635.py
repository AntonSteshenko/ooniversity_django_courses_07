# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-11 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
