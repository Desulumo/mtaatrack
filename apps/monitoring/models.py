from django.db import models
from django.conf import settings
from apps.projects.models import Project

class ProjectUpdate(models.Model):
    project=models.ForeignKey(Project, on_delete=models.PROTECT,related_name="updates")
    reported_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name="project_updates")
    progress_percentage=models.PositiveSmallIntegerField()
    description=models.TextField()
    challenges=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.progress_percentage}%"


class ActivityLog(models.Model):

    class Action(models.TextChoices):
        VIEW = "VIEW", "View"
        CREATE = "CREATE", "Create"
        UPDATE = "UPDATE", "Update"
        APPROVE = "APPROVE", "Approve"
        ARCHIVE = "ARCHIVE", "Archive"
        CHANGE_ROLE = "CHANGE_ROLE", "Change role"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="activity_logs"
    )

    action = models.CharField(
        max_length=20,
        choices=Action.choices
    )

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action}"