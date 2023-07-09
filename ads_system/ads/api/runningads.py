from rest_framework import viewsets

from ..serialiazers import AdsLocationSerializer
from ..models import Location
from .mixins import AuthPermissionMixin


class RunningAdsViewSet(AuthPermissionMixin, viewsets.ReadOnlyModelViewSet):

    serializer_class = AdsLocationSerializer

    def get_queryset(self):
        location_id = self.kwargs.get('id', None)
        location = Location.objects.get(id=location_id)
        queryset = location.ads.with_expiration_data() \
                           .filter(date_expired=False, max_reached=False)
        return queryset
        

