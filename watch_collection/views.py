# watch_collection/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, FormView
from .forms import WatchForm, WatchDeleteForm
from .models import Watch
from django.http import HttpResponseRedirect
from django.views import View
from custom_user.models import CustomUser
from django.shortcuts import get_object_or_404

class WatchListView(ListView):
    model = Watch
    template_name = 'watch_collection/watch_list.html'
    context_object_name = 'watches'
    paginate_by = 10

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(CustomUser, username=username)

        # Check watch_collection_visibility for permission
        if user.watch_collection_visibility == 'public':
            self.queryset = Watch.objects.filter(user=user)
        elif user.watch_collection_visibility == 'logged_in_users' and self.request.user.is_authenticated:
            self.queryset = Watch.objects.filter(user=user)
        elif user.watch_collection_visibility == 'private' and self.request.user == user:
            self.queryset = Watch.objects.filter(user=user)
        else:
            # Handle other cases as needed, e.g., set an empty queryset or redirect to a permission-denied page
            self.queryset = Watch.objects.none()

        return self.queryset

    def get_context_data(self, **kwargs):
        requested_username = self.kwargs['username']
        requested_user = CustomUser.objects.get(username=requested_username)

        # Retrieve the user's editability and visibility values
        context = super().get_context_data(**kwargs)
        context['url_username'] = requested_username
        context['editability'] = requested_user.editability
        context['watch_collection_visibility'] = requested_user.watch_collection_visibility
        context['can_edit'] = self.request.user == requested_user

        return context

class WatchCreateView(LoginRequiredMixin, CreateView):
    model = Watch
    form_class = WatchForm
    template_name = 'watch_collection/watch_add.html'

    def get_success_url(self):
        return reverse_lazy('watch-collection', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class WatchDetailView(View):
    template_name = 'watch_collection/watch_detail.html'

    def get(self, request, pk, *args, **kwargs):
        watch = get_object_or_404(Watch, pk=pk)
        user = watch.user

        # Check watch_collection_visibility for permission
        if user.watch_collection_visibility == 'public':
            can_view = True
        elif user.watch_collection_visibility == 'logged_in_users' and request.user.is_authenticated:
            can_view = True
        elif user.watch_collection_visibility == 'private' and request.user == user:
            can_view = True
        else:
            can_view = False

        # Check if the user has permissions to edit the watch
        can_edit = request.user == user

        form = WatchForm(instance=watch) if can_edit else None

        context = {'watch': watch, 'form': form, 'can_view': can_view, 'can_edit': can_edit}
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        watch = get_object_or_404(Watch, pk=pk)
        user = watch.user

        # Check watch_collection_visibility for permission
        if user.watch_collection_visibility == 'public':
            can_view = True
        elif user.watch_collection_visibility == 'logged_in_users' and request.user.is_authenticated:
            can_view = True
        elif user.watch_collection_visibility == 'private' and request.user == user:
            can_view = True
        else:
            can_view = False

        # Check if the user has permissions to edit the watch
        can_edit = request.user == user

        form = WatchForm(request.POST, request.FILES, instance=watch) if can_edit else None

        if form and form.is_valid():
            form.save()
            # Redirect to the watch detail page or another page upon successful update
            return redirect('watch-detail', pk=pk, username=request.user.username)

        context = {'watch': watch, 'form': form, 'can_view': can_view, 'can_edit': can_edit}
        return render(request, self.template_name, context)

class WatchDeleteView(LoginRequiredMixin, DeleteView):
    model = Watch
    template_name = 'watch_collection/watch_delete.html'
    form_class = WatchDeleteForm
    success_url = reverse_lazy('watch-collection')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Watch.objects.filter(user=self.request.user)

class WatchDeleteMultipleView(LoginRequiredMixin, FormView):
    template_name = 'watch_collection/watch_delete_multiple.html'
    form_class = WatchDeleteForm

    def get_success_url(self):
        return reverse('watch-collection', kwargs={'username': self.request.user.username})

    def form_valid(self, form):
        watches_to_delete = form.cleaned_data['watches_to_delete']
        Watch.objects.filter(id__in=watches_to_delete).delete()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ToggleEditabilityView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = CustomUser.objects.get(username=request.user.username)
        # Save the referring URL before toggling editability
        referring_url = request.META.get('HTTP_REFERER', reverse('watch-collection', kwargs={'username': request.user.username}))
        user.editability = not user.editability
        user.save()
        return HttpResponseRedirect(referring_url)
