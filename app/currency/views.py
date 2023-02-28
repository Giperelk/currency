from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, ContactUsForm, SourceForm


def rate_all(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates
    }

    return render(request, 'models/rate/all.html', context)


def rate_details(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'rate': rate
    }

    return render(request, 'models/rate/details.html', context)


def rate_create(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/all/')
    elif request.method == 'GET':
        form = RateForm()

    context = {
        'form': form
    }

    return render(request, 'models/rate/create.html', context)


def rate_update(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/rate/all/')
    elif request.method == 'GET':
        form = RateForm(instance=rate)

    context = {
        'form': form,
    }
    return render(request, 'models/rate/update.html', context)


def rate_delete(request, pk):
    rate = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/all/')
    elif request.method == 'GET':
        context = {
            'rate': rate,
        }
        return render(request, 'models/rate/delete.html', context)


def contactus_all(request):
    tasks = ContactUs.objects.all()

    context = {
        'tasks': tasks
    }

    return render(request, 'models/contactus/all.html', context)


def contactus_details(request, pk):
    task = get_object_or_404(ContactUs, pk=pk)

    context = {
        'task': task
    }

    return render(request, 'models/contactus/details.html', context)


def contactus_create(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contactus/all/')

    elif request.method == 'GET':
        form = ContactUsForm()

    context = {
        'form': form
    }

    return render(request, 'models/contactus/create.html', context)


def contactus_update(request, pk):
    contactus = get_object_or_404(ContactUs, pk=pk)

    if request.method == 'POST':
        form = ContactUsForm(request.POST, instance=contactus)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contactus/all/')
    elif request.method == 'GET':
        form = ContactUsForm(instance=contactus)

    context = {
        'form': form,
    }
    return render(request, 'models/contactus/update.html', context)


def contactus_delete(request, pk):
    contactus = get_object_or_404(ContactUs, pk=pk)

    if request.method == 'POST':
        contactus.delete()
        return HttpResponseRedirect('/contactus/all/')
    elif request.method == 'GET':
        context = {
            'contactus': contactus,
        }
        return render(request, 'models/contactus/delete.html', context)


def source_all(request):
    sources = Source.objects.all()

    context = {
        'sources': sources
    }

    return render(request, 'models/source/all.html', context)


def source_details(request, pk):
    source = get_object_or_404(Source, pk=pk)

    context = {
        'source': source
    }

    return render(request, 'models/source/details.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/all/')
    elif request.method == 'GET':
        form = SourceForm()

    context = {
        'form': form
    }

    return render(request, 'models/source/create.html', context)


def source_update(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/all/')
    elif request.method == 'GET':
        form = SourceForm(instance=source)

    context = {
        'form': form,
    }
    return render(request, 'models/source/update.html', context)


def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)

    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/all/')
    elif request.method == 'GET':
        context = {
            'source': source,
        }
        return render(request, 'models/source/delete.html', context)
