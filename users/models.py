from __future__ import unicode_literals

from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class LanguageConfig(models.Model):
    language = models.CharField(max_length=255)
    language_plugin = models.CharField(max_length=255)

    def __unicode__(self):
        return self.language


class SenderConfig(models.Model):
    type = models.CharField(max_length=255)
    user = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    meta_data = models.TextField()

    def __unicode__(self):
        return self.type


class User(AbstractUser):

    def __unicode__(self):
        return self.username


class Project(models.Model):

    name = models.CharField(max_length=255)
    languages = models.ManyToManyField(LanguageConfig)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name