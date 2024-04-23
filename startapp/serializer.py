from .models import Employess
from rest_framework import serializers


class EmployessSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    age=serializers.CharField(max_length=3)
    phone=serializers.CharField(max_length=10)
    
    def create(self , validated_data):
        return Employess.objects.create(**validated_data)
    
    def update(self,  employe , validated_data):
        new_employess=Employess(**validated_data)
        new_employess.id=employe.id
        new_employess.save()
        return new_employess
    
class UsersSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=100)
   