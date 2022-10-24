from dataclasses import dataclass
from core.utils.driver.manager import DriverManager, DriverEngine
from core.utils.config.reader import ConfigReader
from core.utils.driver.run_tests import RunTests


@dataclass
class WorkLog(DriverManager, DriverEngine):

    config: str = ConfigReader()

    def setup(self) -> None:
        self.driver.get(self.config.read('jira', 'link'))
        self.driver.implicitly_wait(5)

    def login(self) -> None:
        self.get_element('Jira', 'username').send_keys(self.config.read('jira', 'username'))
        self.get_element('Jira', 'password').send_keys(self.config.read('jira', 'password'))
        self.get_element('Jira', 'login_button').click()

    def navigate(self) -> None:
        self.get_element('Jira', 'drop_down').click()
        self.get_element('Jira', 'log_work').click()
        self.get_element('Jira', 'time_spent').send_keys(f"{self.config.read('jira', 'work_hours')}h")

    def set_day(self) -> None:
        self.get_element('Jira', 'date').click()
        self.get_element('Jira', 'log').click()

    def exit_all(self) -> None:
        self.teardown()


def test() -> None:
    run_test = RunTests(class_name=WorkLog())
    run_test.start(methods=[
        'setup',
        'login',
        'navigate',
        'set_day',
        'exit_all'
    ])


if __name__ == '__main__':
    test()
