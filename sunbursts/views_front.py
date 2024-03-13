from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Project, Element, Survey, SurveyResponse, ElementResponse, Participant
from .graph import generate_graph
from django.http import HttpResponse
import base64
from django.shortcuts import render, get_object_or_404


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
        # survey_responses = SurveyResponse.objects.filter(survey=survey).prefetch_related('participant')
        # element_responses = ElementResponse.objects.filter(survey_response__in=survey_responses).select_related('element')

        context = {
            'survey': survey,
            # 'survey_responses': survey_responses,
            # 'element_responses': element_responses,
        }
        return render(request, 'participants/survey.html', context)
    # def survey_view(request, survey_id):
    #     survey = get_object_or_404(Survey.objects.prefetch_related('elements'), id=survey_id)
    #     return render(request, 'admin/survey.html', {'survey': survey})

    context_object_name = "survey"


    # success_url = reverse_lazy("thank_you")
    # lookup_field = 'unique_link'

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
