from datetime import timedelta

from django.db import models
from django.utils.timezone import now


class AuthCode(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return now() < self.created_at + timedelta(minutes=5)

    def delete(self):
        super().delete()

    def __str__(self):
        return f"AuthCode for {self.phone_number}: {self.code}"
