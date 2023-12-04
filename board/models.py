from django.db import models
from django.contrib.auth.models import User
import os


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    hook_text = models.CharField(max_length=100, blank=True)
    head_image = models.ImageField(upload_to='board/category_images/%Y/%m/%d/', blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/board/category/{self.slug}'

    def get_queryset(self):
        return self.post_set.order_by('-pk')


# User 모델을
# Subclassing (하위 클래스화): 기존 User 모델을 상속하고 새로운 필드를 추가하는 방법입니다.
# 방법으로 전화번호, 학번, 프로필 이미지 등 새로운 필드 넣기
# member App에서 해야하나..

class Post(models.Model):
    title = models.CharField(max_length=30)
    # 현재 로그인된 유저를 자동으로 가져와야 함
    author = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, blank=False, on_delete=models.SET_NULL)

    content = models.TextField()
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    # 현재 로그인된 유저의 프로필 이미지를 가져와야 함
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        truncated_content = self.content[:10] + '...' if len(self.content) > 10 else self.content
        return f'[{self.pk}] | {self.category} | {self.author}) {self.title} : {truncated_content}'

    # def change_ordering(self):
    #     self.ordering = 'pk' if self.ordering_state else '-pk'
    #     self.ordering_state = not self.ordering_state

    def get_absolute_url(self):
        return f'/board/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # slug =

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
