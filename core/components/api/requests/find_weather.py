from dataclasses import dataclass
import requests


BASE_URL: str = "https://api.openweathermap.org/data/2.5/weather"
API = BASE_URL + "?q={city_name}&appid={api_key}&units=metric"


@dataclass
class SendRequest:

    @staticmethod
    def find_weather_for(city) -> dict:
        url = API.format(city_name=city, api_key="")
        response = requests.get(url)
        return response.json()


def main() -> None:
    send = SendRequest()
    send.find_weather_for("tel-aviv")


if __name__ == '__main__':
    main()
