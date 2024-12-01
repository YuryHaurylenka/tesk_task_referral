from django.contrib import admin

from referrals_api.models import AuthCode, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "invite_code", "used_invite_code")
    search_fields = ("phone_number", "invite_code")
    list_filter = ("used_invite_code",)


@admin.register(AuthCode)
class AuthCodeAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "code", "created_at", "is_valid_display")
    search_fields = ("phone_number",)
    list_filter = ("created_at",)

    def is_valid_display(self, obj):
        return obj.is_valid()

    is_valid_display.boolean = True
    is_valid_display.short_description = "Is Valid"
