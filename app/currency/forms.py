from django import forms

from currency.models import Rate, ContactUs, Source


class RateForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
            'source',
            'currency'
        )


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )


class SourceForm(forms.ModelForm):

    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
            'phone_number',
            'contact_email',
            'logo'
        )
