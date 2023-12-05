from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        truncated_content = self.content[:10] + '...' if len(self.content) > 10 else self.content
        return f'[{self.pk}] :: {self.title} >> {truncated_content}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    username = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    student_id = models.CharField(max_length=8, blank=True)
    major = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10)
    git = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username
