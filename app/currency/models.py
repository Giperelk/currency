from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Rate(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=25)
    buy = models.DecimalField(max_digits=8, decimal_places=2)
    sell = models.DecimalField(max_digits=8, decimal_places=2)
    source = models.CharField(max_length=25, default='')


class ContactUs(models.Model):

    email_from = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()


class Source(models.Model):

    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)
    phone_number = PhoneNumberField(blank=True)
    contact_email = models.EmailField(blank=True)
