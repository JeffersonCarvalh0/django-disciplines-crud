# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Discipline(models.Model):
    '''
        Represents the discipline in database
    '''
    name = models.CharField(max_length=60)
    short = models.CharField(max_length=20)
    hours = models.IntegerField()
    email = models.EmailField()
    active = models.BooleanField(default=True)
    url = models.URLField(blank=True)
