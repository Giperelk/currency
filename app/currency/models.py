from currency import choices as mch
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.templatetags.static import static


class Rate(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=mch.RateCurrencyChoices.choices,
        default=mch.RateCurrencyChoices.EUR
    )
    buy = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.DecimalField(max_digits=8, decimal_places=2)
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    def __str__(self):
        return f'Source {{{self.source}}} on {self.created} for {self.get_currency_display()}'


class ContactUs(models.Model):

    email_from = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'From user {{{self.email_from}}} about "{self.subject}"'


def source_logo_path(instance, filename):
    return f"currency/sources/{instance.id}/logos/{filename}"


class Source(models.Model):

    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=64, unique=True)
    phone_number = PhoneNumberField(blank=True)
    contact_email = models.EmailField(blank=True)
    logo = models.FileField(
        default='',
        null=True,
        blank=True,
        upload_to=source_logo_path
    )

    def __str__(self):
        return f'{self.name}'

    @property
    def logo_url(self):
        if self.logo:
            return self.logo.url
        return static('nologo.jpg')


class RequestResponseLog(models.Model):

    path = models.CharField(max_length=150)
    request_method = models.PositiveSmallIntegerField(
        choices=mch.RateRequestResponseLogChoices.choices,
        default=mch.RateRequestResponseLogChoices.GET
    )
    time = models.PositiveIntegerField()
