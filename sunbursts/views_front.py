from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Sunburst


class SunburstListView(LoginRequiredMixin, ListView):
    template_name = "sunbursts/sunburst_list.html"
    model = Sunburst
    context_object_name = "sunbursts"


class SunburstDetailView(LoginRequiredMixin, DetailView):
    template_name = "sunbursts/sunburst_detail.html"
    model = Sunburst


class SunburstUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "sunbursts/sunburst_update.html"
    model = Sunburst
    fields = "__all__"


class SunburstCreateView(LoginRequiredMixin, CreateView):
    template_name = "sunbursts/sunburst_create.html"
    model = Sunburst
    # fields = ["name", "rating", "reviewer"]
    fields = "__all__"

class SunburstDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "sunbursts/sunburst_delete.html"
    model = Sunburst
    success_url = reverse_lazy("sunburst_list")
