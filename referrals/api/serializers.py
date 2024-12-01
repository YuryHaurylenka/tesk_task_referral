from rest_framework import serializers

from referrals.models import User


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number", "invite_code", "used_invite_code"]


class ActivateInviteCodeSerializer(serializers.Serializer):
    invite_code = serializers.CharField(min_length=6, max_length=6, required=True)


class RequestCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=12,
        min_length=7,
        required=True,
        error_messages={
            "required": "Phone number is required.",
            "min_length": "Phone number must have at least 7 digits.",
            "max_length": "Phone number must have at most 12 digits.",
        },
    )

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        return value


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=15,
        required=True,
        error_messages={"required": "Phone number is required."},
    )
    code = serializers.CharField(
        max_length=4, required=True, error_messages={"required": "Code is required."}
    )
