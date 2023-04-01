import shelve
from core.infrastructure.driver.engine import DriverEngine


data = {
    'intro_page': DriverEngine('IntroPage'),
    'terminal_x': DriverEngine('TerminalX')
}


class DataBases:

    @staticmethod
    def shelve_drivers() -> None:
        with shelve.open('DriverDB') as db:
            db.update(data)
