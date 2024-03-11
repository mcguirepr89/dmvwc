# wishlist/urls.py

from django.urls import path
from .views import WishlistListView, WishlistItemCreateView, WishlistDetailView, WishlistItemDeleteMultipleView

urlpatterns = [
    path('', WishlistListView.as_view(), name='wishlist'),  # Updated path
    path('add/', WishlistItemCreateView.as_view(), name='wishlist-add'),  # Updated path
    path('watch/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('delete-multiple/', WishlistItemDeleteMultipleView.as_view(), name='wishlist-delete-multiple'),  # Updated path
    # Add more URLs as needed
]

