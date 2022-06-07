from access.models import AccessLog
from access.serializers import AccessLogSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from employees.models import Employee


class AccessLogViewSet(viewsets.ModelViewSet):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer
    permission_classes = []
    authentication_classes = []
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['direction']
    search_fields = ['direction']

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            employee_id = data['employee']
            direction = data['direction']
            entry_status = data['status']
            employee = Employee.objects.get(id=employee_id)

            log = AccessLog.objects.create(employee=employee, direction=direction, status=entry_status)

            serializer = AccessLogSerializer(log)
            return Response(serializer.data)

        except Employee.DoesNotExist:
            return Response({"detail": f"Employee {employee_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"detail": f"Error: {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

