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
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data, instance=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RFIDCardViewSet(viewsets.ModelViewSet):
    queryset = RFIDCard.objects.all()
    serializer_class = RFIDCardSerializer


class FingerPrintViewSet(viewsets.ModelViewSet):
    queryset = FingerPrint.objects.all()
    serializer_class = FingerPrintSerializer
