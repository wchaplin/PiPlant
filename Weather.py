import requests

class WeatherOutput():
    def getWeather(self):
        req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Casselberry,us&appid=38a5826d48f6e2cdd45c3d50b37f192d")
        return(req)

weather = WeatherOutput()
weatherResult = weather.getWeather()
print(weatherResult.content)