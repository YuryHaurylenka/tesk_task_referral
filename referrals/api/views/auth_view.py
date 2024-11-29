import random
import time

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from referrals.api.serializers import UserReadSerializer
from referrals.models import AuthCode
from referrals.services.user_service import UserService


class AuthViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UserService()

    @action(detail=False, methods=["post"], url_path="request-code")
    def request_code(self, request):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            return Response(
                {"error": "Phone number is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        code = f"{random.randint(1000, 9999)}"

        AuthCode.objects.update_or_create(
            phone_number=phone_number, defaults={"code": code}
        )

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

        try:
            auth_code = AuthCode.objects.get(phone_number=phone_number)
            if auth_code.code != code:
                return Response(
                    {"error": "Invalid code."}, status=status.HTTP_400_BAD_REQUEST
                )
        except AuthCode.DoesNotExist:
            return Response(
                {"error": "Auth code not found."}, status=status.HTTP_400_BAD_REQUEST
            )

        auth_code.delete()

        user = self.service.register_user(phone_number)
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
