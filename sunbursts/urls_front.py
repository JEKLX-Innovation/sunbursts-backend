from django.urls import path
from .views_front import ElementTableView, SurveyView
urlpatterns = [
    path("elements/", ElementTableView.as_view(), name="element_table"),
    path("survey/<int:pk>", SurveyView.as_view(), name="survey"),
    # path("survey/<uuid:unique_link>", survey_form, name="survey_form"),
]
