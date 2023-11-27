from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signup/', views.signup, name="signup"),#회원가입시에는 views.py의 signup함수를 요청
    path('login/', views.login, name="login"),#로그인시에는 views.py의 lognin 함수를 요청
    path('logout/', views.logout, name="logout"),

]
