from . import views
from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    AccountsListView,
    # AccountCreateView,
    AccountDetailView,
    AccountUpdateView,
    AccountDeleteView,
    RegisterView,
)

app_name = "account"

urlpatterns = [
    path("login", LoginView.as_view(), name="Login"),
    path("logout", LogoutView.as_view(), name="Logout"),
    path("register", RegisterView.as_view(), name="Register"),
    path("", AccountsListView.as_view(), name="Accounts"),
    # path("new", AccountCreateView.as_view(), name="NewAccount"),
    path("new1", views.accountCreateView, name="newAccount1"),
    path("<str:pk>/details", AccountDetailView.as_view(), name="AccountDetails"),
    path("<str:pk>/update", AccountUpdateView.as_view(), name="AccountUpdate"),
    path("<str:pk>/delete", AccountDeleteView.as_view(), name="DeleteAccount"),
]
