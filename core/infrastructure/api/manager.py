from dataclasses import dataclass
import requests
from requests import Response
from core.infrastructure.modules.methods import read_config
import datetime


@dataclass
class RestRequests:

    url: str = "https://api.openweathermap.org/data/2.5/weather?"
    api_key: str = read_config('open_weather', 'API_KEY')

    # ~~~~~~~~~ Global Data ~~~~~~~~~~~
    def get_response_status_code(self) -> int:
        request = requests.get(f'{self.url}/appid={self.api_key}')
        return request.status_code

    def get_city(self, city: str) -> Response:
        call = fr"appid={ self.api_key }&q={ city }"
        request = requests.get(fr'{ self.url }{ call }')
        return request.json()

    def get_coordinates(self, lat: float, lon: float) -> Response:
        call = fr"lat={lat}&lon={lon}&appid={self.api_key}"
        request = requests.get(fr'{ self.url }/{ call }')
        return request.json()

    # ~~~~~~~~~ Temperature and Time Conversion ~~~~~~~~~~~
    @staticmethod
    def _kelvin_to_celsius_conversion(kelvin) -> int:
        celsius = kelvin - 273.15
        return round(celsius)

    def _kelvin_to_fahrenheit_conversion(self, kelvin) -> int:
        fahrenheit = self._kelvin_to_celsius_conversion(kelvin) * (9 / 5) + 32
        return round(fahrenheit)

    @staticmethod
    def _time(value: float) -> any:
        generate = datetime.datetime.utcfromtimestamp(value)
        return generate

    # ~~~~~~~~~ Atmosphere Condition ~~~~~~~~~~~
    def get_temperature(self, city: str) -> str:
        kelvin = self.get_city(city)['main']['temp']
        celsius = self._kelvin_to_celsius_conversion(kelvin)
        return f'temperature in { city }: { celsius } C.'

    def get_clouds_and_visibility(self, city: str) -> str:
        visibility = self.get_city(city)['main']
        description = self.get_city(city)['weather'][0]['main']
        return f'city: { city }\nvisibility: { visibility }\nsky condition: { description }'

    def get_pressure(self, city: str) -> str:
        pressure = self.get_city(city)['main']['pressure']
        return f'city: { city }\npressure: { pressure } HPa'
