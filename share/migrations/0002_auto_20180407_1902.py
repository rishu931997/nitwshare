# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-04-07 19:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowrequest',
            name='owner',
        ),
        migrations.AddField(
            model_name='borrowrequest',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='share.Item'),
        ),
    ]
