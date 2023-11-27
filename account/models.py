from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=32, verbose_name='계정이름')
    password = models.CharField(max_length=32, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'test_user'


class Selfprofile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    profileImg = models.ImageField(upload_to='profileImg', blank=True)
    nickName = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True),
    email = models.CharField(max_length=30, blank=True)
