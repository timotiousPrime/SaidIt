from django.urls import path
from .views import (
    LoginView,
    LogoutView,
    AccountsListView,
    AccountCreateView,
    AccountDetailView,
    AccountUpdateView,
    AccountDeleteView,
    RegisterView,
)

app_name = "accounts"

urlpatterns = [
    path("login", LoginView.as_view(), name="Login"),
    path("logout", LogoutView.as_view(), name="Logout"),
    path("register", RegisterView.as_view(), name="Register"),
    path("", AccountsListView.as_view(), name="Accounts"),
    path("new", AccountCreateView.as_view(), name="NewAccount"),
    path("<str:username>/details", AccountDetailView.as_view(), name="AccountDetails"),
    path("<str:username>/update", AccountUpdateView.as_view(), name="AccountUpdate"),
    path("<str:username>/delete", AccountDeleteView.as_view(), name="DeleteAccount"),
]
