from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from referrals.api.serializers import (
    RequestCodeSerializer,
    UserReadSerializer,
    VerifyCodeSerializer,
)
from referrals.services.auth_service import AuthService


class AuthViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AuthService()

    @action(detail=False, methods=["post"], url_path="request_code")
    def request_code(self, request):
        serializer = RequestCodeSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            phone_number = serializer.validated_data["phone_number"]

            self.service.request_auth_code(phone_number)
            return Response(
                {"message": "Auth code sent successfully."}, status=status.HTTP_200_OK
            )

        except ValidationError as e:
            error_message = list(e.detail.values())[0][0]  # First error message
            return Response(
                {"message": error_message}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"message": "Failed to send auth code. Please try again later."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(detail=False, methods=["post"], url_path="verify_code")
    def verify_code(self, request):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data["phone_number"]
        code = serializer.validated_data["code"]

        try:
            result = self.service.verify_auth_code(phone_number, code)
            if not result["success"]:
                return Response(
                    {"error": result["error"]}, status=status.HTTP_400_BAD_REQUEST
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
        except Exception as e:
            return Response(
                {"error": "Verification failed.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
