from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from employees.views import EmployeeViewSet, FingerPrintViewSet, RFIDCardViewSet


router = routers.DefaultRouter()
router.register(r'', EmployeeViewSet)
router.register(r'rfid', RFIDCardViewSet)
router.register(r'fingerprint', FingerPrintViewSet)


urlpatterns = [
    path('', include(router.urls)),
]