from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Project, Element, Survey, SurveyResponse, ElementResponse, Participant
from .graph import generate_graph
from django.http import HttpResponse
import base64
from django.shortcuts import render, get_object_or_404, redirect


class ElementTableView(LoginRequiredMixin, ListView):
    template_name = "participants/element_table.html"
    model = Element
    context_object_name = "elements"

class SurveyView(CreateView, UpdateView):
    # Assuming each project has one survey for simplification
    template_name = "participants/survey.html"
    model = Survey
    fields = "__all__"

    def survey_detail(request, pk):
        survey = get_object_or_404(Survey.objects.prefetch_related('elements'), pk=pk)
        context = {
            'survey': survey,
        }
        return render(request, 'participants/survey.html', context)




class SurveyResponseView(CreateView):
    # template_name = "participants/survey_response.html"
    model = SurveyResponse
    fields = ['element_responses']
    # context_object_name = "survey_response"
    success_url = reverse_lazy("thank_you")

    def post(self, request, *args, **kwargs):
        # Assuming the participant and survey are determined in some way (e.g., session, hidden input)
        # participant_id = request.POST.get('participant_id')
        survey_id = request.POST.get('survey_id')
        print("survey_id, POST:", survey_id)
        survey_response = SurveyResponse.objects.create(survey_id=survey_id)
        print("survey_id, POST:", survey_id)
        print("survey_response, POST:", request.POST)

        # Iterate through the submitted elements
        for key, value in request.POST.items():
            if key.startswith('element_'):
                _, element_id, field_name = key.split('_')
                print("key, value, element_id:", field_name, value, element_id)

                if field_name == 'selected' and value == 'on':
                    value = 1
                elif field_name == 'selected':
                    value = 0
                else:
                    try:
                        value = int(value) if value.strip() != '' else 0
                    except ValueError:
                        value = None
                # Create or update the ElementResponse
                print("key, value, element_id:", field_name, value, element_id)

                ElementResponse.objects.update_or_create(
                    survey_response=survey_response,
                    element_id=element_id,
                    defaults={field_name: value}
                )
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
        # survey_responses = SurveyResponse.objects.filter(survey=survey).prefetch_related('participant')
        # element_responses = ElementResponse.objects.filter(survey_response__in=survey_responses).select_related('element')

        context = {
            'survey': surveyresponse,
            # 'survey_responses': survey_responses,
            # 'element_responses': element_responses,
        }
        return render(request, 'math_calculations.html', context)
