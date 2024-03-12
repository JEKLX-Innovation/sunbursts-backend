from django.urls import path
from .views_front import ElementListView, SurveyView, GraphListView
urlpatterns = [
    path("elements/", ElementListView.as_view(), name="element_list"),
    path("survey/<int:pk>", SurveyView.as_view(), name="survey"),
    # path("survey/<uuid:unique_link>", survey_form, name="survey_form"),
    path('graph/', GraphListView.as_view(), name='graph'),

]
