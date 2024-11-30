from rest_framework import serializers

from referrals.models import User


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number", "invite_code", "used_invite_code"]


class ActivateInviteCodeSerializer(serializers.Serializer):
    invite_code = serializers.CharField(max_length=6, required=True)


class RequestCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=15,
        required=True,
        error_messages={"required": "Phone number is required."},
    )


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=15,
        required=True,
        error_messages={"required": "Phone number is required."},
    )
    code = serializers.CharField(
        max_length=4, required=True, error_messages={"required": "Code is required."}
    )
