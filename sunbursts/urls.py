from django.urls import path
from .views import ProjectListView, SurveyCreateView, ElementListView


urlpatterns = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("survey_create/", SurveyCreateView.as_view(), name="survey_create"),
    path("element_list/", ElementListView.as_view(), name="element_list"),
]
