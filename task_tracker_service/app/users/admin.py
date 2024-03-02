from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uuid",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_display_links = ("uuid", "username")
    search_fields = (
        "id",
        "uuid",
        "first_name",
        "last_name",
        "username",
        "email",
    )
    readonly_fields = ("id", "uuid")
