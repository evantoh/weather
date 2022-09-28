""" Request handler module."""
import os
import requests
import statistics



def getMaximumTemp(maximumValues):
    return max(maximumValues)


def getMinimumTemp(minimumValues):
    return min(minimumValues)

def getAverageTemp(minimumValues):
    avg = sum(minimumValues) / len(minimumValues)

    return avg

def getMedianTemp(minimumValues):
    medianValue = statistics.median(minimumValues)

    return medianValue

# def minMaxAveMedListfn(minimumValues):
#
#     # get max value using max() method
#     maximumValue = max(minimumValues)
#
#     # get min value using min() method
#     minimumValue =  min(minimumValues)
#
#     # get average by using sum and len method
#     avg = sum(minimumValues) / len(minimumValues)
#
#     # get median using statistics module inbuilt module statistics
#     medianValue = statistics.median(minimumValues)
#
#     return maximumValue,minimumValue,avg,medianValue


def get_weather(location, days):
    """ Function to handle the requests to
        the 3rd API http://api.weatherapi.com/v1 ;
        Takes as arguments str "city" and "number_of_days",
        and returns the formatted dictionary
        "
    """
    # print("env",os.environ)
    api_key = os.environ.get('WEATHER_SECRET_APIKEY')
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={days}&aqi=no&alerts=no"
    response = requests.get(url)  # Response object


    # looping through data returned after SuccessFul api call and handling exceptions
    try:
        forecastData=response.json()['forecast']['forecastday']
        maxValuesList = []
        minValuesList = []
        aveValuesList = []
        for data in forecastData:
            # get Maximum value based on parameters passed i.e location and number of days using key maxtemp_c
            maxValuesList.append(data['day']['maxtemp_c'])

            # get minimum value based on parameters passed i.e location and number of days using key mintemp_c
            minValuesList.append(data['day']['mintemp_c'])

            # get average value based on parameters passed i.e location and number of days using key avgtemp_c
            aveValuesList.append(data['day']['avgtemp_c'])

        getMaximumTemps = getMaximumTemp(maxValuesList)
        getMinimumTemps = getMinimumTemp(minValuesList)
        getAverageTemps = getAverageTemp(aveValuesList)
        getMedianTemps = getMedianTemp(minValuesList)

        # Final formatted data dictionary
        weather_dict = {
                "maximum": getMaximumTemps,
                "minimum": getMinimumTemps,
                "average": getAverageTemps,
                "median": getMedianTemps
                }

        return weather_dict  # Send the dictionary to the view
    except Exception as e:
        return {"Erro": e,"status_code":response.status_code } # use status code as key for error handling exceptions
