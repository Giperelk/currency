from django.db import models


class Rate(models.Model):

    created = models.DateTimeField(auto_created=True)
    currency = models.CharField(max_length=25)
    buy = models.DecimalField(max_digits=8, decimal_places=2)
    sell = models.DecimalField(max_digits=8, decimal_places=2)
    source = models.CharField(max_length=25, default='')


class ContactUs(models.Model):

    email_from = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
