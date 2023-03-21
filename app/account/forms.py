import uuid

from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse


User = get_user_model()


class UserSignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2'
        )

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('Password should math')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        user.is_active = False

        user.username = uuid.uuid4()

        user.set_password(password)
        user.save()

        self._send_email()

        return user

    def _send_email(self):

        subject = 'Thank you for sign up on our website!'
        recipient = settings.DEFAULT_FROM_EMAIL
        path = reverse('account:activate', args=(self.instance.username, ))
        message = f"""
            {settings.HTTP_SCHEMA}://{settings.HOST}{path}
        """

        from django.core.mail import send_mail
        send_mail(
            subject=subject,
            message=message,
            from_email=recipient,
            recipient_list=[self.instance.email],
            fail_silently=False
        )
