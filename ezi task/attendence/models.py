from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    GRADES = [
        ('A+', 'A+'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    profile_picture = models.ImageField(upload_to='profile_images/', null=True, default='profile_images/default_profile_picture.png')
    grades = models.CharField(max_length=3, choices=GRADES, default='D')
    id = models.UUIDField(primary_key = True,auto_created=True , default = uuid.uuid4, editable = False)


class Attendence(models.Model):
    STATUS = [
        ('Absent', 'Absent'),
        ('Present', 'Present'),
        ('Leave Accepted', 'Leave Accepted'),
        ('Leave Applied', 'Leave Applied'),
    ]
    
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=15, choices=STATUS, default='Absent')
    leave_reason = models.TextField(max_length=500, null=True, blank=True)
    id = models.UUIDField(primary_key = True,auto_created=True , default = uuid.uuid4, editable = False)

    def __str__(self):
        return self.user.username


