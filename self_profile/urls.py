from django.urls import path
from . import views
from django.urls import path
from .views import profile

app_name = 'self_profile'

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('', views.PostList.as_view())

]