from referrals.models import AuthCode


class AuthRepository:
    @staticmethod
    def get_auth_code_by_phone(phone_number):
        return AuthCode.objects.filter(phone_number=phone_number).first()

    @staticmethod
    def create_or_update_auth_code(phone_number, code):
        return AuthCode.objects.update_or_create(
            phone_number=phone_number, defaults={"code": code}
        )
