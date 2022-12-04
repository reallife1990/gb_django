from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from authapp.forms import CustomUserCreationForm, CustomUserChangeForm
from authapp.models import User

#!!!!
# 2:45 в видео


class CustomLoginView(LoginView):
    template_name = 'authapp/login.html'
    extra_context = {
        'title': 'Вход пользователя'
    }


class RegisterView(CreateView):
    model = User  # get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mainapp:index')


class CustomLogoutView(LogoutView):
    pass


class EditView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'authapp/edit.html'

    # success_url  для edit, update, create обязательный
    def get_success_url(self):
        return reverse_lazy('authapp:edit', args=[self.request.user.pk])

    def get_object(self, queryset=None):  # ограничение на редактирование только своего профиля
        return self.request.user
