from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Post
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from self_profile.forms import UserProfileForm


@login_required
def save_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            # 추가된 정보도 저장되도록 수정
            form.save()
            messages.success(request, '프로필이 성공적으로 저장되었습니다.')
            return redirect('self_profile:post_list')
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
def post_list(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 성공적으로 저장되었습니다.')
            return redirect('self_profile:post_list')
        else:
            messages.error(request, '프로필 저장 중 오류가 발생했습니다.')
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
