from django.db.models import fields
from rest_framework import serializers 
from .models import  Employees 

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees 
        #fields = ['id','title' , 'author' , 'email']
        fields = '__all__'