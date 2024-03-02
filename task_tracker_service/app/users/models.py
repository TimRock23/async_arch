import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.types import UserRole


class User(AbstractUser):
    """Учетная запись пользователя."""

    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name=_("уникальный идентификатор")
    )
    role = models.CharField(
        choices=UserRole.choices,
        max_length=64,
        verbose_name=_("роль")
    )

    class Meta:
        verbose_name = _("пользователь")
        verbose_name_plural = _("пользователи")

    def __str__(self) -> str:
        """Строковое представление объекта класса User."""
        return f"{self.last_name} {self.first_name}" if self.last_name else self.username
