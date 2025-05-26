from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    model = User
    list_display = [
        "email",
        "username",
        "date_joined",
    ]

    ordering = ("-date_joined",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "avatar",
                    "bio",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Address"),
            {
                "fields": (
                    "address_1",
                    "address_2",
                    "city",
                    "state",
                    "country",
                    "zipcode",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
