import secrets
import string
from datetime import timedelta

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The phone number must be set")
        extra_fields.setdefault("is_active", True)

        alphabet = string.ascii_letters + string.digits
        invite_code = "".join(secrets.choice(alphabet) for _ in range(6))
        extra_fields["invite_code"] = invite_code

        user = self.model(phone_number=phone_number, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, unique=True)
    used_invite_code = models.CharField(max_length=6, null=True, blank=True)
    referred_users = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="referrers"
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def can_use_invite_code(self, invite_code):
        if self.invite_code == invite_code:
            return False, "You cannot use your own invite code."
        if self.used_invite_code:
            return False, "Invite code already used."
        return True, None

    def __str__(self):
        return self.phone_number


class AuthCode(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return now() < self.created_at + timedelta(minutes=5)

    def __str__(self):
        return f"AuthCode for {self.phone_number}: {self.code}"
