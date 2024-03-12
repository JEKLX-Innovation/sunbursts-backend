from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Project


class SunburstListView(LoginRequiredMixin, ListView):
    template_name = "sunbursts/sunburst_list.html"
    model = Project
    context_object_name = "sunbursts"


class SunburstDetailView(LoginRequiredMixin, DetailView):
    template_name = "sunbursts/sunburst_detail.html"
    model = Project

