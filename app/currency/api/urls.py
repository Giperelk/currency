from currency.api.views import RateViewSet, ContactUsViewSet, SourceViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('rates', RateViewSet, basename='rates')
router.register('contactus', ContactUsViewSet, basename='contactus')
router.register('sources', SourceViewSet, basename='sources')

app_name = 'api-currency'

urlpatterns = []

urlpatterns += router.urls
