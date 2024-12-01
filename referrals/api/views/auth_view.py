from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

from referrals.api.serializers import (
    RequestCodeSerializer,
    UserReadSerializer,
    VerifyCodeSerializer,
)
from referrals.services.auth_service import AuthService
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse


class AuthViewSet(ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = AuthService()

    @extend_schema(
        summary="Request Authorization Code",
        description="This endpoint allows the user to request an authorization code via phone number.",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="Auth code sent successfully."
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Invalid phone number."
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                description="Failed to send auth code."
            ),
        },
        parameters=[
            OpenApiParameter(
                name="phone_number",
                description="The phone number to send the code to.",
                required=True,
                type=str,
            )
        ],
    )
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
            error_message = list(e.detail.values())[0][0]
            return Response(
                {"message": error_message}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"message": "Failed to send auth code. Please try again later."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @extend_schema(
        summary="Verify Authorization Code",
        description="This endpoint verifies the authorization code provided by the user.",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="Code verified successfully."
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(description="Invalid code."),
            status.HTTP_500_INTERNAL_SERVER_ERROR: OpenApiResponse(
                description="Verification failed."
            ),
        },
        parameters=[
            OpenApiParameter(
                name="phone_number",
                description="The phone number for verification.",
                required=True,
                type=str,
            ),
            OpenApiParameter(
                name="code",
                description="The authorization code entered by the user.",
                required=True,
                type=str,
            ),
        ],
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
