from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        SYSTEM_ADMIN = "SYSTEM_ADMIN","System administrator"
        MANAGER="MANAGER", "Manager"
        OFFICER="OFFICER", "Project Officer"

    role=models.CharField(max_length=50, choices=Role.choices, default=Role.OFFICER)
