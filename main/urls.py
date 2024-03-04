from django.urls import path
from .views import (
    LandingPageView,
)

app_name = "accounts"

urlpatterns = [
    path("", LandingPageView.as_view(), name="LandingPage"),
]
