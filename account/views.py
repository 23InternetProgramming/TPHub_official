# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Account

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {}
        if not (username and password and re_password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."
        else:
            user = Account(username=username, password=make_password(password))
            user.save()
        return render(request, 'signup.html', res_data)
    else:
        return render(request, 'signup.html')

