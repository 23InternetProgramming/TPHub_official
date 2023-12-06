from django.db import models
from django.contrib.auth.models import User
import os
#from self_profile.models import UserProfile


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    #user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        truncated_content = self.content[:10] + '...' if len(self.content) > 10 else self.content
        return f'[{self.pk}] :: {self.title} >> {truncated_content}'
