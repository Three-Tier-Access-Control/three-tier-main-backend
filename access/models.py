from django.db import models
from employees.models import Employee
from utils.models import TimeStampedUUIDModel


class AccessLog(TimeStampedUUIDModel):
    IN = "in"
    OUT = "out"
    DIRECTION_CHOICES = [(IN, "IN"), (OUT, "OUT"), ]
    employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, related_name="access_logs", null=True, blank=True)
    direction = models.CharField(
        max_length=254, choices=DIRECTION_CHOICES, default=IN)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Access Log"
        verbose_name_plural = "Access Logs"
        ordering = ('-created',)

    def __str__(self):
        return f"{self.employee}"
