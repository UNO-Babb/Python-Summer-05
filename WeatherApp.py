#WeatherApp.py
#Name:
#Date:

import WeatherInfo

#Set your key
def setup(city):
    WeatherInfo.setKey("6e5e3294fb74c2b9b6b0f97f82a2c646")
    WeatherInfo.setCity(city)

    #When you call updateWeather() it will retrieve new weather data from the server.
    #We only need to do this when changing cities or if we have not already called it.
    success = WeatherInfo.updateWeather()
    if(success == True):
      print("It worked")
    else:
      print("Invalid City")

## Function that will take temperature in Kelvin and convert to Fahrenheit
def kelvinToFahrenheit(kTemp):
    return 0

## Function that will return a weather report including:
## The city, the description, and the humidity
def report(city, description, humidity):
    return "CITY REPORT"

## Return the string with the temperature given
def tempReport(fTemp):
    return "TEMP REPORT"

## Return the Beaufort scale speed of the given wind.
def windToBeaufort(windSpeed):
    return "Beaufort"


## Return the string of the wind report including speed and Beaufort
def windReport(windSpeed):
    return "SPEED"

## Return a string about whether we need an umbrella
def checkUmbrella(description):
    return "Umbrella"

## Return a string about whether we need a jacket
def checkJacket(feelsTemp):
    return "Jacket"


def test():
    t = 300
    fTemp = kelvinToFahrenheit(t)
    print(fTemp)


def main():
    setup("Omaha")

    temp = WeatherInfo.getTemp()
    print(temp)


#main()
test()
