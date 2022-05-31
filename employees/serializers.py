from django.urls import path, include
from employees.models import Employee, FingerPrint, RFIDCard
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

# Serializers define the API representation.


class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField()

    class Meta:
        model = Employee
        fields = '__all__'


class RFIDCardSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(required=True)

    class Meta:
        model = RFIDCard
        fields = '__all__'
        depth = 1 


class FingerPrintSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = FingerPrint
        fields = '__all__'
        depth = 1 
