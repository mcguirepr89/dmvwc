# custom_user/urls.py

from django.urls import path
from .views import ProfileView 

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    # Add other URL patterns as needed
]

