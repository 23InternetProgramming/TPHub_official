from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    student_id = models.CharField(max_length=10)
    major = models.CharField(max_length=50)
