from core.components.functional.methods import generate_allure_report, Decorators


decorator = Decorators()


@decorator.measure_execution_time
def test() -> None:
    assert 1 + 1 == 2


generate_allure_report(__file__)
