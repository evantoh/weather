from django.urls import path
from temperature import views


urlpatterns = [
    # parameter City is only restricted to data type string
    path('api/location/<str:city>/', views.weather_detail),# /api/locations/{city}/?days={number_of_days}

]