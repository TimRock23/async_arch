from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TaskStatuses(TextChoices):
    """Статусы задачи."""
    OPEN = "OPEN", _("Открыта")
    DONE = "DONE", _("Выполнена")
