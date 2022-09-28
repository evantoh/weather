# Temperature Api

<img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.formula1.com%2Fcontent%2Fdam%2Ffom-website%2Fmanual%2FXPB_Images%2FMexico_2019%2FPre%2F2019mexicoweather-forecast-v02.jpg&imgrefurl=https%3A%2F%2Fwww.formula1.com%2Fen%2Flatest%2Farticle.whats-the-weather-forecast-for-the-mexican-grand-prix-2019.40VPwxKyo9f65wKccMmIwz.html&tbnid=g_9rGwLaY3iIRM&vet=10CIECEDMoygFqFwoTCOjUhLzXtfoCFQAAAAAdAAAAABAC..i&docid=0RfbM4jOV2bUjM&w=1920&h=1080&q=weather%20%20forecast%20&ved=0CIECEDMoygFqFwoTCOjUhLzXtfoCFQAAAAAdAAAAABAC" width="300">



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






Author: Evans Mmwenda | 2022
