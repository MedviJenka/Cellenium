from datetime import datetime
import logging
from dataclasses import dataclass
from core.components.config.reader import ConfigReader
global log


@dataclass
class Log:

    config = ConfigReader()
    time = datetime.now()
    logs_path = config.read('path', 'logs')
    logging.basicConfig(filename=f'{logs_path}/{"logs.log"}',
                        datefmt=f'{time:%A | %B | %d/%m/%y | %X |}',
                        level=logging.DEBUG,
                        format='%(asctime)s:'
                                 '%(levelname)s:'
                                 '%(message)s')

    @staticmethod
    def get_log(name=__name__) -> logging:
        logger = logging.getLogger(name)
        logger.setLevel('CRITICAL')
        logging.debug(name)


if __name__ == '__main__':
    log = Log()
    log = log.get_log()
