from core.components.driver.run_tests import RunTests
from tests.google.IntroPage import IntroPage
from tests.jira.JiraAutomation import WorkLog
from tests.weathermap.CityWeather import TestCityWeather


def test() -> None:
    run_test_1 = RunTests(class_name=IntroPage())
    run_test_1.start(['setup',
                    'navigate',
                    'find_button',
                    'exit_all'])

    run_test_2 = RunTests(class_name=TestCityWeather())
    run_test_2.start(["get_beer_sheva_temperature"])

    run_test_3 = RunTests(class_name=WorkLog())
    run_test_3.start(methods=[
        'setup',
        'login',
        'navigate',
        'set_day',
        'exit_all'
    ])


if __name__ == '__main__':
    test()
