from django.shortcuts import render
from .models import Employess
from .serializer import EmployessSerializer, UsersSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def employessListView(request):
    if request.method  == 'GET':
        employess= Employess.objects.all()
        serializer = EmployessSerializer(employess, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer=EmployessSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
@api_view(['GET','DELETE','PUT'])
def EmployessDetailsview(request,pk):

    try:
        employess=Employess.objects.get(pk=pk)
    except Employess.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'DELETE':
        employess.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'GET':
        Serializer=EmployessSerializer(employess)
        return Response(Serializer.data)
    
    elif request.method == 'PUT':
        serializer=EmployessSerializer(employess , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
    
@api_view(['GET'])
def UserListView(request):
    if request.method == 'GET':
        Users = User.objects.all() 
        serializer = UsersSerializer(Users , many=True)
        return Response(serializer.data)





