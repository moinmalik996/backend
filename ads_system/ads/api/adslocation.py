from rest_framework import viewsets

from ..models import AdsLocation
from ..serialiazers import AdsLocationSerializer


class AdsLocationViewset(viewsets.ModelViewSet):

    serializer_class = AdsLocationSerializer
    queryset = AdsLocation.objects.all()