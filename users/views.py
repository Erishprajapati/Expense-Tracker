from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

"""all the imports are pasted from internet"""
# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    """queryset is the method to get the models in which will return the data"""
    serializer_class = ProfileSerializer
    """serializer is the class name which i have defined"""
    permission_classes = [AllowAny]
    """anyone can register here as permission_class is alllowany"""

class CustomTokenObtainPairView(TokenObtainPairView):
        pass

