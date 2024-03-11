from django.urls import path
from .views_front import (
    CookieStandCreateView,
    CookieStandDeleteView,
    CookieStandDetailView,
    CookieStandListView,
    CookieStandUpdateView,
)

urlpatterns = [
    path("", CookieStandListView.as_view(), name="cookiestand_list"),
    path("<int:pk>/", CookieStandDetailView.as_view(), name="cookiestand_detail"),
    path("create/", CookieStandCreateView.as_view(), name="cookiestand_create"),
    path("<int:pk>/update/", CookieStandUpdateView.as_view(), name="cookiestand_update"),
    path("<int:pk>/delete/", CookieStandDeleteView.as_view(), name="cookiestand_delete"),
]
