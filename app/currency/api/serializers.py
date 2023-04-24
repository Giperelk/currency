from rest_framework import serializers

from django.conf import settings

from currency.tasks import send_mail
from currency.models import Rate, Source, ContactUs


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'created',
            'source',
        )


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = (
            'name',
            'source_url'
        )


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )

    def create(self, validated_data):

        subject = 'Contact Us'
        recipient = settings.DEFAULT_FROM_EMAIL
        message = f"""
                            Reply to email: {validated_data['email_from']}
                            Subject: {validated_data['subject']}
                            Body: {validated_data['message']}
                            """

        send_mail.delay(
            subject=subject,
            from_email=recipient,
            recipient_list=[recipient],
            message=message,
            fail_silently=False
        )

        return super().create(validated_data)
