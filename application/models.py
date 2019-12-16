# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ApplicationModel(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=50)
