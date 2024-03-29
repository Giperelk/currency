from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django_filters.views import FilterView

from currency.mixins import ModifiedPagesMixin
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, ContactUsForm, SourceForm
from currency.tasks import send_mail
from currency.filters import RateFilter, SourceFilter, ContactUsFilter


class RateListView(ModifiedPagesMixin, FilterView):
    paginate_by = 10
    queryset = Rate.objects.all().select_related('source')
    template_name = 'models/rate/list.html'

    filterset_class = RateFilter


class RateDetailsView(LoginRequiredMixin, DetailView):
    queryset = Rate.objects.all()
    template_name = 'models/rate/details.html'


class RateCreateView(UserPassesTestMixin, CreateView):
    form_class = RateForm
    template_name = 'models/rate/create.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class RateUpdateView(UserPassesTestMixin, UpdateView):
    form_class = RateForm
    template_name = 'models/rate/update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()

    def test_func(self):
        return self.request.user.is_superuser


class RateDeleteView(UserPassesTestMixin, DeleteView):
    queryset = Rate.objects.all()
    template_name = 'models/rate/delete.html'
    success_url = reverse_lazy('currency:rate-list')

    def test_func(self):
        return self.request.user.is_superuser


class ContactUsListView(ModifiedPagesMixin, FilterView):
    paginate_by = 10
    queryset = ContactUs.objects.all()
    template_name = 'models/contactus/list.html'

    filterset_class = ContactUsFilter


class ContactUsDetailsView(DetailView):
    queryset = ContactUs.objects.all()
    template_name = 'models/contactus/details.html'


class ContactUsCreateView(CreateView):
    form_class = ContactUsForm
    template_name = 'models/contactus/create.html'
    success_url = reverse_lazy('currency:contactus-list')

    def form_valid(self, form):

        cleaned_data = form.cleaned_data
        redirect = super().form_valid(form)

        subject = 'Contact Us'
        recipient = settings.DEFAULT_FROM_EMAIL
        message = f"""
                    Reply to email: {cleaned_data['email_from']}
                    Subject: {cleaned_data['subject']}
                    Body: {cleaned_data['message']}
                    """

        send_mail.delay(
            subject=subject,
            from_email=recipient,
            recipient_list=[recipient],
            message=message,
            fail_silently=False
        )

        return redirect


class ContactUsUpdateView(UpdateView):
    form_class = ContactUsForm
    template_name = 'models/contactus/update.html'
    success_url = reverse_lazy('currency:contactus-list')
    queryset = ContactUs.objects.all()


class ContactUsDeleteView(DeleteView):
    queryset = ContactUs.objects.all()
    template_name = 'models/contactus/delete.html'
    success_url = reverse_lazy('currency:contactus-list')


class SourceListView(ModifiedPagesMixin, FilterView):
    paginate_by = 10
    queryset = Source.objects.all()
    template_name = 'models/source/list.html'

    filterset_class = SourceFilter


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


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('currency:rate-list')
    model = get_user_model()
    queryset = get_user_model().objects.all()
    fields = (
        'first_name',
        'last_name',
    )

    def get_object(self, queryset=None):
        return self.request.user
