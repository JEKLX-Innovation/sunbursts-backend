from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Project, Element, Survey
from .graph import generate_graph
from django.http import HttpResponse
import base64

class ElementListView(LoginRequiredMixin, ListView):
    template_name = "admin/element_list.html"
    model = Element
    context_object_name = "elements"

class SurveyView(LoginRequiredMixin, CreateView, UpdateView):
    template_name = "admin/survey.html"
    model = Survey
    fields = "__all__"
    context_object_name = "survey"
    # success_url = reverse_lazy("thank_you")
    # lookup_field = 'unique_link'

class HomeView(ListView):
    template_name = "home.html"
    model = Project
    context_object_name = "projects"


class GraphListView(LoginRequiredMixin, ListView):
    template_name = "admin/graph.html"  # Use the admin/graph.html template
    model = Project
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            # Call the function to generate the sunburst plot
            graph_buffer = generate_graph()

            # Encode the graph image to base64
            graph_base64 = base64.b64encode(graph_buffer.getvalue()).decode('utf-8')

            # Pass the plot data to the template context
            context['graph'] = graph_base64
            return context