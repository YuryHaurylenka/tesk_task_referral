from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from referral_test_task.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls) if settings.DEBUG else None,
    path("api/", include("referrals.api.urls")),
    path("", home_view, name="home"),
    path("", include("referrals.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

handler404 = "referral_test_task.views.custom_404"
