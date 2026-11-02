from django.contrib import admin
from .models import Ward


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "code")