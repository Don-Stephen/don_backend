# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdd', '0002_auto_20160313_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='and',
            name='background',
        ),
        migrations.RemoveField(
            model_name='and',
            name='scenario',
        ),
        migrations.AlterField(
            model_name='scenario',
            name='tags',
            field=models.ManyToManyField(blank=True, to='bdd.Tag', null=True),
        ),
        migrations.DeleteModel(
            name='And',
        ),
    ]
