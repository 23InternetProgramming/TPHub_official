from django.views.generic import ListView
from .models import Post
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class PostList(ListView):
    model = Post
    ordering = '-pk'


@login_required
def profile(request):
    # Access user information using request.user
    user_info = {
        'username': request.user.username,
        'name': request.user.first_name,
        'student_id': request.user.profile.student_id,  # Assuming you have a UserProfile model with a student_id field
        'major': request.user.profile.major,  # Assuming you have a UserProfile model with a major field
    }
    return render(request, 'self_profile/profile.html', {'user_info': user_info})


def base(request):
    return render(request, 'landing_page/base.html')
