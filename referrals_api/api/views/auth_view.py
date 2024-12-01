from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from referrals_api.api.serializers import (
    UserReadSerializer,
    RequestCodeSerializer,
    VerifyCodeSerializer,
)
from referrals_api.services.auth_service import AuthService


class AuthViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AuthService()

    @action(detail=False, methods=["post"], url_path="request-code")
    def request_code(self, request):
        serializer = RequestCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data["phone_number"]

        self.service.request_auth_code(phone_number)
        return Response({"message": "Auth code sent."}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"], url_path="verify-code")
    def verify_code(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data["phone_number"]
        code = serializer.validated_data["code"]

        result = self.service.verify_auth_code(phone_number, code)
        if not result["success"]:
            return Response(
                {"error": result["error"]},
                status=status.HTTP_400_BAD_REQUEST,
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
                "access_token": access,
            },
            status=status.HTTP_200_OK,
        )
