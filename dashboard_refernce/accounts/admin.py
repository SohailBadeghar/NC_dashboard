from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'emp_id', 'is_active', 'is_staff', 'has_resigned']
    search_fields = ['email', 'emp_id']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'emp_id', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'has_resigned')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
