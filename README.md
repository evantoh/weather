# weather
# weather
<img src="https://github.com/evantoh/weather/blob/main/images/weather.jpeg" width="100%">



## Overview
This is an API built with Django Rest Framework, and allows to retrieve real time weather data for any location acreoss cities from a third  party API called Open Weather (http://api.weatherapi.com/v1).

The API support GET requests in the following endpoint: <strong> /api/locations/{city}/?days={number_of_days}</strong>.

where the variable "City" is a string. Example: Nairobi, and the variable "Days" is the number of days to pass for forecasting



## Content
* [Overview](#Overview)
* [Technologies](#Technologies)
* [Setup](#Setup)
* [Usage](#Usage)
* [Testing](#Testing)


## Technologies

This project uses the following Python dependencies:
* Requires Python >=3.8
* Django==3.2.6
* asgiref==3.5.2
* certifi==2022.9.24
* charset-normalizer==2.1.1
* Django==3.2
* djangorestframework==3.12.4
* idna==3.4
* pytz==2022.2.1
* requests==2.28.1
* sqlparse==0.4.2
* urllib3==1.26.12



## Setup
To run locally
