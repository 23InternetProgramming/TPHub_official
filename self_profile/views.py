from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Post
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from self_profile.forms import UserProfileForm


@login_required
def save_profile(request):
    if request.method == 'POST':
        user_profile = request.user.userprofile
        user_profile.name = request.POST.get('name')
        user_profile.student_id = request.POST.get('student_id')
        user_profile.major = request.POST.get('major')
        user_profile.email = request.POST.get('email')
        user_profile.phone_number = f"{request.POST.get('phone1')}-{request.POST.get('phone2')}-{request.POST.get('phone3')}"
        user_profile.role = request.POST.get('role')
        user_profile.git = request.POST.get('git')
        user_profile.instagram = request.POST.get('instagram')
        user_profile.facebook = request.POST.get('facebook')
        user_profile.save()

        messages.success(request, '프로필이 성공적으로 저장되었습니다.')

        return redirect('self_profile:post_list')


@login_required
def post_list(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'self_profile/post_list.html', context)


class PostList(ListView):
    model = Post
    ordering = '-pk'
