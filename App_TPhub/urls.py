from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing_page.urls')),
    path('schedule/', include('schedule.urls')),
    path('board/', include('board.urls')),
    path('member/', include('member.urls')),
    path('etc/', include('etc.urls')),
    path('self_profile/', include('self_profile.urls')),
    path('account/', include('account.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
