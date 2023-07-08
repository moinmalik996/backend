from rest_framework import serializers

from ..models import AdsLocation


class AdsLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdsLocation
        fields = '__all__'