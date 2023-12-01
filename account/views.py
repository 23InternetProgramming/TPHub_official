from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from member.models import Post
from self_profile.models import Post

@login_required
def base(request):
    if request.method == 'POST':
        # 회원가입 시에 입력한 정보를 member 앱과 self_profile 앱의 post_list에 저장하는 코드 작성
        student_id = request.POST['student_id']
        major = request.POST['major']
        post = Post(student_id=student_id, major=major)
        post.save()
        post_list = Post(user=request.user, post=post)
        post_list.save()
    return render(request, 'landing_page/base.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page:base')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page:base')
        else:
            return redirect('account:login')
    return render(request, 'account/login.html')
