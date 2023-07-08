from rest_framework import viewsets


from ..serialiazers import LocationSerializer
from ..models import Location

class LocationViewSet(viewsets.ModelViewSet):

    serializer_class = LocationSerializer
    queryset = Location.objects.all()

