# wishlist/views.py

from django.urls import reverse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views import View
from .models import WishlistItem
from custom_user.models import CustomUser
from .forms import WishlistItemForm, WishlistItemDeleteForm
from django.shortcuts import get_object_or_404

class WishlistItemCreateView(LoginRequiredMixin, CreateView):
    model = WishlistItem
    form_class = WishlistItemForm
    template_name = 'wishlist/wishlist_add.html'

    def get_success_url(self):
        return reverse_lazy('wishlist', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WishlistListView(ListView):
    model = WishlistItem
    template_name = 'wishlist/wishlist_list.html'
    context_object_name = 'wishlist_items'

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(CustomUser, username=username)
        current_user = self.request.user

        # Check wishlist_visibility for permission
        if user.wishlist_visibility == 'public':
            self.queryset = WishlistItem.objects.filter(user=user)
        elif user.wishlist_visibility == 'logged_in_users' and current_user.is_authenticated:
            self.queryset = WishlistItem.objects.filter(user=user)
        elif user.wishlist_visibility == 'private' and current_user == user:
            self.queryset = WishlistItem.objects.filter(user=user)
        else:
            # Handle other cases as needed, e.g., set an empty queryset or redirect
            self.queryset = WishlistItem.objects.none()

        return self.queryset

    def get_context_data(self, **kwargs):
        requested_username = self.kwargs['username']
        requested_user = CustomUser.objects.get(username=requested_username)

        # Retrieve the user's editability and visibility values
        context = super().get_context_data(**kwargs)
        context['url_username'] = requested_username
        context['editability'] = requested_user.editability
        context['wishlist_visibility'] = requested_user.wishlist_visibility
        context['can_edit'] = self.request.user == requested_user
        context['model_type'] = 'Wishlist'

        return context

class WishlistDetailView(View):
    template_name = 'wishlist/wishlist_detail.html'

    def get(self, request, pk, *args, **kwargs):
        wishlist_item = get_object_or_404(WishlistItem, pk=pk)
        user = wishlist_item.user

        # Check wishlist_visibility for permission
        if user.wishlist_visibility == 'public':
            can_view = True
        elif user.wishlist_visibility == 'logged_in_users' and request.user.is_authenticated:
            can_view = True
        elif user.wishlist_visibility == 'private' and request.user == user:
            can_view = True
        else:
            can_view = False

        # Check if the user has permissions to edit the wishlist_item
        can_edit = request.user == user

        form = WishlistItemForm(instance=wishlist_item) if can_edit else None

        context = {'wishlist_item': wishlist_item, 'form': form, 'can_view': can_view, 'can_edit': can_edit}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        wishlist_item = get_object_or_404(WishlistItem, pk=pk)
        user = wishlist_item.user

        # Check wishlist_visibility for permission
        if user.wishlist_visibility == 'public':
            can_view = True
        elif user.wishlist_visibility == 'logged_in_users' and request.user.is_authenticated:
            can_view = True
        elif user.wishlist_visibility == 'private' and request.user == user:
            can_view = True
        else:
            can_view = False

        # Check if the user has permissions to edit the wishlist_item
        can_edit = request.user == user

        form = WishlistItemForm(request.POST, request.FILES, instance=wishlist_item) if can_edit else None

        if form and form.is_valid():
            form.save()
            # Redirect to the wishlist_item detail page or another page upon successful update
            return redirect('wishlist-detail', pk=pk, username=request.user.username)

        context = {'wishlist_item': wishlist_item, 'form': form, 'can_view': can_view, 'can_edit': can_edit}
        return render(request, self.template_name, context)

class WishlistItemDeleteMultipleView(LoginRequiredMixin, FormView):
    template_name = 'wishlist/wishlist_list.html'
    form_class = WishlistItemDeleteForm

    def get_success_url(self):
        return reverse('wishlist', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        items_to_delete = form.cleaned_data['items_to_delete']
        WishlistItem.objects.filter(id__in=items_to_delete).delete()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
