from rest_framework import viewsets
from django.contrib.auth.models import User
from blog import models
from . import serializers
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.order_by('-pk')
    serializer_class = serializers.PostSerializer

class MySignUpView(APIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer