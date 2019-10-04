from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserRegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.views.generic import View











"""class MySignUpView(View):
    form_class = UserRegisterForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('accounts:login')
"""


from api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView


class MySignUpView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('accounts:login')


    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token, created = Token.objects.get_or_create(user=request.user)
        print(token)
        return Response({"token": token.key}, status=200)

    """def post(self, request, *args, **kwarg): # <- here i forgot self
                    serializer = self.get_queryset(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    self.perform_create(serializer)
                    headers = self.get_success_headers(serializer.data)
                    token, created = Token.objects.get_or_create(user=serializer.instance)
                    return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)"""




"""class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)"""