from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from referrals.services.user_service import UserService


class UserViewSet(ViewSet):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UserService()

    @action(detail=False, methods=["post"], url_path="activate-invite-code")
    def activate_invite_code(self, request):
        phone_number = request.data.get("phone_number")
        invite_code = request.data.get("invite_code")

        user = self.service.register_user(phone_number)
        result = self.service.activate_invite_code(user, invite_code)

        if not result["success"]:
            return Response(
                {"success": False, "message": result["error"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({"success": True})

    @action(detail=False, methods=["get"], url_path="profile")
    def get_profile(self, request):

        user = request.user

        referred_users = user.referred_users.values_list("phone_number", flat=True)

        return Response(
            {
                "phone_number": user.phone_number,
                "invite_code": user.invite_code,
                "used_invite_code": user.used_invite_code,
                "referred_users": list(referred_users),
            },
            status=status.HTTP_200_OK,
        )
