from rest_framework import viewsets

from ..serialiazers import LocationSerializer
from ..models import Location
from .mixins import AuthPermissionMixin


class LocationViewSet(AuthPermissionMixin, viewsets.ModelViewSet):

    serializer_class = LocationSerializer
    queryset = Location.objects.all()

