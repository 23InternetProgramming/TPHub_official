from django.urls import path
from . import views
from django.urls import path
from .views import save_profile

app_name = 'self_profile'

urlpatterns = [
    path('', views.PostList.as_view()),
    path('save_profile/', save_profile, name='save_profile'),

]