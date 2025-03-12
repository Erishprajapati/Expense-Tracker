from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#lets start the real show
class Profile(models.Model):
    gender_choices = [
        ("MALE" , 'male'),
        ("FEMALE", 'female'),
        ("OTHER", 'other')
    ]
    role_choices = [
        ("ADMIN", 'admin'),
        ("USER", 'user')
    ]
    
    gender = models.CharField(max_length=10, choices = gender_choices, default = "MALE")
    role = models.CharField(max_length=10, choices = role_choices, default = "USER")

    def __str__(self):
        return self.username
    