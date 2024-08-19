from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("is_patient", "is_doctor", "is_technician")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
