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
        try:
            data = request.data
            employee_id = data['employee']
            uid_tag = data['uid_tag']
            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response({"detail": f"Employee {employee_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if RFIDCard.objects.filter(employee=employee):
            return Response({"detail": f"Card for employee {employee_id} already exists "}, status=status.HTTP_400_BAD_REQUEST)

        if RFIDCard.objects.filter(uid_tag=uid_tag):
            return Response({"detail": f"Card id {uid_tag} already exists "}, status=status.HTTP_400_BAD_REQUEST)


        rfid = RFIDCard.objects.create(employee=employee, uid_tag=uid_tag)

        serializer = RFIDCardSerializer(rfid)
        return Response(serializer.data)


class FingerPrintViewSet(viewsets.ModelViewSet):
    queryset = FingerPrint.objects.all()
    serializer_class = FingerPrintSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            employee_id = data['employee']
            fingerprint_id = data['fingerprint_id']

            employee = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            return Response({"detail": f"Employee {employee_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if FingerPrint.objects.filter(employee=employee):
            return Response({"detail": f"Fingerprint for employee {employee_id} already exists"}, status=status.HTTP_400_BAD_REQUEST)

        if FingerPrint.objects.filter(fingerprint_id=fingerprint_id):
            return Response({"detail": f"Fingerprint id {fingerprint_id} already exists"}, status=status.HTTP_400_BAD_REQUEST)

        fingerprint = FingerPrint.objects.create(employee=employee,
                                                 fingerprint_id=fingerprint_id)

        serializer = FingerPrintSerializer(fingerprint)
        return Response(serializer.data)
