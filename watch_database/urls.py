# watch_database/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import index, browse_watches
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('login/', LoginView.as_view(), name='login'),
    path('browse-watches/', browse_watches, name='browse-watches'),
    path('<str:username>/watch-collection/', include('watch_collection.urls'), name='watch-collection'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', include('custom_user.urls'), name='profile'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

