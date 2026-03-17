from rest_framework import serializers
from . import models

class UserSerielizer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserProfileSerielizer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ['first_name','last_name','email','profile_picture', 'grades', 'pk']

class AttendenceSerielizer(serializers.ModelSerializer):
    class Meta:
        model = models.Attendence
        fields = ["date", "user", "status", "leave_reason", "id"]

        
