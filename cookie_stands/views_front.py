from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "cookiestands/cookiestand_list.html"
    model = CookieStand
    context_object_name = "cookie_stands"


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookiestands/cookiestand_detail.html"
    model = CookieStand

