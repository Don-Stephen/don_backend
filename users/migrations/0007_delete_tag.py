# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdd', '0003_auto_20160313_1941'),
        ('users', '0006_remove_project_location'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
