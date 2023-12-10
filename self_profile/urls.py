from django.urls import path
from . import views
from .views import view_profile, user_profile_update_form

app_name = 'self_profile'

urlpatterns = [
    #path('', views.PostList.as_view()),
    path('', views.view_profile, name='view_profile'),
    #path('view_profile/', views.view_profile, name='view_profile'),
    path('user_profile_update_form/', user_profile_update_form, name='user_profile_update_form'),
]
