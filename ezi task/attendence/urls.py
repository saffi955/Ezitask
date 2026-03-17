"""ezitask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('clientview/filter/', views.AttendenceFilterView.as_view(), name="filtered_clientview"),
    path('clientview/', views.ClientView.as_view(), name="clientview"),
    path('clientview/<int:pk>', views.ModifyAttendence.as_view(), name="clientview"),
    path('userview/', views.UserView.as_view(), name='userview'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('present/', views.MarkPresent.as_view(), name='present'),
    path('leave/', views.MarkLeave.as_view(), name='leave'),
    path('leave/view/', views.LeaveView.as_view(), name='leave_view'),
    path('signin/', views.Signin.as_view(), name='signin'),
    path('signup/', views.Signup.as_view(), name='signup')
]
