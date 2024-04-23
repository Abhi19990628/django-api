from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Employess
from .serializer import EmployessSerializer, UsersSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def employessListView(request):
    if request.method  == 'GET':
        employess= Employess.objects.all()
        serializer = EmployessSerializer(employess,many=True)
        return JsonResponse(serializer.data , safe=False)
    elif request.method == 'POST':
        jsonData= JSONParser().parse(request)
        serializer=EmployessSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , safe=False)
        else:
            return JsonResponse(serializer.errors , safe=False)
        
        
@csrf_exempt       
def EmployessDetailsview(request,pk):

    try:
        employess=Employess.objects.get(pk=pk)
    except Employess.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'DELETE':
        employess.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'GET':
        Serializer=EmployessSerializer(employess)
        return JsonResponse(Serializer.data, safe=False)
    
    elif request.method == 'PUT':
        pass  
    
    
    
def UserListView(request):
    Users = User.objects.all() 
    serializer = UsersSerializer(Users , many=True)
    return JsonResponse(serializer.data , safe=False)

