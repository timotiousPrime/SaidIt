from django.shortcuts import render

# Generic Views
from django.views.generic import (
    View,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

# Models
from django.contrib.auth.models import User
from .models import User_Profile

# Create your views here.


class LoginView(View):
    template_name = "/.html"


class LogoutView(View):
    template_name = "/.html"


class RegisterView(View):
    template_name = "/.html"


class AccountsListView(ListView):
    template_name = "accounts/AccountsListPage.html"
    queryset = User_Profile.objects.all()


class AccountCreateView(CreateView):
    template_name = "accounts/AccountCreatePage.html"
    model = User


class AccountDetailView(DetailView):
    template_name = "accounts/AccountDetailPage.html"
    model = User_Profile


class AccountUpdateView(UpdateView):
    template_name = "accounts/AccountUpdatePage.html"
    model = User_Profile


class AccountDeleteView(DeleteView):
    template_name = "accounts/AccountDeletePage.html"
    model = User
