from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Project, Element, Survey


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

