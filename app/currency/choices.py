from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    EUR = 1, 'Euro'
    USD = 2, 'US Dollar'


class RateRequestResponseLogChoices(models.IntegerChoices):
    GET = 1, 'GET'
    POST = 2, 'POST'
    PUT = 3, 'PUT'
    PATCH = 4, 'PATCH'
    DELETE = 5, 'DELETE'
