from django.contrib import admin
from .models import Project, ProjectApproval


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "ward",
        "budget",
        "status",
        "created_at",
    )

    list_filter = ("status", "ward")
    search_fields = ("name", "description")
    readonly_fields = ("created_at", "updated_at")


@admin.register(ProjectApproval)
class ProjectApprovalAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "reviewed_by",
        "decision",
        "reviewed_at",
    )

    list_filter = ("decision",)
    search_fields = ("project__name", "remarks")
    readonly_fields = ("reviewed_at",)