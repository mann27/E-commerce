# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class profile(models.Model):
    name= models.CharField(max_length=120)
    discription = models.TextField(default= 'discription default text ')
    # Instead of default u can also accept null . Use null=True for ignoring errors in making migrations.
    def __unicode__(self):
        return self.name