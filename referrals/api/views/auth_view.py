import random
import time

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from referrals.api.serializers import UserReadSerializer
from referrals.models import AuthCode
from referrals.services.auth_service import AuthService


class AuthViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AuthService()

    @action(detail=False, methods=["post"], url_path="request-code")
    def request_code(self, request):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            return Response(
                {"error": "Phone number is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.service.request_auth_code(phone_number)

        time.sleep(random.uniform(1, 2))

        return Response({"message": "Auth code sent."})

    @action(detail=False, methods=["post"], url_path="verify-code")
    def verify_code(self, request):
        phone_number = request.data.get("phone_number")
        code = request.data.get("code")

        if not phone_number or not code:
            return Response(
                {"error": "Phone number and code are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        result = self.service.verify_auth_code(phone_number, code)
        if not result["success"]:
            return Response(
                {"error": result["message"]}, status=status.HTTP_400_BAD_REQUEST
            )

        user = result["user"]

        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        request.session["access_token"] = access

        user_data = UserReadSerializer(user).data
        return Response(
            {
                "message": "Authentication successful.",
                "user": user_data,
            },
            status=status.HTTP_200_OK,
        )
