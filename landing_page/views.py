from django.views.generic import ListView
from schedule.models import Todo
from .models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        todos = Todo.objects.all()
        context['todos'] = todos
        return context


@login_required
def base(request):
    return render(request, 'landing_page/base.html')
