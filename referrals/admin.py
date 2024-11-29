from django.contrib import admin

from referrals.models import AuthCode, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "invite_code", "used_invite_code")
    search_fields = ("phone_number", "invite_code")
    list_filter = ("used_invite_code",)


@admin.register(AuthCode)
class AuthCodeAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "code", "created_at")
    search_fields = ("phone_number",)
    list_filter = ("created_at",)
