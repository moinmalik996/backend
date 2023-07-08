from django.urls import path, include
from rest_framework import routers

from .api import AdViewSet, LocationViewSet, AdsLocationViewset

router = routers.DefaultRouter()

router.register('ad', AdViewSet, basename='ad-api')
router.register('location', LocationViewSet, basename='location-api')
router.register('adslocation', AdsLocationViewset, basename='adslocation-api')

urlpatterns = [
    path('', include(router.urls)),
]