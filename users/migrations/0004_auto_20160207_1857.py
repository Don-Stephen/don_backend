# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151220_2034'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proyect',
            new_name='Project',
        ),
        migrations.RenameField(
            model_name='feature',
            old_name='proyect',
            new_name='project',
        ),
        migrations.AlterField(
            model_name='scenario',
            name='tags',
            field=models.ManyToManyField(to='users.Tag', blank=True, null=True),
        ),
    ]
