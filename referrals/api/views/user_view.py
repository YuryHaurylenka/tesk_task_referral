from drf_spectacular.utils import (
    OpenApiParameter,
    OpenApiResponse,
    extend_schema,
)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from referrals.api.serializers import ActivateInviteCodeSerializer, UserReadSerializer
from referrals.services.user_service import UserService


class UserViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UserService()

    @action(detail=False, methods=["post"], url_path="activate_invite_code")
    @extend_schema(
        summary="Activate Referral Code",
        description="This endpoint allows the user to activate a referral code, associating their account with the referrer.",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="Referral code activated successfully."
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description="Invalid referral code or other error."
            ),
        },
        parameters=[
            OpenApiParameter(
                name="invite_code",
                description="The referral code to be activated.",
                required=True,
                type=str,
            ),
        ],
    )
    def activate_invite_code(self, request):
        """
        Activates a referral code and associates the user's account with the referrer.

        This method expects the `invite_code` in the request body. If the referral code is valid, the user
        will be associated with the referrer. If the referral code is invalid or another error occurs,
        a `400 Bad Request` response is returned.

        **Request Body**:
            - `invite_code` (str): The referral code provided by the user.

        **Responses**:
            - `200 OK`: Referral code activated successfully.
            - `400 Bad Request`: Invalid referral code or another error.
        """
        serializer = ActivateInviteCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        invite_code = serializer.validated_data["invite_code"]
        result = self.service.activate_invite_code(request.user, invite_code)

        if not result["success"]:
            return Response(
                {"success": False, "message": result["error"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({"success": True, "message": "Invite code activated."})

    @action(detail=False, methods=["get"], url_path="profile")
    @extend_schema(
        summary="Get User Profile",
        description="This endpoint returns the profile information of the authenticated user, including their referred users.",
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description="User profile data, including referred users."
            ),
        },
    )
    def get_profile(self, request):
        user = request.user
        referred_users = user.referred_users.values_list("phone_number", flat=True)

        serializer = UserReadSerializer(user)
        data = serializer.data
        data["referred_users"] = list(referred_users)

        return Response({"success": True, "data": data}, status=status.HTTP_200_OK)
