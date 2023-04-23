from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authapi.models import User


class UserModelAdmin(BaseUserAdmin):
    list_display = ["email", "name", "phone_number", "is_admin", "tc"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "phone_number", "tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "phone_number", "tc", "password1", "password2"],
            },
        ),
    ]
    
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


admin.site.register(User, UserModelAdmin)
