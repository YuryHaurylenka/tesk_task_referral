from referrals.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository=None):
        self.repository = repository or UserRepository()

    def register_user(self, phone_number):
        return self.repository.get_or_create_user_by_phone(phone_number)

    def activate_invite_code(self, user, invite_code):
        if user.invite_code == invite_code:
            return {"success": False, "error": "You cannot use your own invite code."}

        referred_user = self.repository.get_user_by_invite_code(invite_code)
        if not referred_user:
            return {"success": False, "error": "Invalid invite code."}

        if user.used_invite_code:
            return {"success": False, "error": "Invite code already used."}

        user.used_invite_code = invite_code
        user.save()
        referred_user.referred_users.add(user)
        return {"success": True}
