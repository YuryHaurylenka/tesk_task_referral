from referrals.models import User


class UserRepository:
    @staticmethod
    def get_user_by_phone(phone_number):
        return User.objects.filter(phone_number=phone_number).first()

    @staticmethod
    def create_user(phone_number):
        return User.objects.create(phone_number=phone_number)

    @staticmethod
    def get_or_create_user_by_phone(phone_number):
        user, created = User.objects.get_or_create(phone_number=phone_number)
        return user

    @staticmethod
    def get_user_by_invite_code(invite_code):
        return User.objects.filter(invite_code=invite_code).first()
