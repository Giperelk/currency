from django.contrib import admin
from currency.models import Rate, ContactUs, Source
from rangefilter.filters import DateRangeFilter
from import_export.admin import ImportExportModelAdmin


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'currency',
        'buy',
        'sell',
        'source',
        'created',
    )
    list_filter = (
        'currency',
        ('created', DateRangeFilter),
    )
    search_fields = (
        'source',
        'currency',
    )


@admin.register(ContactUs)
class ContactUsAdmin(ImportExportModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(Source)
class SourceAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'source_url',
        'phone_number',
        'contact_email',
    )
    search_fields = (
        'name',
    )
