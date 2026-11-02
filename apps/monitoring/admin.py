
from django.contrib import admin
from .models import ProjectUpdate, ActivityLog


@admin.register(ProjectUpdate)
class ProjectUpdateAdmin(admin.ModelAdmin):
    list_display = (
        "project", "reported_by",
        "progress_percentage", "created_at"
    )
    list_filter = ("created_at",)
    search_fields = ("project__name", "description")
    readonly_fields = ("created_at",)


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = (
        "user", "action", "description", "created_at"
    )
    list_filter = ("action", "created_at")
    search_fields = ("user__username", "description")
    readonly_fields = (
        "user", "action", "description", "created_at"
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
