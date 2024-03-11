from django.urls import path
from .views_front import (
    SunburstDetailView,
    SunburstListView,
)

urlpatterns = [
    path("", SunburstListView.as_view(), name="sunburst_list"),
    path("<int:pk>/", SunburstDetailView.as_view(), name="sunburst_detail"),
    # path("create/", SunburstCreateView.as_view(), name="sunburst_create"),
    # path("<int:pk>/update/", SunburstUpdateView.as_view(), name="sunburst_update"),
    # path("<int:pk>/delete/", SunburstDeleteView.as_view(), name="sunburst_delete"),
]
