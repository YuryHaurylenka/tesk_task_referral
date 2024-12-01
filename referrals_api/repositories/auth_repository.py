from datetime import timedelta

from django.utils.timezone import now

from referrals_api.models import AuthCode


class AuthRepository:
    @staticmethod
    def get_auth_code_by_phone(phone_number):
        return AuthCode.objects.filter(phone_number=phone_number).first()

    @staticmethod
    def create_or_update_auth_code(phone_number, code):
        auth_code, _ = AuthCode.objects.update_or_create(
            phone_number=phone_number, defaults={"code": code}
        )
        return auth_code

    @staticmethod
    def clean_expired_auth_codes():
        expiration_time = now() - timedelta(minutes=5)
        deleted_count, _ = AuthCode.objects.filter(
            created_at__lt=expiration_time
        ).delete()
        return deleted_count
