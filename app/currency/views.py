from django.shortcuts import render
from currency.models import Rate, ContactUs


def list_rates(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'list_rates.html', context)


def contactus_list(request):
    tasks = ContactUs.objects.all()

    context = {
        'tasks': tasks
    }

    return render(request, 'list_contactus.html', context)
