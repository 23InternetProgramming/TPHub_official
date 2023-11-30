from django.conf.urls import url
from . import views
from .views import EventDeleteView

app_name = 'schedule'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    url(r'^event/delete/(?P<pk>\d+)/$', EventDeleteView.as_view(), name='event_delete'),
]