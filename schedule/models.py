from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('schedule:event_edit', args=(self.pk,))
        return f'<a href="{url}"> {self.title} </a>'

class Todo(models.Model):
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] | {self.author}) {self.content[:10]}'

