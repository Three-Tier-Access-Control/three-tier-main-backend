from django.urls import path, include
from employees.models import Employee, FingerPrint, RFIDCard
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField() 

    class Meta:
        model = Employee
        # fields = '__all__'

        fields = ['first_name', 'last_name', 'email_address', 'photo']

class RFIDCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RFIDCard
        fields = '__all__'

class FingerPrintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FingerPrint
        fields = '__all__'

