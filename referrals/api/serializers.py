from rest_framework import serializers

from referrals.models import User


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number", "invite_code", "used_invite_code"]
