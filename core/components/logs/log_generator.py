from datetime import datetime
import logging
from dataclasses import dataclass
from core.components.config.reader import ConfigReader
from functools import wraps


@dataclass
class Log:

    config = ConfigReader()
    time = datetime.now()
    logs_path = config.read('path', 'logs')
    logging.basicConfig(filename=f'{logs_path}/{"logs.log"}',
                        datefmt=f'{time:%A | %B | %d/%m/%y | %X |}',
                        level=logging.INFO,
                        format='%(asctime)s:'
                                 '%(levelname)s:'
                                 '%(message)s')

    @staticmethod
    def get_log() -> logging:

        @wraps
        def decorator() -> None:
            logger = logging.getLogger()
            logger.setLevel('INFO')
            logger.setLevel('DEBUG')
            logger.setLevel('WARNING')
            logger.setLevel('ERROR')
            logger.setLevel('FATAL')

        return decorator
