from core.infrastructure.driver.engine import DriverEngine
from core.infrastructure.modules.reader import read_json


file = read_json(r'C:\Users\medvi\OneDrive\Desktop\credentials.json')
USERNAME = file['username']
PASSWORD = file['password']


class TestIntroPage:

<<<<<<< HEAD
<<<<<<< HEAD
    driver = DriverEngine(page_base_screen='cupid')
=======
    driver = DriverEngine(screen='cupid')
>>>>>>> a6ecf81 (fun)
=======
    driver = DriverEngine(page_base_screen='cupid')
>>>>>>> 6596ac3 (a)

    def test_setup(self) -> None:
        self.driver.get_web(web_link='https://www.okcupid.com/who-you-like?cf=likesIncoming', maximize_window=False)

    def test_login(self) -> None:
        self.driver.get_element('username').send_keys(USERNAME)
        self.driver.get_element('password').send_keys(PASSWORD)
        self.driver.get_element('login_button').click()
        # [self.driver.get_element('send_code_button').click() for _ in range(3)]
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> a6ecf81 (fun)
=======
>>>>>>> 6596ac3 (a)
