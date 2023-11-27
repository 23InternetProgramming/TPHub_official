from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth import authenticate
from .models import Selfprofile


# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST["1st_password"] == request.POST["2nd_password"]:
            user = User.objects.create_user(username=request.POST["username"],
                                            password=request.POST["1st_password"],
                                            email=request.POST["email"],
                                            schoolid=request.POST["schoolid"],
                                            major=request.POST["major"])
            profile = Selfprofile(user=user)#signup 함수에서 user등록 시 Selfprofile과 엮어주기
            profile.save()
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
