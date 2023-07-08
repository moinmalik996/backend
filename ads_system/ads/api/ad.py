from rest_framework import viewsets

from ..serialiazers import AdSerializer
from ..models import Ad
from .mixins import AuthPermissionMixin


class AdViewSet(AuthPermissionMixin, viewsets.ModelViewSet):

    serializer_class = AdSerializer
    queryset = Ad.objects.all()

