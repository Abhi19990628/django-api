from .models import Employess
from rest_framework import serializers
from django.contrib.auth.models import User
class EmployessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employess
        fields= '__all__'
    
class UsersSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'