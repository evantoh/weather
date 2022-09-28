""" API Serializers:"""
from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
     # Serializer fields
    days = serializers.CharField(max_length=2)