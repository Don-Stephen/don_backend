# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bdd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='background',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='features', to='bdd.Background'),
        ),
    ]
