
""" Weather API, and function Tests."""
# Run the API locally is required to carry out the tests

# Django rest framework
from rest_framework import status
from rest_framework.test import APITestCase

# Utils
from .requestapi import get_weather


# Create your tests here.

class WeatherAPITest(APITestCase):
    """ Run test over the our weather API to check
        the response status ."""

    def test_api_url(self):
        """ Make a GET request to the API endpoint."""

        url = 'http://127.0.0.1:8000/api/location/Nairobi/?days=10'  # Weather API endpoint
        response = self.client.get(url)  # Response object from the API

        # Check if the response status code is 200
        self.assertTrue(status.is_success(response.status_code))

class FuncThirdAPITest(APITestCase):
    """ Run test over the test_get_weather() function
        from the requestapi.py module."""

    def test_get_weather(self):
        """Test the test_get weather() function."""
        # Testing variables
        location = 'Nairobi'
        days = '10'
        weather_data = get_weather(location, days)  # Call to the function

        # Check if the result dictionary has the correct location_name value
        self.assertEqual(weather_data['location'], 'Nairobi')


    def test_get_weather(self):
        """Test the test_get weather() function."""
        # Testing variables
        location = 'Nairobi'
        days = '10'
        weather_data = get_weather(location, days)  # Call to the function

        # Check if the result dictionary has the correct region value
        self.assertEqual(weather_data['region'], '"Nairobi Area')