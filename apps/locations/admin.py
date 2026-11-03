from django.contrib import admin
from .models import Ward


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "district", "is_active")