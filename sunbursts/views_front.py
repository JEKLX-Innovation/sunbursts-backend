from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .models import Project, Element, Survey, SurveyResponse, ElementResponse, Participant
from .graph import generate_graph
from django.http import HttpResponse
import base64
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelformset_factory


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


class SurveyResponseView(CreateView):
    model = SurveyResponse
    fields = []  # Remove fields attribute since we're using formsets
    success_url = reverse_lazy("thank_you")

    def post(self, request, *args, **kwargs):
        # Print the request method
        print("Request method:", request.method)

        # Assuming the participant and survey are determined in some way (e.g., session, hidden input)
        survey_id = request.POST.get('survey_id')
        print("Survey ID:", survey_id)

        # Create a survey response object
        survey_response = SurveyResponse.objects.create(survey_id=survey_id)

        # Create a formset for ElementResponse
        ElementResponseFormSet = modelformset_factory(ElementResponse, fields=('element', 'readiness', 'weighting', 'trendnow', 'trendneeded'), extra=0)
        formset = ElementResponseFormSet(request.POST)
        
        if formset.is_valid():
            # Save each form in the formset
            for form in formset:
                element_response = form.save(commit=False)
                element_response.survey_response = survey_response
                element_response.save()

            return redirect(self.get_success_url())
        else:
            # Handle invalid formset
            print("Formset errors:", formset.errors)
            return HttpResponse("Formset is invalid")

class HomeView(ListView):
    template_name = "home.html"
    model = Project
    context_object_name = "projects"


class GraphListView(LoginRequiredMixin, ListView):
    template_name = "admin/graph.html"
    model = Project
    context_object_name = "projects"

    # def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         graph_buffer = generate_graph()

    #         graph_base64 = base64.b64encode(graph_buffer.getvalue()).decode('utf-8')

    #         context['graph'] = graph_base64
    #         return context

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            for project in context['projects']:
                graph_buffer = generate_graph(project)  # You need to implement generate_graph function
                graph_base64 = base64.b64encode(graph_buffer.getvalue()).decode('utf-8')
                project.graph = graph_base64
            return context


class ThankYouView(TemplateView):
    template_name='participants/thank_you.html'