from django.contrib import admin

from referrals.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'invite_code', 'used_invite_code')
