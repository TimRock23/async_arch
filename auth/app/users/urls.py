from django.urls import path

from users import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignUp.as_view(), name="signup")
]
