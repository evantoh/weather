""" Request handler module."""
import os
import requests
import statistics



def getMaximumTemp(maximumValues):
    return max(maximumValues)


def getMinimumTemp(minimumValues):
    return max(minimumValues)

def getAverageTemp(minimumValues):
    avg = sum(minimumValues) / len(minimumValues)

    return avg

def getMedianTemp(minimumValues):
    medianValue = statistics.median(minimumValues)

    return medianValue



def get_weather(location, days):
    """ Function to handle the requests to
        the 3rd API http://api.openweathermap.org ;
        Takes as arguments str "city" and "country",
        and returns the formatted dictionary."
    """
    # print("env",os.environ)
    # api_key = os.environ.get('WEATHER_SECRET_APIKEY')
    api_key = "09e04c00833e472abbf123842222109"
    # url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&mode=xml"  # 3rd API"api.openweathermap.org" URL

    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={days}&aqi=no&alerts=no"

    response = requests.get(url)  # Response object




    # data_json = json.dumps(xmltodict.parse(response.content))  # Converting the response to a json data
    forecastData=response.json()['forecast']['forecastday']
    maxValuesList = []
    minValuesList = []
    for data in forecastData:
        # get Maximum value based on parameters passed i.e location and number of days
        maxValuesList.append(data['day']['maxtemp_c'])

        # get minimum value based on parameters passed i.e location and number of days
        minValuesList.append(data['day']['mintemp_c'])

        # get average value based on parameters passed i.e location and number of days
        minValuesList.append(data['day']['mintemp_c'])


    getMaximumTemps = getMaximumTemp(maxValuesList)
    getMinimumTemps = getMinimumTemp(minValuesList)
    getAverageTemps = getAverageTemp(minValuesList)
    getMedianTemps = getMedianTemp(minValuesList)



    # print("getMedianTemps",getMedianTemps)




    # Final formatted data dictionary
    weather_dict = {
            "maximum": getMaximumTemps,
            "minimum": getMinimumTemps,
            "average": getAverageTemps,
            "median": getMedianTemps
            }

    return weather_dict  # Send the dictionary to the view
