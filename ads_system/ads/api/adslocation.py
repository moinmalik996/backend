from rest_framework import viewsets

from ..models import AdsLocation
from ..serialiazers import AdsLocationSerializer
from .mixins import AuthPermissionMixin


class AdsLocationViewset(AuthPermissionMixin, viewsets.ModelViewSet):

    serializer_class = AdsLocationSerializer
    queryset = AdsLocation.objects.all()
