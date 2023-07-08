from rest_framework import viewsets

from ..serialiazers import AdSerializer
from ..models import Ad


class AdViewSet(viewsets.ModelViewSet):

    serializer_class = AdSerializer
    queryset = Ad.objects.all()

