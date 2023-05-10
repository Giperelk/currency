from rest_framework import viewsets

from currency.models import Rate, Source, ContactUs
from currency.api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.api.paginators import TenThousandPagination
from currency.filters import RateFilter, ContactUsFilter

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    pagination_class = TenThousandPagination


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = TenThousandPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = RateFilter
    ordering_fields = (
        'id',
        'buy',
        'sale',
        'source',
    )


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    pagination_class = TenThousandPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter,
    )
    filterset_class = ContactUsFilter
    ordering_fields = (
        'id',
        'subject',
    )
    search_fields = ['subject', 'message']
