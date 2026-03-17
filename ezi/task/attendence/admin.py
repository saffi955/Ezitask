# admin.py

from django.contrib import admin
from .models import *

# Register your models here.


# apps.py

from django.apps import AppConfig


class AttendenceConfig(AppConfig):
    name = 'attendence'


# models.py

from django.db import models


# Create your models here.


# serializers.py

from rest_framework import serializers
from .models import *


# Create your serializers here.


# tests.py

from django.test import TestCase


# Create your tests here.


# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Add your url patterns here
]


# views.py

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
