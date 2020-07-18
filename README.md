# Homework 1

### OpenWeather API Key
For this assignment, you will need to be able to read data from the Open Weather Map data source. They have an Application Programming Interface (API) available to developers to access this data. You will need to sign up on the website as a developer.
- [https://openweathermap.org/api](https://openweathermap.org/api)
- Sign up for the Current weather data service
- You will get a developer key which is a 32 digit hexadecimal number
- This key will be used in your project.

## WeatherInfo.py
When you read info from the OpenWeather API, it comes as a JSON data stream. I have created an intermediate API for you to more easily get specific weather values from this JSON data. The various functions are described below along with an example of how they would work in your WeatherApp.py program.

### setKey(key)
Use this function to set your private API key for OpenWeather
```
WeatherInfo.setKey("1234567890abcdef")
```
### updateWeather()
Once your key is set, this will make the call to the OpenWeather database for a live weather update. This must be done before any of the other calls will return accurate weather information.
This function will return a **boolean** value to indicate if the call was successful. For example, if the defined city is not valid or misspelled, the function will get an error from the OpenWeather API. In this case, the function would return *False* to indicate that the call was not successful.
If the weather data is successfully updated, the function will return *True*
```
success = WeatherInfo.updateWeather()

if(success == True):
  print("It worked")
else:
  print("Invalid City")
```
### getDescription()
This function will return a **string** value that is the current weather description.
Example descriptions:
- light clouds
- heavy rain
- sunny

```
print(WeatherInfo.getDescription())
description = WeatherInfo.getDescription()
```

### getTemp()
Returns a **float** of the current temperature. The unit of this temperature is Kelvin.
```
print(WeatherInfo.getTemp())
temp = WeatherInfo.getTemp()
```

### getFeelsLike()
Returns a **float** of the current "feels like" temperature in Kelvin. *Feels like* is a unit that combines the air temp, wind speed, and humidity to give an adjusted temperature to what it would feel like outside.
```
print(WeatherInfo.getFeelsLike())
feelTemp = WeatherInfo.getFeelsLike()
```

### getHumidity()
Returns an **integer** value in the range (0-100) on how humid it is currently.
```
print(WeatherInfo.getHumidity())
humidity = WeatherInfo.getHumidity()
```

### getPressure()
Returns an **integer** value for the barometric pressure.
```
print(WeatherInfo.getPressure())
pressure = WeatherInfo.getPressure()
```

### getWindSpeed()
Returns a **float** value for the current wind speed measured in miles per hour.
```
print(WeatherInfo.getWindSpeed())
speed = WeatherInfo.getWindSpeed()
```
---
## Program Requirements
- Ask the user for their city.
  - If the user leaves it blank, assume that they want the weather data for Omaha.
- Report the current weather for the user selected city.
- Ask the user if they would like to get the weather report for another city.
  - This should be answered in a clear way defined in the program.
  - In other words, let the user know how they should respond to your question as part of the question.
- Repeat the process as many times as the user continues.

### For each weather report
- Provide an intro so the user knows what city this info is for.
- Provide the following information:
  - Weather Description
  - Temperature (in Fahrenheit) as a whole number
  - Humidity
  - Wind Speed **and** wind Beaufort description
  - What I should wear today (see below)

### What to wear
To make this app more useful, we want to give advice on what the user should wear based on the current weather conditions.

#### Jackets
Based on the *feels like* temperature the user should wear:
- light jacket (55 - 65 Fahrenheit)
- medium jacket (40 - 54 Fahrenheit)  
- heavy coat (below 40 Fahrenheit)

#### Umbrella
The user should bring an umbrella if it is raining.
This info will be found in the description.
Rain Types:
- mist
- light rain
- rain
- heavy rain

### Wind speed descriptions
The Beaufort scale is an empirical measure that relates wind speed to observed conditions at sea or on land. Its full name is the Beaufort wind force scale.[Wikipedia](https://en.wikipedia.org/wiki/Beaufort_scale)
- Calm (<1 mph)
- Light air (1-3 mph)
- Light breeze (4-7 mph)
- Gentle breeze (8-12 mph)
- Moderate breeze (13-18 mph)
- Fresh breeze (19-24 mph)
- Strong breeze (25-31 mph)
- High wind (32-38 mph)
- Gale (39-46 mph)
- Strong gale (47-54 mph)
- Storm (55-63 mph)
- Violent storm (64-72 mph)
- Hurricane (>= 73 mph)

### Sample Output
Enter city: *Omaha*  
The current weather in *Omaha* is *broken clouds* with *87*% humidity.  
Temperature: 35 degrees Fahrenheit  
Wind speed: 2.12 mph - Light air  
You should wear a heavy coat today.

Would you like another weather report (Y/N): *Y*  

Enter city: *Orlando*  
The current weather in *Orlando* is *clear sky* with *67*% humidity.  
Temperature: 59 degrees Fahrenheit  
Wind speed: 3.8 mph - Light breeze  
You should wear a light jacket today.

Would you like another weather report (Y/N): *N*  

Have a nice day.
