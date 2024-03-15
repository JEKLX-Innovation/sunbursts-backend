from django.urls import path
from .views_front import ElementTableView, SurveyView, GraphListView, SurveyResponseView, do_calculations
from .views_front import survey_for_participant

urlpatterns = [
    path("elements/", ElementTableView.as_view(), name="element_table"),
    path('graph/', GraphListView.as_view(), name='graph'),
    path('graph/<int:project_ID>/', GraphListView.as_view(), name='graph_project'),
    path('survey_response/', SurveyResponseView.as_view(), name='survey_response'),
    path('thank_you/', GraphListView.as_view(), name='thank_you'),
    path('survey/<uuid:unique_link>/', survey_for_participant, name='survey_for_participant'),
    path('math_calculations/', do_calculations, name='math'),  
]
