from access.models import AccessLog
from rest_framework import serializers
from employees.serializers import EmployeeSerializer


class AccessLogSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(required=True)

    class Meta:
        model = AccessLog
        fields = '__all__'
        depth = 1 


