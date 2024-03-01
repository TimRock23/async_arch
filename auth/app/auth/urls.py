from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin", admin.site.urls),
    path("oauth/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
]
