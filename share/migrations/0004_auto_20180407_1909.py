# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-04-07 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20180407_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowrequest',
            name='approvalDate',
            field=models.DateField(null=True),
        ),
    ]
