from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from self_profile.forms import UserProfileForm
from self_profile.models import UserProfile, Post


@login_required
def view_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 성공적으로 저장되었습니다.')
            return redirect('self_profile:view_profile')
        else:
            messages.error(request, '프로필 저장 중 오류가 발생했습니다.')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form
    }
    return render(request, 'self_profile/post_list.html', context)


@login_required
def user_profile_update_form(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('self_profile:view_profile')
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form
    }
    return render(request, 'self_profile/user_profile_update_form.html', context)


class PostList(ListView):
    model = Post
    ordering = '-pk'
