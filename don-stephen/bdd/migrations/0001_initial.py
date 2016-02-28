# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_project_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='And',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(max_length=255)),
                ('related_to', models.CharField(choices=[('given', 'given'), ('then', 'then'), ('when', 'when')], max_length=255)),
                ('table', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=255)),
                ('finality', models.CharField(max_length=255)),
                ('who', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('ffile', models.FileField(upload_to='')),
                ('language', models.ForeignKey(to='users.LanguageConfig')),
                ('project', models.ForeignKey(to='users.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Given',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(max_length=255)),
                ('background', models.ForeignKey(to='bdd.Background', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('feature', models.ForeignKey(to='bdd.Feature')),
                ('tags', models.ManyToManyField(to='users.Tag', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Then',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(max_length=255)),
                ('scenario', models.ForeignKey(to='bdd.Scenario')),
            ],
        ),
        migrations.CreateModel(
            name='When',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(max_length=255)),
                ('scenario', models.ForeignKey(to='bdd.Scenario')),
            ],
        ),
        migrations.AddField(
            model_name='given',
            name='scenario',
            field=models.ForeignKey(to='bdd.Scenario', null=True),
        ),
        migrations.AddField(
            model_name='and',
            name='background',
            field=models.ForeignKey(to='bdd.Background', null=True),
        ),
        migrations.AddField(
            model_name='and',
            name='scenario',
            field=models.ForeignKey(to='bdd.Scenario', null=True),
        ),
    ]
