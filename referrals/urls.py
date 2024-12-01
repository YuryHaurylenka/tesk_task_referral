from django.urls import path

from referrals.views import (
    logout_view,
    profile_view,
    request_code_view,
    verify_code_view,
)

urlpatterns = [
    path("profile/", profile_view, name="profile"),
    path("request_code/", request_code_view, name="request_code"),
    path("verify_code/", verify_code_view, name="verify_code"),
    path("logout/", logout_view, name="logout"),
]
