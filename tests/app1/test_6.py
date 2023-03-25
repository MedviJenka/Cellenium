from core.infrastructure.driver.engine import DriverEngine


engine = DriverEngine()


def test_facebook() -> None:
    engine.driver.get('https://www.facebook.com')


def test_git() -> None:
    engine.driver.get('https://www.github.com')
