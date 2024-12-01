from rest_framework.routers import DefaultRouter
from referrals.api.views import AuthViewSet, UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"auth", AuthViewSet, basename="auth")

urlpatterns = router.urls
