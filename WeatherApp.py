#WeatherApp.py
#Name:
#Date:
#Assignment:

import WeatherInfo

#Set your key
WeatherInfo.setKey("2cecbd80c3163c2ecbf29f8d2b8cfffa")
WeatherInfo.setCity("Boston")

success = WeatherInfo.updateWeather()

if(success == True):
  print("It worked")
else:
  print("Invalid City")

temp = WeatherInfo.getTemp()
print(temp)
#Ask the user for their city

#Update the weather with the given city

#Request any data you need from the WeatherInfo API

#Process the data
#convert temperature to fahrenheit,
#determine wind speed in words
#decide jacket and umbrella status

#Report to the user the weather of their city

#Ask user if they would like another weather report
#If yes, loop to the top of your program where they are asked for a city.
#If no, end with a goodbye statement of some sort.
