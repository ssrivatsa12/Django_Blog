from django.urls import path
from django.contrib.auth import views as auth_views
from .views import MySignUpView
from . import views

app_name = 'registration'
urlpatterns = [
    path('sign_up/', MySignUpView.as_view(), name='sign_up'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
]
