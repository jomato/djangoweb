# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-14 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20170414_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.Category', verbose_name='分类'),
        ),
    ]