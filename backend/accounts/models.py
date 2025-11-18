from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        USER = "user", "Користувач"
        VET = "vet", "Ветеринар"
        ADMIN = "admin", "Адміністратор"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.USER,
        verbose_name="Роль",
    )

    def __str__(self):
        return f"{self.username} ({self.role})"