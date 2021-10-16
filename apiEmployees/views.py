from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.views.decorators import csrf
from rest_framework.parsers  import JSONParser
from rest_framework.views import APIView 
from .models import Employees 
from .serializers import EmployeesSerializer 
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics 
from rest_framework import mixins
# Create your views here.
class EmployeesAPIView(APIView):
    def get(self , request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees , many = True)
        return Response(serializer.data)

    def post(self , request):
        serializer = EmployeesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)



class EmployeesDetails(APIView):

    def get_object(self , pk):
        try:
            return  Employees.objects.get(id = pk)
        except Employees.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self , request,pk):
        employe = self.get_object(pk)
        serializer = EmployeesSerializer(employe)
        return Response(serializer.data )

    def put(self , request , pk):
        employe = self.get_object(pk)
        serializer = EmployeesSerializer(employe , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data )
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

    def delete (self , request , pk):
        employe = self.get_object(pk)
        employe.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)