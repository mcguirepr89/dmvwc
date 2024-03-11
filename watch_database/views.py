# watch_database/views.py

from django.shortcuts import render
from watch_collection.models import Watch
from wishlist.models import WishlistItem
from custom_user.models import CustomUser

def index(request):
    return render(request, 'index.html')

def browse_watches(request):
    public_collection_users = CustomUser.objects.filter(watch_collection_visibility='public')
    public_wishlist_users = CustomUser.objects.filter(wishlist_visibility='public')

    public_collection_watches = Watch.objects.filter(user__in=public_collection_users)
    public_wishlist_watches = WishlistItem.objects.filter(user__in=public_wishlist_users)

    logged_in_users_collection_watches = []
    logged_in_users_wishlist_watches = []
    if request.user.is_authenticated:
        logged_in_users_collection_users = CustomUser.objects.filter(watch_collection_visibility='logged_in_users')
        logged_in_users_wishlist_users = CustomUser.objects.filter(wishlist_visibility='logged_in_users')

        logged_in_users_collection_watches = Watch.objects.filter(user__in=logged_in_users_collection_users)
        logged_in_users_wishlist_watches = WishlistItem.objects.filter(user__in=logged_in_users_wishlist_users)
        
    context = {
        'public_collection_watches': public_collection_watches,
        'public_wishlist_watches': public_wishlist_watches,
        'logged_in_users_collection_watches': logged_in_users_collection_watches,
        'logged_in_users_wishlist_watches': logged_in_users_wishlist_watches,
        'model_type': 'anything',
    }

    return render(request, 'browse_watches.html', context)
