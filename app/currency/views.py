from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, ContactUsForm, SourceForm


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'models/rate/list.html'


class RateDetailsView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'models/rate/details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'models/rate/create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    form_class = RateForm
    template_name = 'models/rate/update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'models/rate/delete.html'
    success_url = reverse_lazy('currency:rate-list')


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'models/contactus/list.html'


class ContactUsDetailsView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'models/contactus/details.html'


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'models/contactus/create.html'
    success_url = reverse_lazy('currency:contactus-list')


class ContactUsUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'models/contactus/update.html'
    success_url = reverse_lazy('currency:contactus-list')
    queryset = ContactUs.objects.all()


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'models/contactus/delete.html'
    success_url = reverse_lazy('currency:contactus-list')


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'models/source/list.html'


class SourceDetailsView(DetailView):
    queryset = Source.objects.all()
    template_name = 'models/source/details.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    template_name = 'models/source/create.html'
    success_url = reverse_lazy('currency:source-list')


class SourceUpdateView(UpdateView):
    form_class = SourceForm
    template_name = 'models/source/update.html'
    success_url = reverse_lazy('currency:source-list')
    queryset = Source.objects.all()


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    template_name = 'models/source/delete.html'
    success_url = reverse_lazy('currency:source-list')
