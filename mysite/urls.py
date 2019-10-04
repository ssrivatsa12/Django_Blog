"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('',include('blog.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/log.html'), name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name="password_reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_don.html'), name="password_reset_done"),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_con.html'), name="password_reset_confirm"),
    path('password_change/', auth_views.PasswordChangeView.as_view( template_name='registration/password_change_for.html'), name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_don.html'), name="password_change_done"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complet.html'), name="password_reset_complete"),
    path('accounts/', include('registration.urls', namespace="accounts")),
]
