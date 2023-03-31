from core.infrastructure.driver.engine import DriverEngine
from core.infrastructure.modules.reader import read_json


driver = DriverEngine('cupid')
data = read_json(path=r'C:\Users\medvi\OneDrive\Desktop\Cellenium\tests\cupid\credentials.json')


class TestIntroPage:

    def test_setup(self) -> None:
        driver.get_web(web_link='https://www.okcupid.com', maximize_window=True)

    def test_navigate(self) -> None:
        driver.driver.implicitly_wait(10)
        driver.get_element('sign_in').click()
        driver.get_element('username').send_keys(data['username'])
        driver.get_element('password').send_keys(data['password'])
        driver.get_element('login_button').click()

    def test_exit_all(self) -> None:
        driver.teardown()
