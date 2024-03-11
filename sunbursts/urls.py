from django.urls import path
from .views import SunburstListView, SunburstDetailView

urlpatterns = [
    path("", SunburstListView.as_view(), name="sunburst_list"),
    path("<int:pk>/", SunburstDetailView.as_view(), name="sunburst_detail"),
]
