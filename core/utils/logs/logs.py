import logging
import datetime
from dataclasses import dataclass
from core.utils.config.reader import ConfigReader
import functools


@dataclass
class LogGenerator:

    config = ConfigReader()
    path: str = config.read('path', 'logs')
    name: object = __name__

    @staticmethod
    def _time_and_date() -> str:
        time = datetime.datetime.now()
        return f'{time: %A %D %X}'

    def __call__(self):
        logging.basicConfig(filename=f'{self.path}/{self.name}.log',
                            format='%(asctime)s',
                            level=logging.INFO,
                            datefmt=self._time_and_date())
        log = logging.getLogger()
        return log.info(self.name)


@LogGenerator
def app():
    return 1


if __name__ == '__main__':
    app()

