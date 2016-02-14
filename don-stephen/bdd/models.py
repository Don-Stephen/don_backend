from __future__ import unicode_literals

from django.db import models
from users.models import LanguageConfig, Project, Tag
# from django.utils.translation import ugettext_lazy as _

class Feature(models.Model):
    language = models.ForeignKey(LanguageConfig)
    description = models.CharField(max_length=255)
    finality = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    ffile = models.FileField()
    project = models.ForeignKey(Project)


    def __unicode__(self):
        return self.description

class Background(models.Model):
    pass

class Scenario(models.Model):
    feature = models.ForeignKey(Feature)
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __unicode__(self):
        return self.title


class Given(models.Model):
    content = models.CharField(max_length=255)
    scenario = models.ForeignKey(Scenario)
    background = models.ForeignKey(Background)

    def __unicode__(self):
        return self.content


class When(models.Model):
    content = models.CharField(max_length=255)
    scenario = models.ForeignKey(Scenario)

    def __unicode__(self):
        return self.content

class Then(models.Model):
    content = models.CharField(max_length=255)
    scenario = models.ForeignKey(Scenario)

    def __unicode__(self):
        return self.content

class And(models.Model):
    content = models.CharField(max_length=255)
    related_to = models.CharField(max_length=255, choices=[('given', 'given'), ('then', 'then'), ('when', 'when')])
    table = models.TextField()
    background = models.ForeignKey(Background)
    scenario = models.ForeignKey(Scenario)

    def __unicode__(self):
        return self.content
