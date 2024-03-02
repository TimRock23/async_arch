from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin", admin.site.urls),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("users/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
]

urlpatterns += staticfiles_urlpatterns()
