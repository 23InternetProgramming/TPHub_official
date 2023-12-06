from django.urls import path

from . import views
from .views import EventDeleteView

app_name = 'schedule'
urlpatterns = [
    path('index', views.index, name='index'),
    path('createTodo', views.create_todo, name='createTodo'),
    path('deleteTodo', views.deleteTodo, name='deleteTodo'),
    path('', views.CalendarView.as_view(), name='calendar'),  # 수정된 부분
    path('event/new/', views.event, name='event_new'),  # 수정된 부분
    path('event/edit/<int:event_id>/', views.event, name='event_edit'),  # 수정된 부분
    path('event/delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),  # 수정된 부분
]
