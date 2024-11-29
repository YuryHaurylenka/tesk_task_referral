import secrets
import string
from datetime import timedelta

from django.db import models
from django.utils.timezone import now


class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, unique=True)
    used_invite_code = models.CharField(max_length=6, null=True, blank=True)
    referred_users = models.ManyToManyField(
        'self', symmetrical=False, blank=True, related_name='referrers'
    )

    def save(self, *args, **kwargs):
        if not self.invite_code:
            self.invite_code = self.generate_invite_code()
        super().save(*args, **kwargs)

    @staticmethod
    def generate_invite_code():
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(6))

    def __str__(self):
        return self.phone_number


class AuthCode(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return now() < self.created_at + timedelta(minutes=5)
