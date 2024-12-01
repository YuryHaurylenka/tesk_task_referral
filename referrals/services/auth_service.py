import time
from random import randint

from referrals.repositories.auth_repository import AuthRepository
from referrals.services.user_service import UserService


class AuthService:
    def __init__(self, auth_repository=None, user_service=None):
        self.auth_repository = auth_repository or AuthRepository()
        self.user_service = user_service or UserService()

    def generate_auth_code(self):
        return f"{randint(1000, 9999)}"

    def request_auth_code(self, phone_number):
        time.sleep(randint(1, 2))
        code = self.generate_auth_code()
        return self.auth_repository.create_or_update_auth_code(phone_number, code)

    def verify_auth_code(self, phone_number, code):
        auth_code = self.auth_repository.get_auth_code_by_phone(phone_number)

        if not auth_code:
            return {
                "success": False,
                "error": "Authorization code not found for this phone number.",
            }

        if auth_code.code != code:
            return {"success": False, "error": "Invalid authorization code."}

        if not auth_code.is_valid():
            auth_code.delete()
            self.request_auth_code(phone_number)
            return {
                "success": False,
                "error": "Authorization code has expired. A new code has been sent.",
            }

        auth_code.delete()
        user = self.user_service.register_user(phone_number)
        return {"success": True, "user": user}
