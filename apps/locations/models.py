from django.db import models


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Ward(models.Model):
    district = models.ForeignKey(
        District,
        on_delete=models.PROTECT,
        related_name="wards",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.district}"