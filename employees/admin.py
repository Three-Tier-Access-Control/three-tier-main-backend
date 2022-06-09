from django.contrib import admin
from django.contrib.auth.models import Group
from employees.models import Employee, RFIDCard, FingerPrint


admin.site.unregister(Group)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address", "phone_number", "fingerprint","created")
    list_filter = ("first_name", "last_name")
    date_hierarchy = 'created'

@admin.register(RFIDCard)
class RFIDCardAdmin(admin.ModelAdmin):
    list_display = ("employee", "uid_tag", "created")
    list_filter = ("employee", "uid_tag",)
    date_hierarchy = 'created'

@admin.register(FingerPrint)
class FingerPrintAdmin(admin.ModelAdmin):
    list_display = ("employee", "fingerprint_id", "created")
    list_filter = ("employee", "fingerprint_id",)
    date_hierarchy = 'created'
