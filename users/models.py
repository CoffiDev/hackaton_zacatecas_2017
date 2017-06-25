# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    first_name = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to="profile")

    def __str__(self):
        return str(self.user)


class ClientProfile(Profile):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=255)


class YoungProfile(Profile):
    user = models.OneToOneField(User)
    level = models.CharField(max_length=255)
    interest_area = models.CharField(max_length=255)
    description = models.TextField()
