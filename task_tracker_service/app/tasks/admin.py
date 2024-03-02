from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "get_link_to_author",
        "get_link_to_assignee",
        "status",
    )
    list_display_links = ("name",)
    search_fields = (
        "id",
        "uuid",
        "author__last_name",
        "assignee__last_name",
        "name",
    )
    autocomplete_fields = ("author", "assignee")
    list_select_related = ("author", "assignee")
    list_filter = ("status",)
    readonly_fields = ("id", "uuid")

    @admin.display(description=_("автор"))
    def get_link_to_author(self, obj: Task) -> str:
        link = reverse("admin:users_user_change", args=[obj.author_id])
        return format_html('<a href="{}">{}</a>', link, obj.author)

    @admin.display(description=_("автор"))
    def get_link_to_assignee(self, obj: Task) -> str:
        if obj.assignee_id:
            link = reverse("admin:users_user_change", args=[obj.assignee_id])
            return format_html('<a href="{}">{}</a>', link, obj.assignee)
        return ""
