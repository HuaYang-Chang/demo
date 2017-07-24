# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0003_auto_20170508_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_Bid',
            fields=[
                ('list_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('bid_txid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_auth.Bid')),
            ],
        ),
    ]