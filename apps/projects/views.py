from django.views.generic import ListView,DetailView
from django.db.models import Q
from .models import Project


class ProjectListView(ListView):
    model = Project
    template_name = "projects/index.html"
    context_object_name = "projects"

    def get_queryset(self):
        queryset = Project.objects.filter(
            is_public=True
        ).select_related(
            "ward"
        ).distinct().order_by("-created_at")

        # Search by project name or ward
        search_query = self.request.GET.get("q", "")

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(ward__name__icontains=search_query)
            )

        # Filter by project status
        status = self.request.GET.get("status", "")

        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_query"] = self.request.GET.get("q", "")
        context["selected_status"] = self.request.GET.get("status", "")

        return context

class ProjectDetailView(DetailView):
    model=Project
    template_name="projects/project_details.html"
    context_object_name="project"

    def get_queryset(self):
        return Project.objects.filter(is_public=True).select_related("ward")