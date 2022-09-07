from dataclasses import dataclass
import requests
from requests import Response
from core.utils.config.reader import ConfigReader


@dataclass
class RestRequests:

    config = ConfigReader()
    url: str = "https://api.openweathermap.org/data/2.5/weather?"
    api_key: str = config.read('open_weather', 'API_KEY')

    # ~~~~~~~~~ Global Data ~~~~~~~~~~~
    def get_city(self, city: str) -> Response:
        call = fr"appid={ self.api_key }&q={ city }"
        request = requests.get(fr'{ self.url }{ call }')
        return request.json()

    def get_coordinates(self, lat: float, lon: float) -> Response:
        call = fr"lat={lat}&lon={lon}&appid={self.api_key}"
        request = requests.get(fr'{ self.url }/{ call }')
        print(request)
        return request.json()

    # ~~~~~~~~~ Temperature Conversion ~~~~~~~~~~~
    @staticmethod
    def _kelvin_to_celsius_conversion(kelvin) -> int:
        celsius = kelvin - 273.15
        return round(celsius)

    def _kelvin_to_fahrenheit_conversion(self, kelvin) -> int:
        fahrenheit = self._kelvin_to_celsius_conversion(kelvin) * (9 / 5) + 32
        return round(fahrenheit)

    # ~~~~~~~~~ Atmosphere Condition ~~~~~~~~~~~
    def get_temperature(self, city: str) -> str:
        kelvin = self.get_city(city)['main']['temp']
        celsius = self._kelvin_to_celsius_conversion(kelvin)
        return f'temperature in { city }: { celsius } C.'

    def get_clouds_and_visibility(self, city: str) -> str:
        visibility = self.get_city(city)['main']
        description = self.get_city(city)['main']
        return f'city: { city }\nvisibility: { visibility }\nsky condition: { description }'

    def get_pressure(self, city: str) -> str:
        pressure = self.get_city(city)['main']['pressure']
        return f'city: { city }\npressure: { pressure } HPa'


rest = RestRequests()
a = rest.get_temperature("tel-aviv")
b = rest.get_city('beer sheva')['main']['pressure']
c = rest.get_clouds_and_visibility('eilat')
d = rest.get_pressure('eilat')
# print(a)
# print(b)
# print(c)
print(d)
"""

{'coord': {'lon': 34.7906, 'lat': 31.2525}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 303.7, 'feels_like': 303.12, 'temp_min': 303.7, 'temp_max': 303.7, 'pressure': 1008, 'humidity': 37, 'sea_level': 1008, 'grnd_level': 976}, 'visibility': 10000, 'wind': {'speed': 5.97, 'deg': 302, 'gust': 4.08}, 'clouds': {'all': 0}, 'dt': 1662551910, 'sys': {'type': 2, 'id': 2002441, 'country': 'IL', 'sunrise': 1662520818, 'sunset': 1662566280}, 'timezone': 10800, 'id': 295530, 'name': 'Beer Sheva', 'cod': 200}

Process finished with exit code 0
"""