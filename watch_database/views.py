# watch_database/views.py

from itertools import chain
from django.shortcuts import render
from watch_collection.models import Watch
from custom_user.models import CustomUser

def index(request):
    return render(request, 'index.html')

def browse_watches(request):
    public_collection_users = CustomUser.objects.filter(watch_collection_visibility='public')
    public_wishlist_users = CustomUser.objects.filter(wishlist_visibility='public')
    public_collection_watches = Watch.objects.filter(user__in=public_collection_users,on_wishlist=True)
    public_wishlist_watches = Watch.objects.filter(user__in=public_wishlist_users,on_wishlist=False)

    public_watches = list(chain(public_wishlist_watches, public_collection_watches))
    public_watches_sorted = sorted(public_watches, key=lambda x: x.created_at, reverse=True)

    logged_in_users_watches_sorted = []
    if request.user.is_authenticated:
        logged_in_users_collection_users = CustomUser.objects.filter(watch_collection_visibility='logged_in_users')
        logged_in_users_wishlist_users = CustomUser.objects.filter(wishlist_visibility='logged_in_users')
        logged_in_users_collection_watches = Watch.objects.filter(user__in=logged_in_users_collection_users,on_wishlist=True)
        logged_in_users_wishlist_watches = Watch.objects.filter(user__in=logged_in_users_wishlist_users,on_wishlist=False)

        logged_in_users_watches = list(chain(logged_in_users_wishlist_watches, logged_in_users_collection_watches))
        logged_in_users_watches_sorted = sorted(logged_in_users_watches, key=lambda x: x.created_at, reverse=True)

        
    context = {
        'public_watches': public_watches_sorted,
        'logged_in_users_watches': logged_in_users_watches_sorted,
    }

    return render(request, 'browse_watches.html', context)
