#writing serializers
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """to make the complex object turn into simpler data for reading purpose"""
    class Meta:
        model = Profile #defining which model i am using to inherit
        fields = '__all__'
        extra_kwargs = {'password' : {'write_only' : True}}

        def create(self, validated_data):
            """this check that when user is create this fucntion is called"""
            user = Profile.objects.create_user(**validated_data) 
            return user
        


