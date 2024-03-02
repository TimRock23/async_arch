import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from tasks.types import TaskStatuses
from users.models import User

class Task(models.Model):
    """Задача."""

    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("уникальный идентификатор")
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_tasks",
        verbose_name=_("автор"),
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="assigned_tasks",
        null=True,
        blank=True,
        default=None,
        verbose_name=_("исполнитель"),
    )
    name = models.CharField(max_length=512, verbose_name=_("наименование"))
    description = models.TextField(verbose_name=_("описание"), null=True, blank=True)
    status = models.CharField(
        max_length=64,
        choices=TaskStatuses.choices,
        verbose_name=_("статус"),
        default=TaskStatuses.OPEN,
    )
    
    class Meta:
        verbose_name = _("задача")
        verbose_name_plural = _("задачи")

    def __str__(self) -> str:
        """Строковое представление объекта класса Task."""
        return f"Задача №{self.id}: {self.name}"
