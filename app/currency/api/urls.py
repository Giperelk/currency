from django.urls import path

from currency.api.views import RateViewSet, ContactUsViewSet, SourceApiView
from rest_framework.routers import DefaultRouter

app_name = 'api-currency'

urlpatterns = [
    path('sources/', SourceApiView.as_view(), name='sources'),
]

for view_set, base_name in (
        (RateViewSet, 'rates'),
        (ContactUsViewSet, 'contactus')
):
    router = DefaultRouter()
    router.register(base_name, view_set, basename=base_name)
    urlpatterns += router.urls
