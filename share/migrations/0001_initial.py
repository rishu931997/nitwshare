# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-04-07 11:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, b'Requested'), (2, b'Accepted'), (3, b'Rejected'), (4, b'Completed')], default=1)),
                ('description', models.CharField(max_length=512, null=True)),
                ('requestDate', models.DateField(default=datetime.date.today)),
                ('approvalDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemType', models.CharField(max_length=20)),
                ('status', models.IntegerField(choices=[(1, b'Available'), (2, b'Requested'), (3, b'Borrowed')], default=1)),
                ('title', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('regNum', models.CharField(max_length=10)),
                ('course', models.CharField(choices=[(b'BTech', b'B.Tech'), (b'MTech', b'M.Tech'), (b'MCA', b'MCA'), (b'MBA', b'MBA'), (b'PHD', b'Phd')], default=b'BTech', max_length=10)),
                ('branch', models.CharField(choices=[(b'CSE', b'Computer Science & Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'MECH', b'Mechanical Engineering'), (b'MME', b'Metallurgy Engineering'), (b'CHE', b'Chemical Engineering'), (b'CIVIL', b'Civil Engineering'), (b'EEE', b'Electrical and Electronics Engineering'), (b'BIO', b'Biotechnology')], max_length=10)),
                ('contact', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='borrowrequest',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Item_borrower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='borrowrequest',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='I_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
