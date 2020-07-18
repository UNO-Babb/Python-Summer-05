import urllib.request, json

user_key = ""
user_city = "Omaha"
description = "No Data"
feels_like = "No Data"
kelvin_temp = 0
humidity = 0
pressure = 0
wind_speed = 0


def setKey(key):
    global user_key
    user_key = key

def setCity(city):
    global user_city
    user_city = city.replace(" ", "%20")

def updateWeather():
    global description, feels_like, kelvin_temp, humidity, pressure, wind_speed
    weatherURL = "https://api.openweathermap.org/data/2.5/weather?q=" + user_city + "&APPID=" + user_key
    try:
        with urllib.request.urlopen(weatherURL) as url:
            data = json.loads(url.read().decode())
            #print(data)
            description = data['weather'][0]['description']

            kelvin_temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']

            wind_speed = data['wind']['speed']
    except:
        print ("Invalid city")
        return False

    return True

def getDescription():
    return description

def getTemp():
    return kelvin_temp

def getFeelsLike():
    return feels_like

def getHumidity():
    return humidity

def getPressure():
    return pressure

def getWindSpeed():
    return wind_speed
