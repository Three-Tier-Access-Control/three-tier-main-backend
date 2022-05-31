from django.shortcuts import render
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from employees.models import Employee, FingerPrint, RFIDCard
from employees.serializers import EmployeeSerializer, FingerPrintSerializer, RFIDCardSerializer


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class RFIDCardViewSet(viewsets.ModelViewSet):
    queryset = RFIDCard.objects.all()
    serializer_class = RFIDCardSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        employee_id = data['employee']
        employee = Employee.objects.get(id=employee_id)

        if RFIDCard.objects.filter(employee=employee):
            return Response({"detail": f"Card for employee {employee_id} already exists "}, status=status.HTTP_400_BAD_REQUEST)


        rfid = RFIDCard.objects.create(employee=employee,
                                       uid_tag=data['uid_tag'])

        serializer = RFIDCardSerializer(rfid)
        return Response(serializer.data)


class FingerPrintViewSet(viewsets.ModelViewSet):
    queryset = FingerPrint.objects.all()
    serializer_class = FingerPrintSerializer
