# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete_status = models.BooleanField(default=False)
    private = models.BooleanField(default=True)
    author = models.ForeignKey('auth.User', related_name='tasks', 
                                            on_delete=models.CASCADE)
