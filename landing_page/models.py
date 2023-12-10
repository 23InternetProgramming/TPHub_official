from django.db import models
from django.contrib.auth.models import User
import os


class Landing(models.Model):

    def __str__(self):
        return f'[{self.pk}]'
