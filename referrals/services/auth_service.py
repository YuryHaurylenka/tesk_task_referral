from random import randint

from referrals.repositories.auth_repository import AuthRepository
from referrals.services.user_service import UserService


class AuthService:
    def __init__(self, auth_repository=None, user_service=None):
        self.auth_repository = auth_repository or AuthRepository()
        self.user_service = user_service or UserService()

    def request_auth_code(self, phone_number):

        code = f"{randint(1000, 9999)}"
        auth_code = self.auth_repository.create_or_update_auth_code(phone_number, code)
        return auth_code

    def verify_auth_code(self, phone_number, code):
        auth_code = self.auth_repository.get_auth_code_by_phone(phone_number)
        if not auth_code or auth_code.code != code or not auth_code.is_valid():
            return {"success": False, "error": "Invalid or expired code."}

        auth_code.delete()

        user = self.user_service.register_user(phone_number)
        return {"success": True, "user": user}
