# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20160228_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
