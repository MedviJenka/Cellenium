from dataclasses import dataclass
from core.utils.driver.run_tests import RunTests
from core.api.requests.manager import RestRequests


@dataclass
class TestCityWeather:

    rest = RestRequests()

    def get_beer_sheva_temperature(self) -> str:
        self.rest.get_response_status_code()
        return self.rest.get_temperature('beer-sheva')


def test() -> None:
    test_city_weather = TestCityWeather()
    run = RunTests(test_city_weather)
    run.start(["get_beer_sheva_temperature"])


if __name__ == "__main__":
    test()
