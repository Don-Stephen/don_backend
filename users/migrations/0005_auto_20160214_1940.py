# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160207_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='language',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='project',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='scenario',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
        migrations.DeleteModel(
            name='Scenario',
        ),
    ]
