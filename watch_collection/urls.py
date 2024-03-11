# watch_collection/urls.py

from django.urls import path
from .views import WatchListView, WatchCreateView, WatchDetailView, WatchDeleteView, WatchDeleteMultipleView, ToggleEditabilityView

urlpatterns = [
    path('', WatchListView.as_view(), name='watch-collection'),  # Updated path
    path('add/', WatchCreateView.as_view(), name='watch-add'),  # Updated path
    path('watch/<int:pk>/', WatchDetailView.as_view(), name='watch-detail'),
    path('delete/<int:pk>/', WatchDeleteView.as_view(), name='watch-delete'),  # Updated path
    path('delete-multiple/', WatchDeleteMultipleView.as_view(), name='watch-delete-multiple'),  # Updated path
    path('toggle-editability/', ToggleEditabilityView.as_view(), name='toggle-editability'),  # Updated path
    # Add more URLs as needed
]

