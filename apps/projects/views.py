from django.views.generic import ListView
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "projects/index.html"
    context_object_name = "projects"

    def get_queryset(self):
        return Project.objects.filter(
            approvals__decision="APPROVED"
        ).select_related(
            "ward"
        ).prefetch_related(
            "approvals",
            "updates"
        ).distinct().order_by("-created_at")