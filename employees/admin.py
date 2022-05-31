from django.contrib import admin

from employees.models import Employee, RFIDCard, FingerPrint

admin.site.register(Employee)
admin.site.register(RFIDCard)
admin.site.register(FingerPrint)


