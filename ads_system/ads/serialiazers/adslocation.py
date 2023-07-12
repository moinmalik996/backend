from django.db import transaction
from django.db.models import F
from django.utils import timezone
from rest_framework import serializers

from ..models import AdsLocation

class AdsLocationSerializer(serializers.ModelSerializer):

    max_visits = serializers.IntegerField(min_value=1)
    visits = serializers.IntegerField(min_value=0)
    end_date = serializers.DateTimeField()
    class Meta:
        model = AdsLocation
        fields = '__all__'

    
    def update(self, instance, validated_data):
        """
        This function will only update the visits data for a particular Ad and Location
        """
        instance.visits=validated_data.get('visits')
        instance.save()
        return instance
    
    def validate(self, data):

        # region -> end_date validation
        if not data['end_date']:
            raise serializers.ValidationError('End date cannot be null')

        if data['end_date'] < timezone.now():
            raise serializers.ValidationError('End date cannot be less than now')
        #endregion


        # region -> visits validation
        if data['visits'] > data['max_visits']:
            raise serializers.ValidationError('No. of visits cannot be greater than max visits')
        # endregion
        
        return data
