# views.py
from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from self_profile.models import UserProfile
from django.urls import reverse
from django.contrib import messages


@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not UserProfile.objects.filter(user=user).exists():
                UserProfile.objects.create(
                    user=user,
                    name=user.name,
                    student_id='',
                    major='',
                    email=user.email,
                    phone_number='',
                    role='',
                    git='',
                    instagram='',
                    facebook=''
                )
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, '회원가입에 실패했습니다.')
            return render(request, 'account/signup.html', {'form': form})
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'account/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')
