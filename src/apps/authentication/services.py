from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


def create_user_account(username, email, password, **extra_fields):
    user = User.objects.create_user(
            username=username, email=email, 
            password=password, **extra_fields)
    return user