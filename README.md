# weather
<img src="https://github.com/evantoh/weather/blob/main/images/weather.jpeg" width="100%">



## Overview
This is an API built with Django Rest Framework, and allows to retrieve real time weather data for any location acreoss cities from a third  party API called Open Weather (http://api.weatherapi.com/v1).

The API support GET requests in the following endpoint: <strong> /api/locations/{city}/?days={number_of_days}</strong>.

where the variable "city" is a string. Example: London, and the variable "number_of_days" is the number of days  for forecasting e.g 10



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



```python
# Within a local folder, Clone this repository

$ git clone https://github.com/evantoh/weather.git

```
```python
# The project has the following file structure
# Once we carry out the migrations a db.sqlite3 database 
#   will be installed automatically.

├── db.sqlite3
├── __init__.py
├── manage.py
├── requirements.txt
├── temperature
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── requestapi.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── yoyoEngTest
    ├── settings.py
    ├── urls.py
    └── wsgi.py
├── images
│   ├── apiResponse.png
│   ├── errorMessage.png
│   ├── Results.png
│   ├── url.png
│   └── weather.jpeg
├── README.md
```
```python
# Create and activate a virtual environment in order to install the requirements.txt
$python -m venv .env
$source .env/bin/activate
$pip install -r requirements.txt

```

```python
# Configure the given environment variables in your O.S.
DJANGO_SECRET_KEY='xxxxxxxxxx'
WEATHER_SECRET_APIKEY='xxxxxxxxxx'
```

```python
# Run the database migrations, this creates automatically a db.sqlite3 file
$python manage.py migrate

```
```python
# in order to using the database cache, you must 
# create the cache table with this command:
$python manage.py createcachetable

```
For caching this API uses a low-level cache API who is used to store objects in the database cache table.
The data stored will be available for 2 minutes.

```python
# Run the local server
$python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 28, 2022 - 06:21:10
Django version 3.2, using settings 'yoyoEngTest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.



```


## Usage

> Open the browser and go to the endpoint and enter the  requested location and days.
ex:
  > Go to  http://127.0.0.1:8000/api/location/Nairobi/?days=10


<img src="https://github.com/evantoh/weather/blob/main/images/url.png" width="700">


> Closer view from the JSON response of the requested location and days.
ex:
  >   http://127.0.0.1:8000/api/location/Nairobi/?days=10

<img src="https://github.com/evantoh/weather/blob/main/images/apiResponse.png" width="700">

> if any error is generated ,you should receive an error message .
ex:
<img src="https://github.com/evantoh/weather/blob/main/images/errorMessage.png" width="700">




## Testing
The tests are using REST framework's test case classes and are defined in the file "temperature/tests.py".
The test will check the correct functioning of the code within the functions of the views and the modules created
sending requests and comparing them with expected values.
In order to carry out the tests, you need to have running the API locally and open another terminal.


```python
# Go to the project file "yoyoEngTest"
$python manage.py test

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.983s

OK
Destroying test database for alias 'default'...


## Setup
To run locally
