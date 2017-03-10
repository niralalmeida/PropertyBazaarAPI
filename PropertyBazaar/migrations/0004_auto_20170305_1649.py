# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyBazaar', '0003_auto_20170305_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL),
        ),
    ]
