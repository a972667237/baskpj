# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-06-13 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baskuser',
            options={'verbose_name': 'member', 'verbose_name_plural': 'member'},
        ),
        migrations.AlterField(
            model_name='baskuser',
            name='nick',
            field=models.CharField(max_length=100, verbose_name=b'nickname'),
        ),
    ]
