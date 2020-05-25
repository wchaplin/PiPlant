import requests
class WeatherParent:
    def __init__(self,weather, main, wind):
        self.Weather = weather
        self.Main = main
        self.Wind = wind        

class WeatherData:
    def __init__(self, id, main, description):
        self.id = id
        self.main = main
        self.description = description

class MainData:
        def __init__(self, temp, feels_like, temp_min, temp_max, pressure, humidity):
            self.temp = temp
            self.feelsLike = feels_like
            self.tempMin = temp_min
            self.pressure = pressure
            self.humidity = humidity

class WindData:
    def __init__(self, speed, deg):
        self.speed = speed
        self.deg = deg


class WeatherOutput():
    def getWeather(self):
        req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Casselberry,us&appid=38a5826d48f6e2cdd45c3d50b37f192d")
        req = req.json()
        weather = req["weather"][0]
        main = req["main"]
        wind = req["wind"]
        weatherData = WeatherData(weather["id"],weather["main"],weather["description"])
        mainData = MainData(main["temp"],main["feels_like"],main["temp_min"],main["temp_max"],main["pressure"],main["humidity"])
        windData = WindData(wind["speed"],wind["deg"])
        weatherParent = WeatherParent(weatherData,mainData,windData)
        return(weatherParent)

weather = WeatherOutput()
weatherResult = weather.getWeather()
print(weatherResult)


