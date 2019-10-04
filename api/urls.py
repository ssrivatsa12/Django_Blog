from django.urls import path, include

from . import views
from .views import PostViewSet, MySignUpView
from rest_framework.routers import DefaultRouter

urlpatterns = [
	path('signup/',MySignUpView.as_view(), name='signup'),
	path('', PostViewSet.as_view({'get':'list'}), name='blog'),

]

