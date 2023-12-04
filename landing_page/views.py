from django.views.generic import ListView
from .models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class PostList(ListView):
    model = Post
    ordering = '-pk'


@login_required
def base(request):
    return render(request, 'landing_page/base.html')
