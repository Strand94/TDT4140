# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_auto_20170324_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staticpages.School'),
        ),
    ]