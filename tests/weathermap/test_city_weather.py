from dataclasses import dataclass
from core.infrastructure.api.manager import RestRequests
from core.infrastructure.modules.methods import run_test


@dataclass
class TestCityWeather:

    rest = RestRequests()

    def get_beer_sheva_temperature(self) -> str:
        self.rest.get_response_status_code()
        return self.rest.get_temperature('beer-sheva')


def test() -> None:
    run_test(TestCityWeather(), ["get_beer_sheva_temperature"])


if __name__ == "__main__":
    test()
