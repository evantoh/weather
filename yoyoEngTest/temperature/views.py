""" Weather API views."""
from django.http import HttpResponse
# Django
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Serializers
from .serializers import WeatherSerializer

# Utilities
import json
from .requestapi import get_weather

# Cache
from django.core.cache import cache


@api_view(['GET'])
def weather_detail(request,city):
    """Receive the client request and return a JSON
        response with the given location and number of days."""

    serializer = WeatherSerializer(data=request.GET)  # Pass the request data to the serializer WeatherSerializer() model
    serializer.is_valid()  # return True if serializer fields are valid

    # Retrieve the validated data from serializer
    # location = serializer.validated_data['location']
    days = serializer.validated_data['days']

    weather_data = get_weather(city, days)  # Call to get_weather function which returns a formatted dictionary

    #  Using Low-level cache API
    if cache_data := cache.get("{}-{}".format(city, days)):  # look if the key is already in the cache table
        return Response(weather_data)  # Return the stored object

    cache.set("{}-{}".format(city, days), weather_data,
              timeout=60 * 2)  # Storing the object in the cache table with a Timeout of 2 Minutes

    return Response(weather_data)







