# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0032_auto_20170406_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='staticpages.School'),
        ),
    ]
