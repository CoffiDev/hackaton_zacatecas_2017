# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.conf import settings
from django.db import models
from users.models import ClientProfile, YoungProfile


class Services(models.Model):

    client = models.ForeignKey(ClientProfile)
    youngs_registered = models.ManyToManyField(YoungProfile, blank=True, null=True)
    youngs_requests = models.ManyToManyField(YoungProfile, blank=True, null=True, related_name='services_requestions')

    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255, choices=settings.LEVEL)
    interest_area = models.CharField(max_length=255, choices=settings.INTEREST_AREA)
    salary = models.IntegerField()

    lat = models.FloatField()
    lon = models.FloatField()
    address = models.CharField(max_length=255)

    description = models.TextField()
    requirements = models.TextField()
    extraInfo = models.TextField()

    def __str__(self):
        return str(self.name)
