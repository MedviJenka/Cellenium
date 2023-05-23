from core.infrastructure.driver.engine import DriverEngine
from core.infrastructure.modules.reader import read_json


data = read_json(r'C:\Cellenium\tests\sync_service\data.json')
username = data['username']
password = data['password']


class TestIntroPage:

    engine = DriverEngine('Jira')

    def test_setup(self) -> None:
        self.engine.get_web(web_link='https://acjira/browse/SMAR-7397?filter=-1', maximize_window=True)

    def test_login(self) -> None:
        self.engine.get_element('username').send_keys(username)
        self.engine.get_element('password').send_keys(password)
        self.engine.get_element('login_button').click()

    def test_navigate(self) -> None:
        self.engine.get_element('drop_down').click()
        self.engine.get_element('log_work').click()
        self.engine.get_element('time_spent').send_keys('9h')
        self.engine.get_element('log').click()

    def test_exit_all(self) -> None:
        self.engine.teardown()
