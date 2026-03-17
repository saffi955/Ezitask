from django.contrib import admin
from . import models

@admin.register(models.Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ['date', 'user', 'status', 'leave_reason']

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']