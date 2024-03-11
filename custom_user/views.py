# custom_user/views.py

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserForm  # Assuming you have a form for CustomUser model

class ProfileView(LoginRequiredMixin, View):
    template_name = 'custom_user/profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        form = CustomUserForm(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user = request.user
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Redirect to the profile page or another page upon successful update
            return redirect('profile')

        return render(request, self.template_name, {'form': form})

