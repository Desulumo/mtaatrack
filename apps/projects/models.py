from django.conf import settings
from django.db import models
from apps.locations.models import Ward
# Create your models here.

class Project(models.Model):
    class Status(models.TextChoices):
        PLANNING="PLANNING", "Planning"
        ONGOING="ONGOING","Ongoing"
        SUSPENDED="SUSPENDED", "Suspended"
        COMPLETED="COMPLETED", "Completed"

    name=models.CharField(max_length=200)
    description=models.TextField()
    budget = models.DecimalField(max_digits=15, decimal_places=2)
    ward=models.ForeignKey(Ward,on_delete=models.PROTECT, related_name="projects")
    start_date=models.DateField()
    expected_end_date=models.DateField()
    status=models.CharField(max_length=20, choices=Status.choices, default=Status.PLANNING)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name="created_projects")
    def __str__(self):
        return self.name

class ProjectApproval(models.Model):

    class Decision(models.TextChoices):
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    project = models.ForeignKey(
        Project,
        on_delete=models.PROTECT,
        related_name="approvals"
    )

    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="project_reviews"
    )

    decision = models.CharField(
        max_length=20,
        choices=Decision.choices
    )

    remarks = models.TextField()

    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.project.name} - {self.decision}"