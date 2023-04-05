from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_teacher',
        'is_student',
        'address'
    )

    fieldsets = (
        (
            None, {
                'fields': ('username', 'password', 'user_image')
            }
        ),
        (
            'Informações pessoais', {
                'fields': ('first_name', 'last_name', 'email')
            }
        ),
        (
            'Permissões', {
                'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
            }
        ),
        (
            'Log de acessos', {
                'fields': ('last_login', 'date_joined')
            }
        ),
        (
            'Informação adicional', {
                'fields': ('is_student', 'is_teacher', 'address')
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)
