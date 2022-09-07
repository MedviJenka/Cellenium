from core.utils.driver.manager import *
from dataclasses import dataclass
from core.utils.config.reader import ConfigReader


@dataclass
class WorkLog(DriverManager, DriverEngine, RunTest):

    config = ConfigReader()

    def setup(self) -> None:
        self.driver.get(self.config.read('jira', 'link'))
        self.driver.implicitly_wait(5)

    def login(self) -> None:
        self.get_element('jira', 'username').send_keys(self.config.read('jira', 'username'))
        self.get_element('jira', 'password').send_keys(self.config.read('jira', 'password'))
        self.get_element('jira', 'login_button').click()

    def navigate(self) -> None:
        self.get_element('jira', 'drop_down').click()
        self.get_element('jira', 'log_work').click()
        self.get_element('jira', 'time_spent').send_keys(self.config.read('jira', 'work_hours'))

    def set_day(self) -> None:
        self.get_element('jira', 'date').click()
        self._submit()

    def _submit(self) -> None:
        self.get_element('jira', 'log').click()
        self.get_element('jira', 'log').click()

    def exit_all(self) -> None:
        self.teardown()


def test() -> None:
    run_test = RunTest(class_name=WorkLog())
    run_test.start([
        'setup',
        'login',
        'navigate',
        'set_day',
        'exit_all'
    ])


if __name__ == '__main__':
    test()
