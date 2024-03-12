from django.urls import path
from .views import ProjectListView, SurveyCreateView


urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("survey_create/", SurveyCreateView.as_view(), name="survey_create"),
]
