from django.urls import path
from .views import SunburstList, SunburstDetail

urlpatterns = [
    path("", SunburstList.as_view(), name="sunburst_list"),
    path("<int:pk>/", SunburstDetail.as_view(), name="sunburst_detail"),
]
