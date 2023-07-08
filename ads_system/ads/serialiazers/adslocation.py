from django.db.models import F
from rest_framework import serializers

from ..models import AdsLocation, Ad, Location
from .ad import AdSerializer
from .location import LocationSerializer

class AdsLocationSerializer(serializers.ModelSerializer):
    ad = AdSerializer()
    location = LocationSerializer()
    class Meta:
        model = AdsLocation
        fields = '__all__'


    def create(self, validated_data):
        ad_name = validated_data.pop('ad').get('name')
        location_name = validated_data.pop('location').get('name')

        location = Location.objects.create(name=location_name)
        ad = Ad.objects.create(name=ad_name)

        adslocation = AdsLocation.objects.create(
            ad = ad,
            location = location,
            **validated_data
        )
        return adslocation
    
    def update(self, instance, validated_data):
        """
        This function will only update the visits data for a particular Ad and Location
        """
        instance.visits=validated_data.get('visits')
        instance.save()
        return instance
