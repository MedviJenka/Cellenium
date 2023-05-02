from core.infrastructure.driver.engine import DriverEngine
from core.infrastructure.modules.reader import read_json


path = r"C:\Users\evgenyp\Desktop\data.json"
username = read_json(path)['username']
password = read_json(path)['password']


class TestLoginSTNG:

    engine = DriverEngine('ST')

    def test_setup(self) -> None:
        self.engine.get_web(web_link='https://nextgenkube.ai-logix.net')

    def test_login(self) -> None:
        self.engine.get_element('login_with_microsoft').click()
        self.engine.get_element('username').send_keys(username)
        self.engine.get_element('next_button').click()
        self.engine.get_element('password').send_keys(password)

    def test_sign_in(self) -> None:
        self.engine.press_keyboard_key('enter')
