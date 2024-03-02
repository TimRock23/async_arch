from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class UserRole(TextChoices):
    ADMIN = "ADMIN", _("Администратор")
    CHIEF = "CHIEF", _("Начальник")
    MANAGER = "MANAGER", _("Менеджер")
    DEVELOPER = "DEVELOPER", _("Разработчик")
