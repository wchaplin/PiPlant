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
