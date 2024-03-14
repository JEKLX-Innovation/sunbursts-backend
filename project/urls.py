from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from .views import MyTokenObtainPairView
from django.views.generic.base import TemplateView
from sunbursts.views_front import HomeView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path(
        "api/token/",
        MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "api/token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("sunbursts/", include("sunbursts.urls_front")),
    # If you still want to use HomeView for a specific path, change the path from "" to something else, e.g., "home/"
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # Make admin the first page a user goes to
    path("", admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
]
