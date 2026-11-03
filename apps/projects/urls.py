from django.urls import path
from .views import ProjectListView,ProjectDetailView
app_name='projects' 
urlpatterns = [
    path('', ProjectListView.as_view(),name="index"),
    path('<int:pk>/',ProjectDetailView.as_view(),name="detail"),
]
