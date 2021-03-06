# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 12:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20170405_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lecturer',
        ),
        migrations.RemoveField(
            model_name='courseinfo',
            name='course',
        ),
        migrations.RemoveField(
            model_name='courseinfo',
            name='students',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
        migrations.AlterField(
            model_name='answer',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 5, 14, 51, 57, 75084)),
        ),
        migrations.AlterField(
            model_name='question',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='question',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 5, 14, 51, 57, 74583)),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='CourseInfo',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
