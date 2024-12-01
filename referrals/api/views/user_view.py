from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from referrals.services.user_service import UserService
from referrals.api.serializers import (
    ActivateInviteCodeSerializer,
    UserReadSerializer,
)


class UserViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UserService()

    @action(detail=False, methods=["post"], url_path="activate_invite_code")
    def activate_invite_code(self, request):
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
    def get_profile(self, request):

        user = request.user
        referred_users = user.referred_users.values_list("phone_number", flat=True)

        serializer = UserReadSerializer(user)
        data = serializer.data
        data["referred_users"] = list(referred_users)

        return Response({"success": True, "data": data}, status=status.HTTP_200_OK)
