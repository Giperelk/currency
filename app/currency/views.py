# from django.shortcuts import render
from django.http import HttpResponse

from currency.models import Rate, ContactUs


def list_rates(request):
    qs = Rate.objects.all()
    result = []

    for rate in qs:
        result.append(
            f'id: {rate.id}, '
            f'buy: {rate.buy}, '
            f'sell: {rate.sell}, '
            f'currency: {rate.currency}, '
            f'source: {rate.source}, '
            f'created: {rate.created}'
        )

    return HttpResponse(str(result))


def contactus_list(request):
    qs = ContactUs.objects.all()
    result = []

    for message in qs:
        result.append(
            f'id: {message.id}, '
            f'email_from: {message.email_from}, '
            f'subject: {message.subject}, '
            f'message: {message.message}'
        )

    return HttpResponse(str(result))
