# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255)


class ClientProfile(Profile):
    pass


class YoungProfile(Profile):

    level = models.CharField(max_length=255)
    interest_area = models.CharField(max_length=255)
    description = models.TextField()
