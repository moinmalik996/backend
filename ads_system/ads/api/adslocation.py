from django.db import transaction

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from ..models import AdsLocation
from ..serialiazers import AdsLocationSerializer
from .mixins import AuthPermissionMixin


class AdsLocationViewset(AuthPermissionMixin, viewsets.ModelViewSet):

    serializer_class = AdsLocationSerializer
    queryset = AdsLocation.objects.all()


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        ad = serializer.validated_data['ad']
        location = serializer.validated_data['location']
        adslocation = AdsLocation.objects.filter(
            ad=ad,
            location=location
        ).exists()

        if not adslocation:
            adslocation = serializer.save()
            serializer = self.serializer_class
            serializer = serializer(adslocation)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'error': 'This ad already exist'
            },status=status.HTTP_409_CONFLICT)