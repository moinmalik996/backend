from django.urls import path, include
from rest_framework import routers

from .api import AdViewSet, LocationViewSet, AdsLocationViewset, RunningAdsViewSet

base_router = routers.DefaultRouter()
runningads_router = routers.DefaultRouter()

base_router.register('ad', AdViewSet, basename='ad-api')
base_router.register('location', LocationViewSet, basename='location-api')
base_router.register('adslocation', AdsLocationViewset, basename='adslocation-api')
runningads_router.register('running-ads', RunningAdsViewSet, basename='running-ads-api')

urlpatterns = [
    path('', include(base_router.urls)),
    path('location/<int:id>/', include(runningads_router.urls)),
]