from django.views.generic import ListView
from .models import Post
from django.shortcuts import render, redirect


class PostList(ListView):
    model = Post
    ordering = '-pk'
