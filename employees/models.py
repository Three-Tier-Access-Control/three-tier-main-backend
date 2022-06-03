from re import T
from django.db import models
from utils.models import TimeStampedUUIDModel
from django.utils import timezone
import os
import sys


# Create your models here.


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond 
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class Employee(TimeStampedUUIDModel):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email_address = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=254)
    city = models.CharField(max_length=254, null=True, blank=True)
    street_address = models.CharField(max_length=254, null=True, blank=True)

    photo = models.ImageField(upload_to=upload_to, blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    # @property
    # def file_url(self):
    #     return self.file.url

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class RFIDCard(TimeStampedUUIDModel):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="rfids")
    uid_tag = models.CharField(max_length=254)

    class Meta:
        verbose_name = "RFID Card"
        verbose_name_plural = "RFID Cards"
        ordering = ('-created',)
    def __str__(self):
        return self.uid_tag

class FingerPrint(TimeStampedUUIDModel):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="fingerprints")
    fingerprint_id = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name = "Fingerprint"
        verbose_name_plural = "Fingerprints"
        ordering = ('-created',)
    
    def __str__(self):
        return f"{self.fingerprint_id}"
