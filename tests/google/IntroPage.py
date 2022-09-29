from dataclasses import dataclass
from core.utils.driver.manager import DriverManager, DriverEngine
from core.utils.driver.run_tests import RunTests


@dataclass
class IntroPage(DriverManager, DriverEngine):

    def setup(self) -> None:
        self.driver.get('https://www.google.com')

    def navigate(self) -> None:
        self.get_element('FirstPage', 'search').send_keys('cats')

    def find_button(self) -> None:
        self.get_element('FirstPage', 'button')

    def exit_all(self) -> None:
        self.teardown()


 # IN a different file  (because each file should be respponsible for only 1 thing- 
# for example, the "intoPage.py" should define the mothods to get elements (like you did)
# And another file in another folder would be "introPageTests.py"
# And these functions will be there: 
import ....bla bla...


intro_page = IntroPage(DriverManager, DriverEngine)
        
def test() -> None:

    run_test = RunTests(class_name=IntroPage())
    run_test.start([intro_page.setup,
                    intro_page.navigate,
                    intro_page.find_button,
                    intro_page.exit_all ])

    

    

if __name__ == '__main__':
    test()
