from django.urls import path

from currency.views import (
    RateListView, RateDetailsView, RateCreateView, RateUpdateView, RateDeleteView,
    ContactUsListView, ContactUsDetailsView, ContactUsCreateView, ContactUsUpdateView, ContactUsDeleteView,
    SourceListView, SourceDetailsView, SourceCreateView, SourceUpdateView, SourceDeleteView,
)

rate_patterns = [
    path('rates/list/', RateListView.as_view(), name='rate-list'),
    path('rates/<int:pk>/', RateDetailsView.as_view(), name='rate-details'),
    path('rates/create/', RateCreateView.as_view(), name='rate-create'),
    path('rates/<int:pk>/update/', RateUpdateView.as_view(), name='rate-update'),
    path('rates/<int:pk>/delete/', RateDeleteView.as_view(), name='rate-delete'),
]

contact_us_patterns = [
    path('contactus/list/', ContactUsListView.as_view(), name='contactus-list'),
    path('contactus/<int:pk>/', ContactUsDetailsView.as_view(), name='contactus-details'),
    path('contactus/create/', ContactUsCreateView.as_view(), name='contactus-create'),
    path('contactus/<int:pk>/update/', ContactUsUpdateView.as_view(), name='contactus-update'),
    path('contactus/<int:pk>/delete/', ContactUsDeleteView.as_view(), name='contactus-delete'),
]

source_patterns = [
    path('sources/list/', SourceListView.as_view(), name='source-list'),
    path('sources/<int:pk>/', SourceDetailsView.as_view(), name='source-details'),
    path('sources/create/', SourceCreateView.as_view(), name='source-create'),
    path('sources/<int:pk>/update/', SourceUpdateView.as_view(), name='source-update'),
    path('sources/<int:pk>/delete/', SourceDeleteView.as_view(), name='source-delete'),
]


app_name = 'currency'

urlpatterns = [
    *rate_patterns,
    *contact_us_patterns,
    *source_patterns,
]
