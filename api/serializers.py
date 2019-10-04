from rest_framework import serializers
from blog import models
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework import exceptions
from django.contrib.auth.models import User



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        	'__all__'
        )
        model = models.Post
        read_only_fields=('pk','author',)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email',)
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user