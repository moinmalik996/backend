from rest_framework import serializers

from ..models import Ad


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ['id', 'name', 'created_at', 'updated_at']
