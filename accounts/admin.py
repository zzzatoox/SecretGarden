from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ("username", "email", "phone", "first_name", "last_name", "is_staff")

    search_fields = ("username", "email", "phone", "first_name", "last_name")

    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Персональная информация",
            {"fields": ("first_name", "last_name", "email", "phone")},
        ),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Важные даты", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "phone",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )

    def get_field_verbose_name(self, field_name):
        verbose_names = {
            "username": "Имя пользователя",
            "email": "Email",
            "phone": "Телефон",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "is_staff": "Персонал",
            "is_active": "Активен",
            "is_superuser": "Суперпользователь",
            "groups": "Группы",
            "user_permissions": "Разрешения пользователя",
            "last_login": "Последний вход",
            "date_joined": "Дата регистрации",
            "password": "Пароль",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",
        }
        return verbose_names.get(field_name, field_name)

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        field = super().formfield_for_dbfield(db_field, request, **kwargs)
        field.label = self.get_field_verbose_name(db_field.name)
        return field


admin.site.register(User, UserAdmin)
