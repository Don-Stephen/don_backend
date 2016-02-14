from __future__ import unicode_literals

from django.db import models
# from django.utils.translation import ugettext_lazy as _

class Feature(models.Model):
    language = models.ForeignKey(LanguageConfig)
    description = models.CharField(max_length=255)
    finality = models.CharField(max_length=255)
    who = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    ffile = models.FileField()
    project = models.ForeignKey(Project)


class Scenario(models.Model):

    feature = models.ForeignKey(Feature)
    title = models.CharField(max_length=255)
    given = models.CharField(max_length=255)
    then = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
