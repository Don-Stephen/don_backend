# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160214_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='location',
        ),
    ]
