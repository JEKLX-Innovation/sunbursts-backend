"""
Module containing various views for project management and survey responses.

Attributes:
    None

Classes:
    - ElementTableView: A view to display a table of elements.
    - SurveyView: A view to display and manage surveys.
    - SurveyResponseView: A view to handle survey responses.
    - HomeView: A view for the home page.
    - GraphListView: A view to display graphs.
    - survey_for_participant: A view for survey responses by participants.

Functions:
    None
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .models import Project, Element, Survey, SurveyResponse, ElementResponse, Participant
from .graph import generate_graph, create_df
from django.http import HttpResponse
import base64
from django.shortcuts import render, get_object_or_404, redirect
from .math_calculations import math_calculations


class ElementTableView(LoginRequiredMixin, ListView):
    template_name = "participants/element_table.html"
    model = Element
    context_object_name = "elements"

class SurveyView(CreateView, UpdateView):
    template_name = "participants/survey.html"
    model = Survey
    fields = "__all__"

    def survey_detail(request, pk):
        survey = get_object_or_404(Survey.objects.prefetch_related('elements', 'participants'), pk=pk)
        context = {
            'survey': survey,
        }
        return render(request, 'participants/survey.html', context)


class SurveyResponseView(CreateView):
    model = SurveyResponse
    fields = ['element_responses']
    # context_object_name = "survey_response"
    success_url = reverse_lazy("thank_you")

    def post(self, request, *args, **kwargs):
        participant_id = request.POST.get('participant_id')
        survey_id = request.POST.get('survey_id')
        print("survey_id, participant_id POST:", survey_id, participant_id)
        survey_response = SurveyResponse.objects.create(survey_id=survey_id, participant_id=participant_id)
        print("survey_response, POST:", request.POST)
        # Iterate through the submitted elements
        for key, value in request.POST.items():
            if key.startswith('element_'):
                _, element_id, field_name = key.split('_')
                print("key, value, element_id:", field_name, value, element_id)
                if field_name == 'selected' and value == 'on':
                    ElementResponse.objects.update_or_create(
                    survey_response=survey_response,
                    element_id=element_id,
                    selected=True
                    )

                elif field_name == 'selected':
                    value = False
                else:
                    try:
                        value = int(value)
                        ElementResponse.objects.update_or_create(
                        survey_response=survey_response,
                        element_id=element_id,
                        defaults={field_name: value})
                    # if value.strip() != '' else 0
                    except ValueError:
                        value = None
                print("key, value, element_id:", field_name, value, element_id)

        return redirect(self.success_url)


class HomeView(ListView):
    template_name = "home.html"
    model = Project
    context_object_name = "projects"


class GraphListView(LoginRequiredMixin, ListView):
    template_name = "admin/graph.html"
    model = Project
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            graph_buffer = generate_graph()

            graph_base64 = base64.b64encode(graph_buffer.getvalue()).decode('utf-8')

            context['graph'] = graph_base64

            return context


    def get_data(request, surveyresponse, pk):
        surveyresponse = get_object_or_404(Survey.objects.prefetch_related('elementresponse'), pk=pk)

        context = {
            'survey': surveyresponse,
        }

        return render(request, 'math_calculations.html', context)

def survey_for_participant(request, unique_link):
    participant = get_object_or_404(Participant, unique_link=unique_link)
    project = participant.project
    survey = project.surveys.first()
    
    if not survey:
        pass

    elements = survey.selected_elements.all() if survey else []
    context = {
        'survey': survey,
        'participant': participant,
        'elements': elements,
    }
    return render(request, 'participants/survey.html', context)



class ThankYouView(TemplateView):
    template_name='participants/thank_you.html'


def do_calculations(request):
    math_calculations()
    return HttpResponse("Check log:")