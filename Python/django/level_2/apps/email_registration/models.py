# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models

class User(models.Model):

    email = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
