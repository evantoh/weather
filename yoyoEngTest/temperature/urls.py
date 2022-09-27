from django.urls import path
from temperature import views


urlpatterns = [
    path('api/', views.weather_detail),

    # path(
    #     route = 'locations/<str:city>/', # /api/locations/{city}/?days={number_of_days}
    #     view = views.weather_detail,
    # )
]