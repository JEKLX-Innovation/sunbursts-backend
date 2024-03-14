from django.urls import path
from .views_front import ElementTableView, SurveyView, GraphListView, SurveyResponseView

urlpatterns = [
    path("elements/", ElementTableView.as_view(), name="element_table"),
    path("survey/<int:pk>/", SurveyView.as_view(), name="survey"),
    # path("survey/<uuid:unique_link>", survey_form, name="survey_form"),
    path('graph/', GraphListView.as_view(), name='graph'),
    path('graph/<int:project_ID>/', GraphListView.as_view(), name='graph_project'),
    path('survey_response/', SurveyResponseView.as_view(), name='survey_response'),
    path('thank_you/', GraphListView.as_view(), name='thank_you'),
]
