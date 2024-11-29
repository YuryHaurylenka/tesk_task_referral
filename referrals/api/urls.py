from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from referrals.api.views import AuthViewSet, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
