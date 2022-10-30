from core.components.driver.manager import DriverManager
from functools import wraps


class WriteTestSteps(DriverManager):

    def write_steps(self) -> callable:

        @wraps
        def __call__(*args):
            for _ in self.driver.find_element(*args):
                print("action")

        return __call__
