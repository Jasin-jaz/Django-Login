from rest_framework import serializers
# from django.contrib.auth.models import User
from auth_app.models import User
from rest_framework.authtoken.models import Token

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_customer = True
        user.save()
        Token.objects.create(user=user)
        return user

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_admin = True
        user.save()
        Token.objects.create(user=user)
        return user